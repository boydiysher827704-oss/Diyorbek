"""
streamlit_app.py

Minimal public demo for the Railway Track Defect Detection project.
Upload a photo of a rail section; the trained YOLOv8 model (models/best.pt,
committed in this repo) returns a defective / non-defective prediction.

This is the same trained model used in src/predict.py and documented in
experiments/final_evaluation.md — no retraining happens here.

Run locally:
    pip install -r requirements.txt
    streamlit run streamlit_app.py

Deployed publicly via Streamlit Community Cloud (see README.md).
"""

import streamlit as st
from PIL import Image
from ultralytics import YOLO

st.set_page_config(page_title="Railway Track Defect Detector", page_icon="🚆")


@st.cache_resource
def load_model():
    return YOLO("models/best.pt")


model = load_model()

st.title("🚆 Railway Track Defect Detector")
st.write(
    "Upload a photo of a railway track section. The model will flag it as "
    "**defective** or **non-defective** with a confidence score."
)
st.caption(
    "Capstone demo model (YOLOv8n). Not validated for real safety "
    "decisions — see the project repository for full evaluation results "
    "and known limitations (including a confirmed data-leakage caveat)."
)

uploaded = st.file_uploader("Upload an image", type=["jpg", "jpeg", "png"])

if uploaded is not None:
    image = Image.open(uploaded).convert("RGB")

    with st.spinner("Running detection..."):
        results = model(image)
        result = results[0]

    st.image(result.plot(), caption="Detection result", use_container_width=True)

    boxes = result.boxes
    if boxes is not None and len(boxes) > 0:
        best_idx = boxes.conf.argmax().item()
        cls_name = result.names[int(boxes.cls[best_idx])]
        conf = float(boxes.conf[best_idx])
        if cls_name == "defective":
            st.error(f"Prediction: **{cls_name}** (confidence: {conf:.1%})")
        else:
            st.success(f"Prediction: **{cls_name}** (confidence: {conf:.1%})")
    else:
        st.warning("No defect detected with sufficient confidence.")
else:
    st.info("Upload a JPG or PNG image of a rail section to get a prediction.")
