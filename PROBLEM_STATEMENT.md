# Problem Statement

## 1. Problem

Manual railway track inspection is slow, expensive, and prone to human
error. Defects such as cracks, corrosion, or spalling can go undetected
in time, creating serious safety risks.

## 2. Proposed Solution

An ML model that automatically analyzes railway track images (captured
by a camera) and detects whether and where a defect is present.

## 3. Task Type

**This is an object detection task, not image classification.**

The model (YOLOv8) takes an image as input and outputs one or more
bounding boxes, each with a class label (`defective` or
`non-defective`) and a confidence score. This was a deliberate choice
made once the dataset was selected: the Roboflow "Railway Track Fault
Detection" dataset provides bounding-box annotations, so the project
uses that structure directly rather than converting it into a simpler
whole-image label. Object detection also gives more information than
classification would (where the defect is, not just whether one
exists), which is more useful for a real inspection workflow.

Note: earlier drafts of this document described the MVP as
"classification." That was corrected here to match what was actually
built and evaluated.

## 4. MVP Scope

**In scope (v1):**
- Accepts a single railway track image as input
- Outputs bounding box(es) with class label (`defective` /
  `non-defective`) and confidence score

**Out of scope for now (future versions):**
- Real-time video stream analysis
- GPS tagging or automatic alert delivery to a server - production-stage
  feature, not part of the Capstone MVP
- Multi-class defect typing (crack vs corrosion vs spalling, etc.) -
  the current dataset only distinguishes defective/non-defective;
  the Mendeley "Railway Track Surface Faults" dataset (7 defect types)
  is a candidate for this in a future iteration

## 5. Success Metric

Because this is a safety-related use case, **recall** is prioritized
over precision: missing a real defect (false negative) is more costly
than a false alarm (false positive). Final results are documented in
experiments/final_evaluation.md.

## 6. Dataset

- **Source:** Roboflow Universe - "Railway Track Fault Detection"
- **Version:** 1 (see DATASET.md for exact download instructions)
- **Size:** 1,118 images
- **Classes:** `defective`, `non-defective`
- **License:** CC BY 4.0

Additional datasets (Mendeley "Railway Track Surface Faults", Rail-5k)
are candidates for later stages (multi-class defect detection, v2).

## Status

Stage 3 (EDA) and core Model Gate work (baseline training, comparison
experiment, final test evaluation) are complete. See PROJECT_STATUS.md
for the current overall status.
