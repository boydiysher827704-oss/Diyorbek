# Final Evaluation — baseline_v1 (Selected Candidate)

## Important Caveat: Confirmed Data Leakage

A near-duplicate check (run after this evaluation — see EDA_NOTES.md
"Data Leakage Check") found that **~12.5% of test images have a
near-identical match in the training set** (14/112, mostly exact
perceptual matches). This means the metrics below are likely somewhat
**optimistic** — the model had effectively already seen a portion of
the "held out" test data. True generalization performance on fully
novel images is probably modestly lower than reported here. This is
disclosed as a known, unresolved limitation (see ISSUE_LOG.md Issue 5)
rather than corrected in this submission due to time constraints.

## Purpose
One-time evaluation of the selected candidate (baseline_v1, YOLOv8n,
30 epochs) on the protected test set. The test set was not used in any
prior decision (model selection was based on validation metrics only,
see experiment2_50epoch.md).

## Test Set
112 images, 109 labeled instances, never used during training or model
selection.

## Results

| Class | Precision | Recall | mAP50 | mAP50-95 |
|---|---|---|---|---|
| defective | 0.692 | 0.739 | 0.702 | 0.397 |
| non-defective | 0.489 | 0.833 | 0.601 | 0.369 |
| **all (overall)** | **0.590** | **0.786** | **0.651** | **0.383** |

## Comparison: Validation vs Test

| Metric | Validation (baseline_v1) | Test | Delta |
|---|---|---|---|
| Precision | 0.684 | 0.590 | -0.094 |
| Recall | 0.680 | 0.786 | +0.106 |
| mAP50 | 0.678 | 0.651 | -0.027 |
| mAP50-95 | 0.430 | 0.383 | -0.047 |

## Error Analysis

**Recall improved on test vs validation** (0.680 -> 0.786), including for
the safety-critical `defective` class (0.699 -> 0.739). This is a
favorable result relative to our stated priority (recall over precision
for safety reasons - see PROBLEM_STATEMENT.md).

**Precision dropped notably** (0.684 -> 0.590), driven mostly by
`non-defective` precision falling to 0.489. In practice this means: when
the model predicts "non-defective," it is right only about half the
time on this test set. Likely contributing factors:

1. **Small test set** for `non-defective` - only 24 instances - makes
   this metric high-variance; a few extra false positives shift the
   percentage sharply.
2. **Class imbalance** (documented in EDA_NOTES.md: ~72-78% defective
   across all splits) means the model saw far fewer non-defective
   examples during training, making it less confident/accurate at
   correctly identifying them.
3. **Loosely-drawn bounding boxes** in the training data (EDA finding)
   may cause the model to flag defect-adjacent regions as defective
   even when the specific area is not.

## Practical Implication

The current model is a reasonable **safety-oriented baseline**: it
catches most real defects (high recall) at the cost of extra false
alarms (lower precision) - a safer failure mode than silently missing
defects. It is **not** yet precise enough to fully trust `non-defective`
predictions without human spot-checks.

## Next Steps (Beyond MVP Scope for Now)
- Address class imbalance (e.g. targeted collection/augmentation of
  non-defective examples) to improve precision without sacrificing
  recall.
- Investigate tighter bounding-box annotation for defective examples to
  improve mAP50-95 (localization precision).
- Consider a larger model (YOLOv8s) if compute budget allows, now that
  YOLOv8n's plateau is documented (see experiment2_50epoch.md).

## Status
**Model Gate core evaluation complete.** No further tuning was done
after seeing this test result (test set integrity preserved).
