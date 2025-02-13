"""Towards Total Recall in Industrial Anomaly Detection.

Paper https://arxiv.org/abs/2106.08265.
"""

# Copyright (C) 2022 Intel Corporation
# SPDX-License-Identifier: Apache-2.0

from __future__ import annotations

import logging

import torch
from torch import nn
from omegaconf import DictConfig, ListConfig
from pytorch_lightning.utilities.types import STEP_OUTPUT
from torch import Tensor

from anomalib.models.components import AnomalyModule
from anomalib.models.patchcore.torch_model import PatchcoreModel

logger = logging.getLogger(__name__)


class Patchcore(AnomalyModule):
    """PatchcoreLightning Module to train PatchCore algorithm.

    Args:
        input_size (tuple[int, int]): Size of the model input.
        backbone (str): Backbone CNN network
        layers (list[str]): Layers to extract features from the backbone CNN
        pre_trained (bool, optional): Boolean to check whether to use a pre_trained backbone.
        coreset_sampling_ratio (float, optional): Coreset sampling ratio to subsample embedding.
            Defaults to 0.1.
        num_neighbors (int, optional): Number of nearest neighbors. Defaults to 9.
        pretrained_weights (str, optional): Path to pretrained weights. Defaults to None.
        compress_memory_bank (bool): If true the memory bank features are projected to a lower dimensionality following
            the Johnson-Lindenstrauss lemma.
        coreset_sampler (str): Coreset sampler to use. Defaults to "anomalib".
        score_computation (str): Score computation to use. Defaults to "anomalib". If "amazon" is used, the anomaly
            score is correctly computed as from the paper but it may require more time to compute.
        disable_score_weighting: If true, the model will not apply the weight factor to the anomaly score. Only works if
            score_computation is set to anomalib.
        weight_anomaly_map: If true, the model will apply the weight factor to the whole anomaly map, this might be
            useful as the anomaly score is now the max of the anomaly map. Only enabled if disable_score_weighting is
            False. Only works if score_computation is set to anomalib.
        anomaly_score_from_max_heatmap: If true, the anomaly score will be the max of the anomaly map.
    """

    def __init__(
        self,
        input_size: tuple[int, int],
        backbone: str | nn.Module,
        layers: list[str],
        pre_trained: bool = True,
        coreset_sampling_ratio: float = 0.1,
        num_neighbors: int = 9,
        pretrained_weights: str | None = None,
        compress_memory_bank: bool = False,
        coreset_sampler: str = "anomalib",
        score_computation: str = "anomalib",
        disable_score_weighting: bool = False,
        weight_anomaly_map: bool = False,
        anomaly_score_from_max_heatmap: bool = False,
    ) -> None:
        super().__init__()

        self.model: PatchcoreModel = PatchcoreModel(
            input_size=input_size,
            backbone=backbone,
            pre_trained=pre_trained,
            layers=layers,
            num_neighbors=num_neighbors,
            pretrained_weights=pretrained_weights,
            compress_memory_bank=compress_memory_bank,
            score_computation=score_computation,
            disable_score_weighting=disable_score_weighting,
            weight_anomaly_map=weight_anomaly_map,
            anomaly_score_from_max_heatmap=anomaly_score_from_max_heatmap,
        )
        self.coreset_sampling_ratio = coreset_sampling_ratio
        self.embeddings: Tensor = torch.tensor([])
        self.automatic_optimization = False
        self.coreset_sampler = coreset_sampler
        self.counter = 0

    def configure_optimizers(self) -> None:
        """Configure optimizers.

        Returns:
            None: Do not set optimizers by returning None.
        """
        return None

    def on_train_epoch_start(self) -> None:
        self.embeddings = torch.tensor([])
        self.counter = 0
        return super().on_train_epoch_start()

    def training_step(self, batch: dict[str, str | Tensor], *args, **kwargs) -> None:
        """Generate feature embedding of the batch.

        Args:
            batch (dict[str, str | Tensor]): Batch containing image filename, image, label and mask

        Returns:
            dict[str, np.ndarray]: Embedding Vector
        """
        del args, kwargs  # These variables are not used.

        self.model.feature_extractor.eval()
        embedding = self.model(batch["image"])

        # NOTE: `self.embedding` appends each batch embedding to
        #   store the training set embedding. We manually append these
        #   values mainly due to the new order of hooks introduced after PL v1.4.0
        #   https://github.com/PyTorchLightning/pytorch-lightning/pull/7357

        if len(self.embeddings) == 0:
            if not self.trainer.sanity_checking:
                # Initialize the embeddings tensor with the estimated number of batches
                self.embeddings = torch.zeros(
                    (
                        (embedding.shape[0] // batch["image"].shape[0])
                        * len(self.trainer.train_dataloader.dataset)
                        * self.trainer.max_epochs,
                        *embedding.shape[1:],
                    ),
                    device=self.device,
                    dtype=embedding.dtype,
                )
            else:
                self.embeddings = self.embeddings.to(device=self.device, dtype=embedding.dtype)

        if not self.trainer.sanity_checking:
            self.embeddings[self.counter : self.counter + embedding.shape[0]] = embedding
        else:
            self.embeddings = torch.cat((self.embeddings, embedding))

        self.counter += embedding.shape[0]
        zero_loss = torch.tensor(0.0, requires_grad=True, device=self.device)
        return {"loss": zero_loss}

    def on_validation_start(self) -> None:
        """Apply subsampling to the embedding collected from the training set."""
        # NOTE: Previous anomalib versions fit subsampling at the end of the epoch.
        #   This is not possible anymore with PyTorch Lightning v1.4.0 since validation
        #   is run within train epoch.
        if len(self.embeddings) == 0:
            # This is a workaround to allow automatic batch computation using lightning
            train_dl = self.trainer.datamodule.train_dataloader()
            batch = next(iter(train_dl))

            batch = {k: v.to(self.device) for k, v in batch.items()}
            self.model.train()
            self.training_step(batch)
            self.model.eval()

        logger.info("Aggregating the embedding extracted from the training set.")

        logger.info("Applying core-set subsampling to get the embedding.")

        self.model.subsample_embedding(self.embeddings, self.coreset_sampling_ratio, mode=self.coreset_sampler)
        self.embeddings = torch.tensor([])

        if torch.cuda.is_available():
            torch.cuda.empty_cache()

    def validation_step(self, batch: dict[str, str | Tensor], *args, **kwargs) -> STEP_OUTPUT:
        """Get batch of anomaly maps from input image batch.

        Args:
            batch (dict[str, str | Tensor]): Batch containing image filename,
                image, label and mask

        Returns:
            dict[str, Any]: Image filenames, test images, GT and predicted label/masks
        """
        del args, kwargs  # These variables are not used.

        anomaly_maps, anomaly_score = self.model(batch["image"])
        batch["anomaly_maps"] = anomaly_maps
        batch["pred_scores"] = anomaly_score

        return batch


class PatchcoreLightning(Patchcore):
    """PatchcoreLightning Module to train PatchCore algorithm.

    Args:
        hparams (Union[DictConfig, ListConfig]): Model params
        backbone: optional, override hparams.model.backbone. Can be both a string or a nn.Module
    """

    def __init__(self, hparams: DictConfig | ListConfig, backbone: str | nn.Module | None = None):
        if backbone is None:
            backbone = hparams.model.backbone

        super().__init__(
            input_size=hparams.model.input_size,
            backbone=backbone,
            layers=hparams.model.layers,
            pre_trained=getattr(hparams.model, "pre_trained", True),
            coreset_sampling_ratio=hparams.model.coreset_sampling_ratio,
            num_neighbors=hparams.model.num_neighbors,
            pretrained_weights=getattr(hparams.model, "pretrained_weights", None),
            compress_memory_bank=getattr(hparams.model, "compress_memory_bank", False),
            coreset_sampler=getattr(hparams.model, "coreset_sampler", "anomalib"),
            score_computation=getattr(hparams.model, "score_computation", "anomalib"),
            disable_score_weighting=getattr(hparams.model, "disable_score_weighting", False),
            weight_anomaly_map=getattr(hparams.model, "weight_anomaly_map", False),
            anomaly_score_from_max_heatmap=getattr(hparams.model, "anomaly_score_from_max_heatmap", False),
        )
        self.hparams: DictConfig | ListConfig  # type: ignore
        self.save_hyperparameters(hparams)
