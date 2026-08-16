# Railway Track Defect Detection

An object detection model (YOLOv8) that automatically detects defects
(cracks, corrosion, spalling, etc.) on railway tracks from images —
built as an AI/ML Fundamentals Capstone project.

## Status

✅ **Core work complete**: dataset audited, baseline model trained,
compared against a second experiment, evaluated on a held-out test set,
and a confirmed limitation (data leakage) has been disclosed
transparently. See [PROJECT_STATUS.md](./PROJECT_STATUS.md) for the
current, detailed status.

## Live Showcase

An interactive project showcase page ([`index.html`](./index.html)) is
included in this repo — it presents the project, sample detections, and
model results visually.

- **View locally:** open `index.html` in any browser
- **View online:** once GitHub Pages is enabled for this repo, it will be
  available at `https://boydiysher827704-oss.github.io/Diyorbek/`

## Quick Start

```bash
git clone https://github.com/boydiysher827704-oss/Diyorbek.git
cd Diyorbek
pip install -r requirements.txt
```

**Run inference on an image** (uses the trained weights already in
this repo — no training needed):

```bash
python src/predict.py path/to/rail_image.jpg
```

**Reproduce training from scratch** (downloads the dataset and trains
a new model — see [DATASET.md](./DATASET.md) for how to get an API key):

```bash
python src/train.py
```

## Project Documents

| Document | What it covers |
|---|---|
| [PROBLEM_STATEMENT.md](./PROBLEM_STATEMENT.md) | Problem, task type (object detection), MVP scope, success metric |
| [DATASET.md](./DATASET.md) | Exact dataset version and how to download it |
| [EDA_NOTES.md](./EDA_NOTES.md) | Full exploratory data analysis: class balance, image sizes, annotation quality, confirmed data leakage check |
| [ISSUE_LOG.md](./ISSUE_LOG.md) | All data/model issues found, in Observation → Risk → Decision → Evidence → Status format |
| [experiments/baseline_v1.md](./experiments/baseline_v1.md) | Baseline model (YOLOv8n, 30 epochs) configuration and results |
| [experiments/experiment2_50epoch.md](./experiments/experiment2_50epoch.md) | Comparison experiment (50 epochs) and model selection decision |
| [experiments/final_evaluation.md](./experiments/final_evaluation.md) | One-time test-set evaluation, error analysis, and leakage caveat |
| [PROJECT_STATUS.md](./PROJECT_STATUS.md) | Current status, what's done, what's next |

## Results Summary

Final model: **YOLOv8n**, 30 epochs, trained on the Roboflow
"Railway Track Fault Detection" dataset (1,118 images).

| Metric (test set) | Value |
|---|---|
| Precision | 0.590 |
| Recall | 0.786 |
| mAP50 | 0.651 |
| mAP50-95 | 0.383 |

Recall was prioritized over precision because missing a real defect
(false negative) is more costly than a false alarm in this safety
context — see PROBLEM_STATEMENT.md for the reasoning.

**Known limitation:** a confirmed near-duplicate check found ~12.5% of
test images have a near-identical match in the training set, so the
metrics above are likely somewhat optimistic. This is disclosed in full
in EDA_NOTES.md and ISSUE_LOG.md rather than hidden.

## Project Structure

```
PROBLEM_STATEMENT.md   problem definition, task type, scope
DATASET.md             exact dataset version + download instructions
EDA_NOTES.md           full exploratory data analysis
ISSUE_LOG.md           formal log of data/model issues found
PROJECT_STATUS.md      current project status
requirements.txt       Python dependencies

data/
  raw/                 original, unmodified dataset (not committed — see DATASET.md)
  processed/           cleaned/split data, ready for training

notebooks/             Colab/Jupyter notebooks (EDA, experiments, demo)

src/
  train.py             end-to-end reproducible training script
  predict.py            reusable inference script (loads models/best.pt)

models/
  best.pt              trained model weights, committed directly
  README.md            how to reload and use the model

experiments/
  baseline_v1.md               first trained model, results
  experiment2_50epoch.md       comparison experiment, model selection
  final_evaluation.md          one-time test-set evaluation, error analysis
```

## Tools Used

- **Dataset:** [Roboflow](https://roboflow.com) — "Railway Track Fault
  Detection" (CC BY 4.0)
- **Model:** [Ultralytics YOLOv8](https://github.com/ultralytics/ultralytics)
  (transfer learning from COCO-pretrained weights)
- **Training environment:** Google Colab (Tesla T4 GPU)
- **Version control:** Git / GitHub

## Author

Diyorbek — AI/ML Fundamentals, Capstone Project (Module 8)
