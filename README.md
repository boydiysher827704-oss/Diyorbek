# Railway Track Defect Detection

AI/ML Capstone project: automatically detecting defects (cracks, corrosion,
etc.) on railway tracks from images.

## Status

🚧 Early stage — problem scope defined, dataset selection in progress.

## Project Documents

- [Problem Statement](./PROBLEM_STATEMENT.md) — problem, MVP scope, success
  metric, and dataset

## Course Stages

1. Scope and problem definition ✅
2. GitHub repository and project organization ⏳
3. Data audit, EDA, preprocessing, leakage prevention
4. Baseline, experiments, MLflow, model selection
5. Final usable inference/demo workflow
6. Reproducibility, documentation, submission, defense preparation

## Author

Diyorbek

## Project Structure

data/raw/         original, unmodified datasets
data/processed/   cleaned/split data, ready for training
notebooks/        EDA and experiment notebooks
src/              reusable Python code (data loading, training, eval)
models/           trained model weight files
experiments/      MLflow experiment tracking
