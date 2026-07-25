# Problem Statement

## 1. Problem

Manual railway track inspection is slow, expensive, and prone to human error.
Defects such as cracks, corrosion, or spalling can go undetected in time,
creating serious safety risks.

## 2. Proposed Solution

An ML model that automatically analyzes railway track images (captured by a
camera) and detects whether a defect is present.

## 3. MVP Scope

**In scope (v1 - Classification):**
- Accepts a single railway track image as input
- Outputs a label: `defective` or `normal`
- Outputs a confidence score (%)

**Out of scope for now (future versions):**
- Real-time video stream analysis
- Localizing the defect within the image (bounding box) — planned for v2
  using object detection (YOLO)
- GPS tagging or automatic alert delivery to a server — production-stage
  feature, not part of the Capstone MVP

## 4. Success Metric

Because this is a safety-related use case, **recall** is prioritized over
precision: missing a real defect (false negative) is more costly than a
false alarm (false positive). Target metrics will be finalized after the
baseline model is trained (see `experiments/` in later stages).

## 5. Initial Dataset

- **Source:** Roboflow — "Railway Track Fault Detection"
- **Size:** 1,118 images
- **Classes:** `defective`, `non-defective`
- **License:** CC BY 4.0

Additional datasets (Mendeley "Railway Track Surface Faults", Rail-5k) are
candidates for later stages (multi-class defect detection, v2).

## Status

This is a living document. It will be updated as the project evolves
through the course stages (EDA, baseline, experiments, final demo).
