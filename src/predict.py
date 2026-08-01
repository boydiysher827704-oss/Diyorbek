"""
predict.py

Minimal, reusable script to load the trained model and run inference on
a single railway track image. This is the "reload check" artifact for
the Model Gate: it proves the saved weights can be loaded and used in a
clean process without retraining.

Usage:
    python src/predict.py path/to/image.jpg

Requirements:
    pip install ultralytics

Expects the trained weights at models/best.pt (see models/README.md for
how to obtain this file).
"""

import sys
from pathlib import Path

from ultralytics import YOLO

MODEL_PATH = Path(__file__).resolve().parent.parent / "models" / "best.pt"


def load_model(model_path: Path = MODEL_PATH) -> YOLO:
    """Load the trained YOLO model from disk."""
    if not model_path.exists():
        raise FileNotFoundError(
            f"Model weights not found at {model_path}. "
            "See models/README.md for how to obtain best.pt."
        )
    return YOLO(str(model_path))


def predict_image(model: YOLO, image_path: str):
    """Run inference on a single image and return the results object."""
    results = model(image_path)
    return results


def summarize(results) -> None:
    """Print a simple, human-readable summary of the detections."""
    class_names = results[0].names
    boxes = results[0].boxes

    if boxes is None or len(boxes) == 0:
        print("No defects detected.")
        return

    print(f"Detected {len(boxes)} object(s):")
    for box in boxes:
        cls_id = int(box.cls[0])
        conf = float(box.conf[0])
        print(f"  - {class_names[cls_id]} (confidence: {conf:.2%})")


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python src/predict.py path/to/image.jpg")
        sys.exit(1)

    image_path = sys.argv[1]
    model = load_model()
    results = predict_image(model, image_path)
    summarize(results)
