# Issue Log

Format: Observation -> Risk -> Decision -> Evidence -> Status

This log summarizes the data quality findings from EDA_NOTES.md in the
Data Gate's required format.

---

## Issue 1: Class Imbalance

- **Observation:** `defective` boxes outnumber `non-defective` boxes
  roughly 2.5-3x across train/valid/test (e.g. train: 555 vs 217).
- **Risk:** Model may become biased toward predicting `defective`,
  reducing precision on `non-defective` and/or under-recognizing it.
- **Decision:** Accept the imbalance for the MVP. It is consistent across
  splits (not a split artifact), and the direction of bias (over-flagging
  defects) is the safer failure mode for this safety use case.
- **Evidence:** EDA_NOTES.md, "Class Balance" section. Confirmed at
  final test evaluation: non-defective precision was lowest metric
  (0.489), consistent with this prediction.
- **Status:** Documented and accepted for MVP. Flagged as a priority
  improvement area for future iterations (see final_evaluation.md).

---

## Issue 2: Loosely-Drawn Bounding Boxes

- **Observation:** Visual inspection of sample images showed several
  `defective` boxes covering large rail sections rather than tightly
  framing the specific defect.
- **Risk:** Reduces localization precision (mAP50-95 lower than mAP50);
  model may learn coarse "region contains a defect" rather than precise
  defect boundaries.
- **Decision:** Accept for MVP classification-style use case (defect
  present vs not) since exact localization is not yet in scope (see
  PROBLEM_STATEMENT.md — precise localization is v2/YOLO detection
  scope). Documented as a factor behind the mAP50 vs mAP50-95 gap.
- **Evidence:** EDA_NOTES.md, "Visual Inspection" section;
  final_evaluation.md notes mAP50=0.651 vs mAP50-95=0.383 on test.
- **Status:** Documented, no action taken this iteration.

---

## Issue 3: Empty Labels on Large/Original-Resolution Images

- **Observation:** 27/783 (3.4%) train labels are empty; of the 30
  large/original-resolution images, 14 (46.7%) have empty labels — a
  much higher rate than the dataset average.
- **Risk:** Could indicate incomplete annotation (mislabeled as
  background) rather than genuine "no defect" images, which would
  corrupt training if used as negative examples.
- **Decision:** Manually reviewed all 14 images. All show legible,
  legitimate rail scenes with no obvious defect — consistent with
  genuine background examples. Kept in the dataset, no exclusion.
- **Evidence:** EDA_NOTES.md, "Follow-up: Manual Review" section
  (includes list of inspected filenames).
- **Status:** Resolved — confirmed valid, no further action needed.

---

## Issue 4: Unrelated/Noisy Sample Images

- **Observation:** A small number of sample images (filenames prefixed
  `RF--`) appeared unrelated to rail tracks (e.g. a ruler/tool close-up)
  during the initial random-sample visual review.
- **Risk:** Mislabeled or irrelevant training examples could add noise
  and reduce model quality.
- **Decision:** Not excluded for the MVP due to time constraints; the
  volume of such images was not systematically counted beyond the
  random sample. Flagged as a known limitation.
- **Evidence:** EDA_NOTES.md, "Visual Inspection" section.
- **Status:** Open — recommended as a future cleanup task (see
  final_evaluation.md "Next Steps").

---

## Issue 5: No Near-Duplicate / Leakage Detection

- **Observation:** No systematic check was run to detect near-duplicate
  images (e.g. consecutive camera frames) split across train/valid/test.
- **Risk:** If present, could inflate validation/test metrics by letting
  the model see near-copies of test images during training.
- **Decision:** Not run for this MVP stage due to time constraints.
  Partial mitigation: filenames show varied prefixes (B--, C--, RF--, i),
  suggesting images came from multiple sources rather than one
  continuous video feed, which lowers (but doesn't eliminate) this risk.
- **Evidence:** EDA_NOTES.md, "Data Leakage Check" section.
- **Status:** Open — documented as a limitation; recommended as a
  follow-up check if metrics are used for decisions beyond this MVP.

---

## Issue 6: No Reusable Preprocessing Script (Data Gate requirement)

- **Observation:** Preprocessing (resize/format) was handled entirely by
  Roboflow's export pipeline (see data.yaml, images already resized to
  640x640 during YOLO training via `imgsz`). No custom preprocessing
  script exists in `src/`.
- **Risk:** Reduced reproducibility if the raw data source or export
  settings change; no single script documents the exact preprocessing
  applied.
- **Decision:** Documented the pipeline (Roboflow export -> YOLO
  training with imgsz=640) as the de facto preprocessing flow. A minimal
  reusable inference script was added instead (`src/predict.py`) to
  cover the "reusable, reloadable" requirement for the trained model.
- **Evidence:** data.yaml, experiments/baseline_v1.md configuration
  table, src/predict.py.
- **Status:** Partially addressed — inference reproducibility covered;
  a dedicated data-preprocessing script remains a future improvement.
