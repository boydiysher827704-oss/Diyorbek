# EDA Notes — Roboflow "Railway Track Fault Detection" Dataset

## Dataset Overview

- Source: Roboflow Universe - "Railway Track Fault Detection"
  (workspace: diyorbek-boyxurozov, project: railway-track-fault-detection-hrem8)
- Format: YOLOv8 (bounding box annotations)
- Classes: defective, non-defective
- License: CC BY 4.0

## Split Sizes

| Split | Images | Label files |
|-------|--------|-------------|
| train | 783    | 783         |
| valid | 223    | 223         |
| test  | 112    | 112         |
| Total | 1118   | 1118        |

Every image has a matching label file - no orphaned images or labels.

## Class Balance (bounding boxes per split)

| Split | defective | non-defective | % defective |
|-------|-----------|----------------|-------------|
| train | 555       | 217            | ~72%        |
| valid | 163       | 56             | ~74%        |
| test  | 85        | 24             | ~78%        |

Finding: There is moderate class imbalance - defective boxes outnumber
non-defective roughly 2.5-3x across all splits. Importantly, the ratio is
consistent across train/valid/test, which means Roboflow's split was
stratified. This is good: the model will be evaluated on a distribution
similar to what it trained on.

Implication for modeling: because defective is the majority class,
the model should have enough examples to learn it well. The bigger risk is
under-recognizing non-defective tracks, which could increase false
positives (unnecessary alerts) - a safer failure mode than missing real
defects (false negatives), consistent with our recall-first priority.

## Visual Inspection (sample of 6 training images)

- Several defective bounding boxes cover a large section of the rail
  rather than tightly framing the specific defect - annotation granularity
  is "defect present in this region," not pixel-precise.
- A few images (e.g. filenames starting with RF--) appear to be
  unrelated to rail tracks (a ruler/tool close-up, an ambiguous metal
  surface with markings) - these look like noisy/mislabeled examples worth
  a closer manual review before final training.

## Image Size Audit

| Size (W x H) | Count |
|---------------|-------|
| 416 x 416     | 753   |
| 4000 x 3000   | 28    |
| 3000 x 4000   | 2     |

Most images (753/783 = 96%) were already resized by Roboflow to 416x416.
A small subset (30 images, ~4%) remain at original camera resolution
(~4000x3000). This is not a blocker (YOLO training resizes all images via
imgsz), but it signals inconsistent preprocessing upstream.

## Empty Label Audit

- 27 / 783 (3.4%) train label files are empty (no annotated objects).
- Of the 30 large/original-resolution images, 14 (46.7%) have empty
  labels - a rate ~13x higher than the dataset average.

Finding: Empty labels are strongly correlated with the un-preprocessed,
original-resolution images. This suggests these images may not have been
properly annotated, and combined with the visual inspection finding above
(some large images look unrelated to rail tracks), they are candidates for
manual review or exclusion before training.

## Follow-up: Manual Review of the 14 Empty-Label Large Images

All 14 large-resolution images with empty labels were visually inspected.

Finding: none of them resemble the earlier "noisy" examples spotted
during the general sample review (e.g. the ruler/tool close-up). All 14
show clear, legible rail track scenes - rail, ballast (gravel), wooden
sleepers, bolts - with no obvious visible defect.

Conclusion: the empty labels for these images are very likely
legitimate "no defect present" cases, not annotation gaps. They are usable
as background/negative examples during training. No exclusion needed.

Minor note: a few images (i24, i17, i14) show small colored
pixel artifacts in one corner - likely a compression/metadata rendering
quirk, not a data quality concern.

## Action Items for Preprocessing Stage

1. DONE - Manually review the 30 large-resolution images (and their 14
   empty labels). Decision: keep all 14 as valid background examples.
2. DONE - Confirmed empty-label images are true "no defect" backgrounds,
   not annotation gaps, via visual inspection.
3. Proceed with imgsz=640 during training regardless of original image
   size.
4. The remaining 16 large images (30 total - 14 empty) still have normal
   annotations and need no special handling.

## Data Leakage Check

Risk: if near-duplicate images (e.g. consecutive camera frames of the
same rail spot) ended up split across train and test, the model could
appear to perform well on test data it has effectively already seen.

Assessment: the dataset split (train/valid/test) was performed by
Roboflow, not manually by us. Filenames show varied prefixes (B--,
C--, RF--, i), suggesting images were aggregated from multiple
sources/sessions rather than one continuous video feed - which lowers
(but does not eliminate) the risk of near-duplicate frames being split
across sets.

Decision: no near-duplicate detection was run for this MVP stage,
given time constraints. This is a known limitation, documented here for
transparency. If test performance looks unexpectedly high relative to
visual difficulty, revisit this check (e.g. via perceptual image hashing)
before trusting the metric.

## Status

Stage 3 (Data audit / EDA) - complete. Dataset is downloaded,
structurally verified, class-balance checked, visually inspected, and
documented. Ready to proceed to Stage 4 (baseline model).
