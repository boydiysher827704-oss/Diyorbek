# Experiment: baseline_v2_50epoch

## Goal
Test whether increasing training length (more epochs) improves on the
baseline, before trying more expensive changes (bigger model, more data).

## Configuration
Same as baseline_v1, except:

| Parameter | Value |
|---|---|
| Epochs | 50 (was 30) |
| Training time | ~13.8 minutes (0.230 hours) |

## Results (validation set, 223 images, 219 instances)

| Class | Precision | Recall | mAP50 | mAP50-95 |
|---|---|---|---|---|
| defective | 0.684 | 0.703 | 0.682 | 0.387 |
| non-defective | 0.698 | 0.643 | 0.685 | 0.464 |
| **all (overall)** | **0.691** | **0.673** | **0.684** | **0.426** |

## Comparison with baseline_v1 (30 epochs)

| Metric | v1 (30 ep) | v2 (50 ep) | Delta |
|---|---|---|---|
| Precision (overall) | 0.684 | 0.691 | +0.007 |
| Recall (overall) | 0.680 | 0.673 | -0.007 |
| mAP50 | 0.678 | 0.684 | +0.006 |
| mAP50-95 | 0.430 | 0.426 | -0.004 |
| Recall (defective) | 0.699 | 0.703 | +0.004 |
| Recall (non-defective) | 0.661 | 0.643 | -0.018 |

## Conclusion

Extending training from 30 to 50 epochs produced **no meaningful
improvement** - metrics are within noise of each other, and overall
recall (our priority metric) is marginally worse with more epochs. This
suggests the model has plateaued for this configuration (YOLOv8n,
default augmentation, this dataset size/quality) and further gains would
likely require a different lever: a larger model (YOLOv8s), better
annotation quality (see EDA note on loosely-drawn boxes), or more/better
data rather than simply more epochs.

## Decision

**baseline_v1 (30 epochs) is selected as the final candidate.** Given
statistically indistinguishable performance, the faster-to-train
configuration is preferred (simplicity, faster iteration for any future
work), consistent with keeping the MVP appropriately scoped.

This decision is based entirely on validation set evidence. The test set
has not yet been used for any decision.

## Status
Complete. Proceeding to final test-set evaluation using baseline_v1.
