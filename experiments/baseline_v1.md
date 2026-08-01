# Experiment: baseline_v1

## Goal
Establish a "zero point" performance reference using the smallest,
fastest YOLO model with default settings, before any tuning.

## Configuration

| Parameter | Value |
|---|---|
| Model | YOLOv8n (nano, pretrained on COCO) |
| Epochs | 30 |
| Image size | 640x640 |
| Batch size | 16 |
| Optimizer | AdamW (auto-selected) |
| Hardware | Google Colab, Tesla T4 GPU |
| Training time | ~8.3 minutes (0.139 hours) |
| Data | Roboflow "Railway Track Fault Detection" v1, default split |

## Results (validation set, 223 images, 219 instances)

| Class | Precision | Recall | mAP50 | mAP50-95 |
|---|---|---|---|---|
| defective | 0.699 | 0.699 | 0.710 | 0.418 |
| non-defective | 0.668 | 0.661 | 0.646 | 0.442 |
| **all (overall)** | **0.684** | **0.680** | **0.678** | **0.430** |

## Observations

- Training was stable: box/cls/dfl losses decreased steadily across
  epochs, with a mosaic-augmentation cutoff at epoch ~20 causing a
  temporary metric dip before recovering and continuing to improve.
- `mAP50` (0.678) is noticeably higher than `mAP50-95` (0.430), meaning
  the model is reasonably good at detecting *that* a defect is present
  but less precise about the *exact* box location. This is consistent
  with the EDA finding that many training boxes are loosely drawn
  around large rail sections rather than tightly framing the defect.
- Recall for `defective` (0.699) is the metric we care most about for
  safety reasons (missing a real defect is the costliest error). At
  ~70%, this baseline is usable as a reference but not yet strong enough
  on its own for a safety-critical deployment — improving recall is a
  priority for the next experiment.

## Artifacts

- Best weights: `runs/detect/baseline_v1-2/weights/best.pt` (Colab
  session; not committed to Git — see models/README.md)
- Training plots/logs: `runs/detect/baseline_v1-2/`

## Status
Complete. This is the reference point for comparing future experiments.
