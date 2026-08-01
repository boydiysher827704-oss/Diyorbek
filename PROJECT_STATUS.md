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
- **Experiment 2 run** (YOLOv8n, 50 epochs): no meaningful improvement
  over baseline (see experiments/experiment2_50epoch.md). Decision:
  baseline_v1 (30 epochs) selected as final candidate based on
  validation evidence.

## Current task
Evaluate the selected candidate (baseline_v1) once on the protected test
set, and save/verify reloadable inference artifacts.

## Next
- Run final test-set evaluation (test set untouched until now)
- Basic error analysis with concrete examples
- Save best.pt + minimal inference script to models/
- Verify reload works in a clean process
- Add a formal issue log (Observation -> Risk -> Decision -> Evidence ->
  Status) summarizing EDA findings in Data Gate format

## Known problems / blockers
- No near-duplicate/leakage detection run yet (documented in
  EDA_NOTES.md as a known limitation, not blocking MVP)
- No reusable preprocessing script in src/ yet — preprocessing so far is
  done inline in the Colab notebook
