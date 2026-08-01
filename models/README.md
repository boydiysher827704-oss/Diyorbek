# models

Trained model weight files go here.

## Final Model (baseline_v1)

The trained weights are committed directly in this repository:
models/best.pt (YOLOv8n, trained 30 epochs on the Roboflow "Railway
Track Fault Detection" dataset, version 1).

No download or retraining is needed to use it - it is already here.

To reproduce training from scratch instead, see src/train.py and
DATASET.md.

Results: see experiments/final_evaluation.md for full metrics.

## How to Reload and Use

pip install ultralytics

from ultralytics import YOLO
model = YOLO("models/best.pt")
results = model("path/to/rail_image.jpg")
results[0].show()

This loads the trained weights directly - no retraining needed.
