# Project Status

## Project
Railway Track Defect Detection

## Current stage
Data Gate (finishing) -> moving into Model Gate

## Completed
- Problem defined, MVP scope set (see PROBLEM_STATEMENT.md)
- Repository structure created (data/, notebooks/, src/, models/, experiments/)
- Dataset downloaded (Roboflow "Railway Track Fault Detection", 1118 images,
  YOLOv8 format, CC BY 4.0)
- Full EDA completed and documented (see EDA_NOTES.md): split sizes, class
  balance, visual inspection, image size audit, empty-label audit
- Data leakage risk assessed (documented limitation: no near-duplicate
  detection run yet)
- **Baseline model trained** (YOLOv8n, 30 epochs, GPU, ~8 min):
  overall P=0.684, R=0.680, mAP50=0.678, mAP50-95=0.430
  (see experiments/baseline_v1.md for full results)

## Current task
Run a second experiment (different config) to compare against the
baseline, per Model Gate requirement of at least two configurations.

## Next
- Run experiment #2 (e.g. more epochs, or yolov8s instead of yolov8n)
- Add a formal issue log (Observation -> Risk -> Decision -> Evidence ->
  Status) summarizing EDA findings in Data Gate format
- Select final candidate using validation data only (not test set)
- Evaluate once on protected test set
- Save and verify reloadable inference artifacts (best.pt + loading code)

## Known problems / blockers
- No near-duplicate/leakage detection run yet (documented in
  EDA_NOTES.md as a known limitation, not blocking MVP)
- No reusable preprocessing script in src/ yet — preprocessing so far is
  done inline in the Colab notebook
