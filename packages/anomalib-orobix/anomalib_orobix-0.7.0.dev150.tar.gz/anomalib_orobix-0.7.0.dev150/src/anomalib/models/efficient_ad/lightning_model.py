"""EfficientAd: Accurate Visual Anomaly Detection at Millisecond-Level Latencies.
https://arxiv.org/pdf/2303.14535.pdf
"""

# Copyright (C) 2023 Intel Corporation
# SPDX-License-Identifier: Apache-2.0

from __future__ import annotations

import logging
from pathlib import Path

import itertools
from typing import Literal, Tuple
import albumentations as A
import numpy as np
import torch
import tqdm
from albumentations.pytorch import ToTensorV2
from omegaconf import DictConfig, ListConfig
from pytorch_lightning.utilities.types import STEP_OUTPUT
from torch import Tensor, optim
from torch.utils.data import DataLoader
from torchvision.datasets import ImageFolder

from anomalib.data.utils import DownloadInfo, download_and_extract, download_single_file
from anomalib.models.components import AnomalyModule

from .torch_model import EfficientAdModel, EfficientAdModelSize, reduce_tensor_elems

logger = logging.getLogger(__name__)

IMAGENETTE_DOWNLOAD_INFO = DownloadInfo(
    name="imagenette2.tgz",
    url="https://s3.amazonaws.com/fast-ai-imageclas/imagenette2.tgz",
    hash="fe2fc210e6bb7c5664d602c3cd71e612",
)

WEIGHTS_DOWNLOAD_INFO = DownloadInfo(
    name="efficientad_pretrained_weights.zip",
    url="https://github.com/openvinotoolkit/anomalib/releases/download/efficientad_pretrained_weights/efficientad_pretrained_weights.zip",
    hash="ec6113d728969cd233271eeed7d692f2",
)

NELSON_TEACHER_S = DownloadInfo(
    name="teacher_small.pth",
    url="https://raw.githubusercontent.com/nelson1425/EfficientAD/main/models/teacher_small.pth",
    hash="31c3904bbb722addb96c45c0a469853f",
)

NELSON_TEACHER_M = DownloadInfo(
    name="teacher_medium.pth",
    url="https://raw.githubusercontent.com/nelson1425/EfficientAD/main/models/teacher_medium.pth",
    hash="c3e413767011824b76cf23ae76ea329f",
)


class TransformsWrapper:
    def __init__(self, t: A.Compose):
        self.transforms = t

    def __call__(self, img, *args, **kwargs):
        return self.transforms(image=np.array(img))


