# 🩺 Heart Disease Prediction Web App

This project is part of the **Predictive Modelling Bootcamp Project**, where we built a machine learning model to predict whether a person is likely to suffer from heart failure based on clinical features. The model is deployed using **Flask**, with a responsive **HTML/CSS frontend**.

---

## 📌 Project Objective

To develop a predictive system using ML techniques that can identify potential heart disease cases based on patient medical data. The goal was to:

- Achieve an accuracy of 80% or higher
- Deploy the model using a **Flask web app**
- Integrate a **custom-styled HTML frontend**
- Host all project files in a GitHub repository

---

## 💻 Technologies Used

| Component     | Tool / Library              |
|---------------|-----------------------------|
| Programming   | Python                      |
| Model         | **SVC (Support Vector Classifier)** |
| Preprocessing | StandardScaler              |
| Web Framework | Flask                       |
| Frontend      | HTML + CSS (custom design)  |
| Notebook      | Google Colab                |
| Version Ctrl  | Git & GitHub                |

---

## 📁 Project Structure
heart-disease-prediction/
├── app.py # Flask backend
├── model_heart.pkle # Trained ML model (SVC)
├── scaler.pkle # Preprocessing scaler
├── project1.ipynb # Model training in Google Colab
├── templates/
│ └── heart_form.html # HTML frontend form
└── static/
└── background image(s) # Background used in the web form



##  📊 Model Overview
Model Used: Support Vector Classifier (SVC)

Scaler: StandardScaler from scikit-learn

Accuracy Achieved: Over 80%

Input Features:

Age

Anaemia

Creatinine Phosphokinase

Diabetes

Ejection Fraction

High Blood Pressure

Platelets

Serum Creatinine

Serum Sodium

Sex

Smoking

Time (follow-up period)


## ⚙️ How to Run Locally

> Make sure Python is installed, and you're in a **virtual environment (optional but recommended).**

```bash
# Clone the repository
git clone https://github.com/YOUR_USERNAME/heart-disease-predictions.git

cd heart-disease-predictions

# (Optional) Create and activate virtual environment
python -m venv venv
venv\Scripts\activate  # On Windows

# Install required packages
pip install -r requirements.txt

# Run Flask app
python app.py

Visit: http://127.0.0.1:5000 to use the app.
---
