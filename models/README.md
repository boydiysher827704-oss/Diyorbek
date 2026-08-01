# models

Trained model weight files go here (e.g., best.pt). Excluded from Git via
.gitignore since they are large binaries.

## Final Model (baseline_v1)

- File: best.pt (YOLOv8n, trained 30 epochs on the Roboflow
  "Railway Track Fault Detection" dataset)
- Produced in Colab at:
  /content/runs/detect/baseline_v1-2/weights/best.pt
- How to get it: download from the Colab session (Files panel ->
  right-click -> Download) and place it here as models/best.pt, or
  retrain using the steps in experiments/baseline_v1.md.
- Results: see experiments/final_evaluation.md for full metrics.

## How to Reload and Use

```python
from ultralytics import YOLO

model = YOLO("models/best.pt")
results = model("path/to/rail_image.jpg")
results[0].show()
```

This loads the trained weights directly - no retraining needed.
# Model Weights

## best.pt
- **File:** `best.pt` - trained YOLO model
- **Download:** [Link to Google Drive] (replace with your actual link)
- **Place:** Copy the file into this `models/` folder.