class EfficientAd(AnomalyModule):
    """PL Lightning Module for the EfficientAd algorithm.

    Args:
        pretrained_models_dir (str): directory containing pre-trained teacher file
        imagenette_dir(str): directory containing imagenette dataset
        teacher_file_name (str): path to the pre-trained teacher model
        teacher_out_channels (int): number of convolution output channels
        input_size (tuple): size of input images
        model_size (str): size of student and teacher model
        lr (float): learning rate
        weight_decay (float): optimizer weight decay
        padding (bool): use padding in convoluional layers
        pad_maps (bool): relevant if padding is set to False. In this case, pad_maps = True pads the
            output anomaly maps so that their size matches the size in the padding = True case.
        batch_size (int): batch size for imagenet dataloader
        pre_padding (bool): If True, apply prepadding to inputs inside forward function.
        pretrained_teacher_type (str): Type of pretrained model. Currently nelson and anomalib are supported.
    """

    def __init__(
        self,
        imagenette_dir: str,
        teacher_out_channels: int,
        input_size: Tuple[int, int],
        pretrained_models_dir: str = "./efficient_ad_pretrained_models",
        model_size: EfficientAdModelSize = EfficientAdModelSize.S,
        lr: float = 0.0001,
        weight_decay: float = 0.00001,
        padding: bool = False,
        pad_maps: bool = True,
        batch_size: int = 1,
        pre_padding: bool = False,
        pretrained_teacher_type: Literal["nelson", "anomalib"] = "nelson",
    ) -> None:
        super().__init__()

        self.model_size = model_size
        self.pre_padding = pre_padding
        self.input_size = input_size
        self.model: EfficientAdModel = EfficientAdModel(
            teacher_out_channels=teacher_out_channels,
            input_size=input_size,
            model_size=model_size,
            padding=padding,
            pad_maps=pad_maps,
            pre_padding=self.pre_padding,
            pretrained_teacher_type=pretrained_teacher_type,
        )
        self.batch_size = batch_size
        self.lr = lr
        self.weight_decay = weight_decay
        self.pretrained_models_dir = Path(pretrained_models_dir)
        self.imagenette_dir = Path(imagenette_dir)

        self.prepare_pretrained_model()
        self.prepare_imagenette_data()

    def prepare_pretrained_model(self) -> None:
        if self.model.pretrained_teacher_type == "nelson":
            if self.model.model_size == EfficientAdModelSize.S:
                model_type = NELSON_TEACHER_S
            else:
                model_type = NELSON_TEACHER_M
            teacher_path = self.pretrained_models_dir / model_type.name
            # Attempt to download if file does not exist
            download_single_file(self.pretrained_models_dir, model_type)
        else:
            download_and_extract(self.pretrained_models_dir, WEIGHTS_DOWNLOAD_INFO)
            # Why is it nelson also here?
            teacher_path = (
                self.pretrained_models_dir / "efficientad_pretrained_weights" / f"nelson_teacher_{self.model_size}.pth"
            )

        logger.info(f"Load pretrained teacher model from {teacher_path}")
        self.model.teacher.load_state_dict(torch.load(teacher_path, map_location=torch.device(self.device)))

    def prepare_imagenette_data(self) -> None:
        self.data_transforms_imagenet = A.Compose(
            [  # We obtain an image P ∈ R 3×256×256 from ImageNet by choosing a random image,
                A.Resize(self.input_size[0] * 2, self.input_size[1] * 2),  # resizing it to 512 × 512,
                A.ToGray(p=0.3),  # converting it to gray scale with a probability of 0.3
                A.CenterCrop(self.input_size[0], self.input_size[1]),  # and cropping the center 256 × 256 pixels
                # TODO: Anomalib version expects only a ToFloat. The Imagenet normalization is performed inside the forward
                # A.ToFloat(always_apply=False, p=1.0, max_value=255),
                A.Normalize(mean=[0.485, 0.456, 0.406], std=[0.229, 0.224, 0.225]),
                ToTensorV2(),
            ]
        )

        if not self.imagenette_dir.is_dir():
            download_and_extract(self.imagenette_dir, IMAGENETTE_DOWNLOAD_INFO)

        imagenet_dataset = ImageFolder(
            self.imagenette_dir, transform=TransformsWrapper(t=self.data_transforms_imagenet)
        )

        self.imagenet_loader = DataLoader(imagenet_dataset, batch_size=self.batch_size, shuffle=True, pin_memory=True)
        self.imagenet_iterator = iter(self.imagenet_loader)

    @torch.no_grad()
    def teacher_channel_mean_std(self, dataloader: DataLoader) -> dict[str, Tensor]:
        """Calculate the mean and std of the teacher models activations.

        Args:
            dataloader (DataLoader): Dataloader of the respective dataset.

        Returns:
            dict[str, Tensor]: Dictionary of channel-wise mean and std
        """
        y_means = []
        means_distance = []

        logger.info("Calculate teacher channel mean and std")
        for batch in tqdm.tqdm(dataloader, desc="Calculate teacher channel mean", position=0, leave=True):
            if self.pre_padding:
                if self.model.pre_padding_values is None:
                    raise ValueError("Pre-padding should not be None here, given that pre_padding has been set to True")
                batch["image"] = torch.nn.functional.pad(batch["image"], self.model.pre_padding_values)
            y = self.model.teacher(batch["image"].to(self.device))
            y_means.append(torch.mean(y, dim=[0, 2, 3]))

        channel_mean = torch.mean(torch.stack(y_means), dim=0)[None, :, None, None]

        for batch in tqdm.tqdm(dataloader, desc="Calculate teacher channel std", position=0, leave=True):
            y = self.model.teacher(batch["image"].to(self.device))
            distance = (y - channel_mean) ** 2
            means_distance.append(torch.mean(distance, dim=[0, 2, 3]))

        channel_var = torch.mean(torch.stack(means_distance), dim=0)[None, :, None, None]
        channel_std = torch.sqrt(channel_var)
        return {"mean": channel_mean, "std": channel_std}

    @torch.no_grad()
    def map_norm_quantiles(self, dataloader: DataLoader) -> dict[str, Tensor]:
        """Calculate 90% and 99.5% quantiles of the student(st) and autoencoder(ae).

        Args:
            dataloader (DataLoader): Dataloader of the respective dataset.

        Returns:
            dict[str, Tensor]: Dictionary of both the 90% and 99.5% quantiles
            of both the student and autoencoder feature maps.
        """
        maps_st = []
        maps_ae = []
        logger.info("Calculate Validation Dataset Quantiles")
        for batch in tqdm.tqdm(dataloader, desc="Calculate Validation Dataset Quantiles", position=0, leave=True):
            for img, label in zip(batch["image"], batch["label"]):
                if label == 0:  # only use good images of validation set!
                    if self.pre_padding:
                        if self.model.pre_padding_values is None:
                            raise ValueError(
                                "Pre-padding should not be None here, given that pre_padding has been set to True"
                            )
                        img = torch.nn.functional.pad(img, self.model.pre_padding_values)
                    output = self.model(img.to(self.device))
                    map_st = output[2]
                    map_ae = output[3]
                    maps_st.append(map_st)
                    maps_ae.append(map_ae)
        qa_st, qb_st = self._get_quantiles_of_maps(maps_st)
        qa_ae, qb_ae = self._get_quantiles_of_maps(maps_ae)

        return {"qa_st": qa_st, "qa_ae": qa_ae, "qb_st": qb_st, "qb_ae": qb_ae}

    def _get_quantiles_of_maps(self, maps: list[Tensor]) -> Tuple[Tensor, Tensor]:
        """Calculate 90% and 99.5% quantiles of the given anomaly maps.

        If the total number of elements in the given maps is larger than 16777216
        the returned quantiles are computed on a random subset of the given
        elements.

        Args:
            maps (list[Tensor]): List of anomaly maps.

        Returns:
            tuple[Tensor, Tensor]: Two scalars - the 90% and the 99.5% quantile.
        """

        maps_flat = reduce_tensor_elems(torch.cat(maps))
        qa = torch.quantile(maps_flat, q=0.9).to(self.device)
        qb = torch.quantile(maps_flat, q=0.995).to(self.device)
        return qa, qb

    def configure_optimizers(self) -> optim.Optimizer:
        optimizer = optim.Adam(
            list(self.model.student.parameters()) + list(self.model.ae.parameters()),
            lr=self.lr,
            weight_decay=self.weight_decay,
        )
        num_steps = min(
            self.trainer.max_steps, self.trainer.max_epochs * len(self.trainer.datamodule.train_dataloader())
        )
        scheduler = optim.lr_scheduler.StepLR(optimizer, step_size=int(0.95 * num_steps), gamma=0.1)

        return {"optimizer": optimizer, "lr_scheduler": scheduler}

    def on_train_start(self) -> None:
        """Calculate or load the channel-wise mean and std of the training dataset and push to the model."""
        if not self.model.is_set(self.model.mean_std):
            channel_mean_std = self.teacher_channel_mean_std(self.trainer.datamodule.train_dataloader())
            self.model.mean_std.update(channel_mean_std)

    def training_step(self, batch: dict[str, str | Tensor], *args, **kwargs) -> dict[str, Tensor]:
        """Training step for EfficientAd returns the student, autoencoder and combined loss.

        Args:
            batch (batch: dict[str, str | Tensor]): Batch containing image filename, image, label and mask

        Returns:
          Loss.
        """
        del args, kwargs  # These variables are not used.

        try:
            # infinite dataloader; [0] getting the image not the label
            batch_imagenet = next(self.imagenet_iterator)[0]["image"].to(self.device)
        except StopIteration:
            self.imagenet_iterator = iter(self.imagenet_loader)
            batch_imagenet = next(self.imagenet_iterator)[0]["image"].to(self.device)

        loss_st, loss_ae, loss_stae = self.model(batch=batch["image"], batch_imagenet=batch_imagenet)

        loss = loss_st + loss_ae + loss_stae
        self.log("train_st", loss_st.item(), on_epoch=True, prog_bar=True, logger=True)
        self.log("train_ae", loss_ae.item(), on_epoch=True, prog_bar=True, logger=True)
        self.log("train_stae", loss_stae.item(), on_epoch=True, prog_bar=True, logger=True)
        self.log("train_loss", loss.item(), on_epoch=True, prog_bar=True, logger=True)
        return {"loss": loss}

    def on_validation_start(self) -> None:
        """
        Calculate the feature map quantiles of the validation dataset and push to the model.
        """
        if (self.current_epoch > self.trainer.max_epochs) or (self.global_step > self.trainer.max_steps):
            # TODO: Anomalib uses validation which is heavily biased as it generally performed over test images since
            # val is not available most of the times.
            map_norm_quantiles = self.map_norm_quantiles(self.trainer.datamodule.train_dataloader())
            self.model.quantiles.update(map_norm_quantiles)

    def validation_step(self, batch: dict[str, str | Tensor], *args, **kwargs) -> STEP_OUTPUT:
        """Validation Step of EfficientAd returns anomaly maps for the input image batch

        Args:
          batch (dict[str, str | Tensor]): Input batch

        Returns:
          Dictionary containing anomaly maps.
        """
        del args, kwargs  # These variables are not used.

        batch["anomaly_maps"], _, _, _ = self.model(batch["image"])

        return batch


class EfficientAdLightning(EfficientAd):
    """PL Lightning Module for the EfficientAd Algorithm.

    Args:
        hparams (DictConfig | ListConfig): Model params
    """

    def __init__(self, hparams: DictConfig | ListConfig) -> None:
        super().__init__(
            teacher_out_channels=hparams.model.teacher_out_channels,
            model_size=hparams.model.model_size,
            lr=hparams.model.lr,
            weight_decay=hparams.model.weight_decay,
            padding=hparams.model.padding,
            input_size=hparams.model.input_size,
            batch_size=hparams.model.train_batch_size,
            pretrained_models_dir=hparams.model.pretrained_models_dir,
            imagenette_dir=hparams.model.imagenette_dir,
            pad_maps=hparams.model.pad_maps,
            pre_padding=hparams.model.pre_padding,
            pretrained_teacher_type=hparams.model.pretrained_teacher_type,
        )
        self.hparams: DictConfig | ListConfig  # type: ignore
        self.save_hyperparameters(hparams)
