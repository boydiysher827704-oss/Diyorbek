# Dataset Access

This project uses the Roboflow Universe dataset "Railway Track Fault
Detection" (version 1), owned by workspace `diyorbek-boyxurozov`.

- Public dataset page:
  https://universe.roboflow.com/diyorbek-boyxurozov/railway-track-fault-detection-hrem8

## How to Download the Exact Version Used

### Option A — Roboflow Python package (recommended, matches training code)

```python
pip install roboflow

from roboflow import Roboflow

rf = Roboflow(api_key="YOUR_API_KEY")
project = rf.workspace("diyorbek-boyxurozov").project("railway-track-fault-detection-hrem8")
dataset = project.version(1).download("yolov8")
```

Get your own free API key at https://app.roboflow.com/settings/api
(Account -> Roboflow Keys). Do not commit API keys to Git; the training
script reads it via input prompt (see src/train.py).

### Option B — Manual download

1. Go to the dataset page linked above.
2. Click "Export Dataset".
3. Choose format: YOLOv8.
4. Choose "download zip to computer".
5. Extract the zip - it produces `train/`, `valid/`, `test/` folders and
   a `data.yaml` file, matching the structure expected by
   src/train.py and src/predict.py.

## Dataset Summary

| Split | Images |
|-------|--------|
| train | 783    |
| valid | 223    |
| test  | 112    |
| Total | 1118   |

Classes: `defective`, `non-defective`
License: CC BY 4.0

Full exploratory analysis (class balance, image sizes, annotation
quality) is documented in EDA_NOTES.md.
