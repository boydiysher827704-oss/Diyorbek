"""
train.py

End-to-end, reproducible training script for the railway track defect
detection model. Downloads the dataset from Roboflow, trains a YOLOv8n
model, and evaluates it on the validation and test sets.

This mirrors the exact steps used to produce the results documented in
experiments/baseline_v1.md and experiments/final_evaluation.md.

Usage:
    python src/train.py

Requirements:
    pip install -r requirements.txt

A GPU is strongly recommended (CPU training is roughly 40-50x slower
for this dataset - see experiments/baseline_v1.md notes).

You will be prompted for a Roboflow API key. Get a free one at:
https://app.roboflow.com/settings/api
"""

from getpass import getpass

from roboflow import Roboflow
from ultralytics import YOLO

WORKSPACE = "diyorbek-boyxurozov"
PROJECT = "railway-track-fault-detection-hrem8"
VERSION = 1
EPOCHS = 30
IMG_SIZE = 640
BATCH_SIZE = 16
RUN_NAME = "baseline_v1_reproduced"


def download_dataset():
    """Download the exact dataset version used for this project."""
    api_key = getpass("Roboflow API key: ")
    rf = Roboflow(api_key=api_key)
    project = rf.workspace(WORKSPACE).project(PROJECT)
    dataset = project.version(VERSION).download("yolov8")
    return dataset


def train_model(data_yaml_path: str):
    """Train YOLOv8n on the downloaded dataset."""
    model = YOLO("yolov8n.pt")
    results = model.train(
        data=data_yaml_path,
        epochs=EPOCHS,
        imgsz=IMG_SIZE,
        batch=BATCH_SIZE,
        name=RUN_NAME,
    )
    return model, results


def evaluate_on_test(model: YOLO, data_yaml_path: str):
    """Run a one-time evaluation on the held-out test set."""
    test_results = model.val(
        data=data_yaml_path,
        split="test",
        name=f"{RUN_NAME}_test_eval",
    )
    print("\n--- Test Set Results ---")
    print(f"Precision: {test_results.box.mp:.3f}")
    print(f"Recall:    {test_results.box.mr:.3f}")
    print(f"mAP50:     {test_results.box.map50:.3f}")
    print(f"mAP50-95:  {test_results.box.map:.3f}")


def main():
    print("Downloading dataset...")
    dataset = download_dataset()
    data_yaml_path = f"{dataset.location}/data.yaml"

    print("\nTraining model...")
    model, _ = train_model(data_yaml_path)

    print("\nEvaluating on test set...")
    evaluate_on_test(model, data_yaml_path)

    print(f"\nDone. Best weights saved under runs/detect/{RUN_NAME}/weights/best.pt")
    print("Copy that file to models/best.pt to use it with src/predict.py")


if __name__ == "__main__":
    main()
