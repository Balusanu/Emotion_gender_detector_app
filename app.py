import streamlit as st
from deepface import DeepFace
import cv2
import numpy as np
from PIL import Image

# -------------------------------------------------------
# Streamlit App Settings
# -------------------------------------------------------
st.set_page_config(page_title="Emotion & Gender Predictor", layout="centered")
st.title("Emotion & Gender Prediction App")
st.write("Upload an image and the app will predict **emotion** and **gender** for every detected face.")

# -------------------------------------------------------
# File Uploader
# -------------------------------------------------------
uploaded_file = st.file_uploader("Upload an image", type=["jpg", "jpeg", "png"])
show_boxes = st.checkbox("Show face bounding boxes", True)

if uploaded_file:

    # -------------------------------------------------------
    # Convert Uploaded Image to OpenCV Format
    # -------------------------------------------------------
    file_bytes = np.asarray(bytearray(uploaded_file.read()), dtype=np.uint8)
    img = cv2.imdecode(file_bytes, cv2.IMREAD_COLOR)  # BGR format
    img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)    # Convert to RGB for DeepFace

    st.image(img_rgb, caption="Uploaded Image", use_container_width=True)

    # -------------------------------------------------------
    # DeepFace Analysis: Emotion + Gender
    # -------------------------------------------------------
    with st.spinner("Analyzing image..."):
        try:
            results = DeepFace.analyze(
                img_path=img_rgb,
                actions=['emotion', 'gender'],   # Removed age
                enforce_detection=False
            )
        except Exception as e:
            st.error(f"Error during analysis: {e}")
            st.stop()

    # DeepFace returns dict for 1 face, list for multiple
    if isinstance(results, dict):
        results = [results]

    annotated = img_rgb.copy()

    # -------------------------------------------------------
    # Process Each Detected Face
    # -------------------------------------------------------
    for idx, res in enumerate(results):
        st.subheader(f"Face {idx + 1}")

        # Extract Predictions
        emotion = res.get("dominant_emotion")
        emotion_scores = res.get("emotion")
        gender = res.get("gender")

        # Display Predictions
        st.write(f"**Gender:** {gender}")
        st.write(f"**Emotion:** {emotion}")

        # Show Top 3 Emotions
        if emotion_scores:
            st.write("Top emotions:")
            top3 = sorted(emotion_scores.items(), key=lambda x: x[1], reverse=True)[:3]
            for em, score in top3:
                st.write(f"- {em}: {score:.2f}")

        # Face Region for Bounding Box
        region = res.get("region", {})
        x = int(region.get("x", 0))
        y = int(region.get("y", 0))
        w = int(region.get("w", 0))
        h = int(region.get("h", 0))

        # Draw Bounding Box + Label
        if show_boxes:
            cv2.rectangle(annotated, (x, y), (x + w, y + h), (255, 0, 0), 2)
            label = f"{gender}, {emotion}"
            cv2.putText(
                annotated,
                label,
                (x, max(y - 10, 10)),
                cv2.FONT_HERSHEY_SIMPLEX,
                0.6,
                (255, 0, 0),
                2
            )

    # -------------------------------------------------------
    # Display Annotated Image
    # -------------------------------------------------------
    st.image(annotated, caption="Predicted Results", use_container_width=True)

# -------------------------------------------------------
# Footer Caption
# -------------------------------------------------------
st.markdown(
    """
    <div style='text-align: center; padding-top: 30px; font-size: 16px;'>
        Made with ❤️ by <b>Balasubramanya</b>
    </div>
    """,
    unsafe_allow_html=True
)
