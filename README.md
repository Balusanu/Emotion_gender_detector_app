# 📌 Emotion & Gender Prediction App

This project is a simple and intuitive **Streamlit web app** that predicts **emotion** and **gender** from any uploaded image using **DeepFace** and **OpenCV**.
It detects all faces in the image and displays:

* 🎭 Dominant emotion
* 👤 Gender
* 📦 Optional bounding boxes around faces
* 📊 Top emotion probabilities

---

## 🚀 Features

* Upload any image (JPG / JPEG / PNG)
* Detect multiple faces
* Predict:

  * **Emotion**
  * **Gender**
* Show top 3 emotion probabilities
* Draw bounding boxes with labels
* Clean UI built using Streamlit
* Fast and lightweight

---

## 🛠️ Tech Stack

* **Python**
* **Streamlit**
* **DeepFace**
* **OpenCV**
* **NumPy**
* **Pillow (PIL)**

---

## 📦 Installation

### 1️⃣ Clone the repository

```bash
git clone https://github.com/yourname/emotion-gender-app.git
cd emotion-gender-app
```

### 2️⃣ Install dependencies

```bash
pip install -r requirements.txt
```

### 3️⃣ Run the app

```bash
streamlit run app.py
```

---

## 📁 Project Structure

```
├── app.py              # Main Streamlit application
├── requirements.txt    # Required Python packages
└── README.md           # Project documentation
```

---

## 🧠 How It Works

1. User uploads an image
2. Image is processed using **OpenCV**
3. DeepFace analyzes:

   * Emotion
   * Gender
4. Results are rendered on the UI
5. Bounding boxes and labels are added for clarity

---

## 📷 Supported Emotions

* Angry
* Disgust
* Fear
* Happy
* Sad
* Surprise
* Neutral

---

## 👨‍💻 Author

**Made with ❤️ by Balasubramanya**
