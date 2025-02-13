"""Base Anomaly Module for Training Task."""

# Copyright (C) 2022 Intel Corporation
# SPDX-License-Identifier: Apache-2.0

from __future__ import annotations

import logging
from abc import ABC
from typing import Any, OrderedDict
from warnings import warn

import pytorch_lightning as pl
from anomalib.models.components.losses import dice
import torch
from pytorch_lightning.callbacks import Callback
from pytorch_lightning.utilities.types import STEP_OUTPUT
from torch import Tensor, nn
from torchmetrics import Metric

from anomalib.data.utils import boxes_to_anomaly_maps, boxes_to_masks, masks_to_boxes
from anomalib.post_processing import ThresholdMethod
from anomalib.utils.metrics import (
    AnomalibMetricCollection,
    AnomalyScoreDistribution,
    AnomalyScoreThreshold,
    MinMax,
)

logger = logging.getLogger(__name__)


class AnomalyModule(pl.LightningModule, ABC):
    """AnomalyModule to train, validate, predict and test images.

    Acts as a base class for all the Anomaly Modules in the library.
    """

    def __init__(self) -> None:
        super().__init__()
        logger.info("Initializing %s model.", self.__class__.__name__)

        self.save_hyperparameters()
        self.model: nn.Module
        self.loss: nn.Module
        self.callbacks: list[Callback]

        self.threshold_method: ThresholdMethod
        self.image_threshold = AnomalyScoreThreshold().cpu()
        self.pixel_threshold = AnomalyScoreThreshold().cpu()

        self.normalization_metrics: Metric

        self.image_metrics: AnomalibMetricCollection
        self.pixel_metrics: AnomalibMetricCollection
        self.false_good = 0
        self.false_bad = 0
        self.validation_outputs = []
        self.test_outputs = []

    def forward(self, batch: dict[str, str | Tensor], *args, **kwargs) -> Any:
        """Forward-pass input tensor to the module.

        Args:
            batch (dict[str, str | Tensor]): Input batch.

        Returns:
            Tensor: Output tensor from the model.
        """
        del args, kwargs  # These variables are not used.

        return self.model(batch)

    def validation_step(self, batch: dict[str, str | Tensor], *args, **kwargs) -> STEP_OUTPUT:
        """To be implemented in the subclasses."""
        raise NotImplementedError

    def predict_step(self, batch: Any, batch_idx: int, dataloader_idx: int = 0) -> Any:
        """Step function called during :meth:`~pytorch_lightning.trainer.trainer.Trainer.predict`.

        By default, it calls :meth:`~pytorch_lightning.core.lightning.LightningModule.forward`.
        Override to add any processing logic.

        Args:
            batch (Any): Current batch
            batch_idx (int): Index of current batch
            dataloader_idx (int): Index of the current dataloader

        Return:
            Predicted output
        """
        del batch_idx, dataloader_idx  # These variables are not used.

        outputs: Tensor | dict[str, Any] = self.validation_step(batch)
        self._post_process(outputs)
        if outputs is not None and isinstance(outputs, dict):
            outputs["pred_labels"] = outputs["pred_scores"] >= self.image_threshold.value
            if "anomaly_maps" in outputs.keys():
                outputs["pred_masks"] = outputs["anomaly_maps"] >= self.pixel_threshold.value
                if "pred_boxes" not in outputs.keys():
                    outputs["pred_boxes"], outputs["box_scores"] = masks_to_boxes(
                        outputs["pred_masks"], outputs["anomaly_maps"]
                    )
                    outputs["box_labels"] = [torch.ones(boxes.shape[0]) for boxes in outputs["pred_boxes"]]
            # apply thresholding to boxes
            if "box_scores" in outputs and "box_labels" not in outputs:
                # apply threshold to assign normal/anomalous label to boxes
                is_anomalous = [scores > self.pixel_threshold.value for scores in outputs["box_scores"]]
                outputs["box_labels"] = [labels.int() for labels in is_anomalous]

        return outputs

    def test_step(self, batch: dict[str, str | Tensor], batch_idx: int, *args, **kwargs) -> STEP_OUTPUT:
        """Calls validation_step for anomaly map/score calculation.

        Args:
          batch (dict[str, str | Tensor]): Input batch
          batch_idx (int): Batch index

        Returns:
          Dictionary containing images, features, true labels and masks.
          These are required in `on_validation_epoch_end` for feature concatenation.
        """
        del args, kwargs  # These variables are not used.

        return self.predict_step(batch, batch_idx)

    def on_validation_batch_end(self, outputs: STEP_OUTPUT, *args, **kwargs) -> STEP_OUTPUT:
        """Called at the end of each validation step."""
        del args, kwargs  # These variables are not used.

        self._outputs_to_cpu(outputs)
        self._post_process(outputs)

        self.validation_outputs.append(outputs)

    def on_test_batch_end(self, outputs: STEP_OUTPUT, *args, **kwargs) -> STEP_OUTPUT:
        """Called at the end of each test step."""
        del args, kwargs  # These variables are not used.

        self._outputs_to_cpu(outputs)
        self._post_process(outputs)
        self.test_outputs.append(outputs)

    def on_validation_epoch_end(self) -> None:
        """Compute threshold and performance metrics."""
        outputs = self.validation_outputs
        if self.threshold_method == ThresholdMethod.ADAPTIVE:
            self._compute_adaptive_threshold(outputs)

        if hasattr(self.image_metrics, "F1Score"):
            self.log("image_F1_threshold", self.image_metrics.F1Score.threshold)
            logging.info("Image f1 threshold {%s}", self.image_metrics.F1Score.threshold)

        if hasattr(self.pixel_metrics, "F1Score"):
            self.log("pixel_F1_threshold", self.pixel_metrics.F1Score.threshold)
            logging.info("Pixel f1 threshold {%s}", self.pixel_metrics.F1Score.threshold)

        self._collect_outputs(self.image_metrics, self.pixel_metrics, outputs)
        self._log_metrics("validation")
        self.validation_outputs.clear()

    def on_test_epoch_end(self) -> None:
        """Compute and save anomaly scores of the test set."""
        outputs = self.test_outputs
        if hasattr(self.image_metrics, "F1Score"):
            dice_score = 0
            counter = 0

            for output in outputs:
                for anomaly_score, gt_label in zip(output["pred_scores"], output["label"]):
                    pred_label = int(anomaly_score >= self.image_metrics.F1Score.threshold)
                    if gt_label == 0 and pred_label == 1:
                        self.false_bad += 1
                    elif gt_label == 1 and pred_label == 0:
                        self.false_good += 1

                if "mask" in output.keys():
                    for anomaly_map, mask in zip(output["anomaly_maps"], output["mask"]):
                        dice_score += 1 - dice(anomaly_map >= self.pixel_metrics.F1Score.threshold, mask)
                        counter += 1

            if counter > 0:
                self.log("Dice_score", dice_score / counter)
            self.log("False_good", self.false_good)
            self.log("False_bad", self.false_bad)

        self._collect_outputs(self.image_metrics, self.pixel_metrics, outputs)
        self._log_metrics("test")

    def _compute_adaptive_threshold(self, outputs: Any) -> None:
        self.image_threshold.reset()
        self.pixel_threshold.reset()
        self._collect_outputs(self.image_threshold, self.pixel_threshold, outputs)
        self.image_threshold.compute()
        if "mask" in outputs[0].keys() and "anomaly_maps" in outputs[0].keys():
            self.pixel_threshold.compute()
        else:
            self.pixel_threshold.value = self.image_threshold.value

        self.image_metrics.set_threshold(self.image_threshold.value.item())
        self.pixel_metrics.set_threshold(self.pixel_threshold.value.item())

    @staticmethod
    def _collect_outputs(
        image_metric: AnomalibMetricCollection,
        pixel_metric: AnomalibMetricCollection,
        outputs: Any,
    ) -> None:
        for output in outputs:
            image_metric.cpu()
            image_metric.update(output["pred_scores"], output["label"].int())
            if "mask" in output.keys() and "anomaly_maps" in output.keys():
                pixel_metric.cpu()
                pixel_metric.update(torch.squeeze(output["anomaly_maps"]), torch.squeeze(output["mask"].int()))

    @staticmethod
    def _post_process(outputs: STEP_OUTPUT) -> None:
        """Compute labels based on model predictions."""
        if isinstance(outputs, dict):
            if "pred_scores" not in outputs and "anomaly_maps" in outputs:
                # infer image scores from anomaly maps
                outputs["pred_scores"] = (
                    outputs["anomaly_maps"].reshape(outputs["anomaly_maps"].shape[0], -1).max(dim=1).values
                )
            elif "pred_scores" not in outputs and "box_scores" in outputs:
                # infer image score from bbox confidence scores
                outputs["pred_scores"] = torch.zeros_like(outputs["label"]).float()
                for idx, (boxes, scores) in enumerate(zip(outputs["pred_boxes"], outputs["box_scores"])):
                    if boxes.numel():
                        outputs["pred_scores"][idx] = scores.max().item()

            if "pred_boxes" in outputs and "anomaly_maps" not in outputs:
                # create anomaly maps from bbox predictions for thresholding and evaluation
                image_size: tuple[int, int] = outputs["image"].shape[-2:]
                true_boxes: list[Tensor] = outputs["boxes"]
                pred_boxes: Tensor = outputs["pred_boxes"]
                box_scores: Tensor = outputs["box_scores"]
                outputs["anomaly_maps"] = boxes_to_anomaly_maps(pred_boxes, box_scores, image_size)
                outputs["mask"] = boxes_to_masks(true_boxes, image_size)

    def _log_metrics(self, phase: str):
        if hasattr(self.image_metrics, "F1Score"):
            self.log(f"{phase}_image_F1", self.image_metrics.F1Score.compute().item())

        if hasattr(self.image_metrics, "AUROC"):
            self.log(f"{phase}_image_AUROC", self.image_metrics.AUROC.compute().item())

        if self.hparams.dataset.task == "segmentation":
            if hasattr(self.pixel_metrics, "F1Score"):
                self.log(f"{phase}_pixel_F1", self.pixel_metrics.F1Score.compute().item())
            if hasattr(self.pixel_metrics, "AUROC"):
                self.log(f"{phase}_pixel_AUROC", self.pixel_metrics.AUROC.compute().item())

        self.pixel_metrics.reset()
        self.image_metrics.reset()

    def _outputs_to_cpu(self, output):
        if isinstance(output, dict):
            for key, value in output.items():
                output[key] = self._outputs_to_cpu(value)
        elif isinstance(output, list):
            output = [self._outputs_to_cpu(item) for item in output]
        elif isinstance(output, Tensor):
            output = output.cpu()
        return output

    # TODO: Check if this is necessary
    # def _log_metrics(self) -> None:
    #     """Log computed performance metrics."""
    #     if self.pixel_metrics.update_called:
    #         self.log_dict(self.pixel_metrics, prog_bar=True)
    #         self.log_dict(self.image_metrics, prog_bar=False)
    #     else:
    #         self.log_dict(self.image_metrics, prog_bar=True)

    def _load_normalization_class(self, state_dict: OrderedDict[str, Tensor]) -> None:
        """Assigns the normalization method to use."""
        if "normalization_metrics.max" in state_dict.keys():
            self.normalization_metrics = MinMax()
        elif "normalization_metrics.image_mean" in state_dict.keys():
            self.normalization_metrics = AnomalyScoreDistribution()
        else:
            warn("No known normalization found in model weights.")

    def load_state_dict(self, state_dict: OrderedDict[str, Tensor], strict: bool = True):
        """Load state dict from checkpoint.

        Ensures that normalization and thresholding attributes is properly setup before model is loaded.
        """
        # Used to load missing normalization and threshold parameters
        self._load_normalization_class(state_dict)
        return super().load_state_dict(state_dict, strict=strict)
