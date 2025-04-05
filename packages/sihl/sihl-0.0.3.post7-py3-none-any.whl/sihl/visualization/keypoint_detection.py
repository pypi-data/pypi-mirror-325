from typing import List

from matplotlib import patches
from matplotlib import pyplot as plt
from torchvision.transforms.v2 import Resize
import numpy as np
import torch

from sihl.heads import KeypointDetection

from .common import get_images, plot_to_numpy, COLORS


def get_rectangle_patch(box, color):
    xy, width, height = (box[0], box[1]), box[2] - box[0], box[3] - box[1]
    return patches.Rectangle(
        xy, width, height, linewidth=1, edgecolor=color, facecolor="none"
    )


@get_images.register(KeypointDetection)
def _(head, config, input, target, features) -> List[np.ndarray]:
    keypoint_labels = config["keypoints"] if "keypoints" in config else []
    keypoint_links = config["links"] if "links" in config else []

    num_instances, scores, _, logits = head.forward_logits(features)
    batch_size, _, height, width = logits.shape
    heatmaps = logits.reshape(
        (batch_size, head.max_instances, head.num_kpts, height, width)
    )
    heatmaps = heatmaps.flatten(3, 4).softmax(dim=3).reshape(heatmaps.shape)
    keypoint_scores = heatmaps.flatten(3, 4).max(dim=3)[0]
    pred_keypoints = head.heatmap_to_keypoints(features, heatmaps)
    scores, reg_features = head.get_features(features)
    scores = scores.max(dim=2)[0]

    images = (input.permute(0, 2, 3, 1) * 255).to(torch.uint8).to("cpu").numpy()
    visualizations = []
    for batch_idx, image in enumerate(images):
        fig, axes = plt.subplots(1, 3, figsize=(10.24, 5.12), dpi=100)
        for ax in axes:
            ax.set_xticks([])
            ax.set_yticks([])
        axes[0].title.set_text("Input")
        axes[0].axis("off")
        axes[0].imshow(image)

        axes[1].title.set_text("Target")
        axes[1].imshow(image, alpha=0.2)
        if target is not None:
            for instance_idx in range(target["presence"][batch_idx].shape[0]):
                presence = target["presence"][batch_idx][instance_idx].to("cpu")
                keypoints = target["keypoints"][batch_idx][instance_idx].to("cpu")
                if keypoints.numel() > 0:
                    color = np.array(COLORS[instance_idx % len(COLORS)]) / 255
                    idxs = [idx for idx, pres in enumerate(presence) if pres is True]
                    xs = [keypoints[idx][0] + 0.5 for idx in idxs]
                    ys = [keypoints[idx][1] + 0.5 for idx in idxs]
                    axes[1].scatter(xs, ys, marker="o", s=3, color=color)
                    for link in keypoint_links:
                        try:
                            i = keypoint_labels.index(link[0])
                            j = keypoint_labels.index(link[1])
                        except ValueError:
                            continue
                        if presence[i] and presence[j]:
                            xs = [keypoints[i][0], keypoints[j][0]]
                            ys = [keypoints[i][1], keypoints[j][1]]
                            axes[1].plot(xs, ys, lw=2, c=color)

        axes[2].title.set_text("Prediction")
        total_hm = heatmaps[batch_idx, : target["presence"][batch_idx].shape[0]]
        total_hm = total_hm.sum(dim=(0, 1)).unsqueeze(0)
        resize = Resize(image.shape[:2], interpolation=0)
        axes[2].imshow(resize(total_hm).squeeze(0).to("cpu"))
        if pred_keypoints is not None:
            for instance_idx in range(target["presence"][batch_idx].shape[0]):
                presence = keypoint_scores[batch_idx, instance_idx].to("cpu") > 0.1
                keypoints = pred_keypoints[batch_idx, instance_idx].to("cpu")
                if keypoints.numel() > 0:
                    idxs = [idx for idx, pres in enumerate(presence) if pres is True]
                    xs = [keypoints[idx][0] + 0.5 for idx in idxs]
                    ys = [keypoints[idx][1] + 0.5 for idx in idxs]
                    axes[2].scatter(xs, ys, marker="o", s=3, color=color)
                    color = np.array(COLORS[instance_idx % len(COLORS)]) / 255
                    for link in keypoint_links:
                        try:
                            i = keypoint_labels.index(link[0])
                            j = keypoint_labels.index(link[1])
                        except ValueError:
                            continue
                        if presence[i] and presence[j]:
                            xs = [keypoints[i][0], keypoints[j][0]]
                            ys = [keypoints[i][1], keypoints[j][1]]
                            axes[1].plot(xs, ys, lw=2, c=color)

        fig.tight_layout()
        visualizations.append(plot_to_numpy(fig))
        plt.close()
    return visualizations
