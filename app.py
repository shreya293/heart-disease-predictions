# from flask import Flask, render_template, request  # importing the flask module
# import numpy as np  # for numerical operations
# import pandas as pd  # for data manipulation
# import pickle  # to bring in the model

# # Load the trained model
# import gzip
# import pickle

# with gzip.open('model_heart.pkle', 'rb') as f:
#     model = pickle.load(f)

# app = Flask(__name__)  # initialize the Flask app

# @app.route('/')  # default route
# def home():
#     return render_template('heart_form.html')  # Your HTML input form

# @app.route('/predict', methods=['POST'])  # route for prediction
# def predict():
#     # Extracting form inputs
#     age = float(request.form['age'])
#     anaemia = int(request.form['anaemia'])
#     creatinine_phosphokinase = float(request.form['creatinine_phosphokinase'])
#     diabetes = int(request.form['diabetes'])
#     ejection_fraction = float(request.form['ejection_fraction'])
#     high_blood_pressure = int(request.form['high_blood_pressure'])
#     platelets = float(request.form['platelets'])
#     serum_creatinine = float(request.form['serum_creatinine'])
#     serum_sodium = float(request.form['serum_sodium'])
#     sex = int(request.form['sex'])
#     smoking = int(request.form['smoking'])
#     time = int(request.form['time'])

#     # Make prediction
#     input_data = np.array([[age, anaemia, creatinine_phosphokinase, diabetes,
#                             ejection_fraction, high_blood_pressure, platelets,
#                             serum_creatinine, serum_sodium, sex, smoking, time]])
#     prediction = model.predict(input_data)

#     # Output message
#     result = "The person has Heart Disease." if prediction[0] == 1 else "The person does not have Heart Disease."

#     return render_template('heart_form.html', result=result)


# if __name__ == '__main__':
#     app.run(debug=True, port=5000)
from flask import Flask, render_template, request
import numpy as np
import pickle
import gzip

# Load the trained model
# Correct way to load uncompressed model
with gzip.open('model.pkl', 'rb') as f:
    model = pickle.load(f)

with gzip.open('scaler.pkle', 'rb') as f:
    scaler = pickle.load(f)


app = Flask(__name__)

@app.route('/')
def home():
    return render_template('heart_form.html')

@app.route('/predict', methods=['POST'])
def predict():
    # Extracting form inputs
    age = float(request.form['age'])
    anaemia = int(request.form['anaemia'])
    creatinine_phosphokinase = float(request.form['creatinine_phosphokinase'])
    diabetes = int(request.form['diabetes'])
    ejection_fraction = float(request.form['ejection_fraction'])
    high_blood_pressure = int(request.form['high_blood_pressure'])
    platelets = float(request.form['platelets'])
    serum_creatinine = float(request.form['serum_creatinine'])
    serum_sodium = float(request.form['serum_sodium'])
    sex = int(request.form['sex'])
    smoking = int(request.form['smoking'])
    time = int(request.form['time'])

    # Same logic as in your working Colab code
    input = (age, anaemia, creatinine_phosphokinase, diabetes,
             ejection_fraction, high_blood_pressure, platelets,
             serum_creatinine, serum_sodium, sex, smoking, time)

    input_np = np.asarray(input).reshape(1, -1)
    input_scaled = scaler.transform(input_np)  # Important!

    prediction = model.predict(input_scaled)

    result = "The person has Heart Disease." if prediction[0] == 1 else "The person does not have Heart Disease."

    return render_template('heart_form.html', result=result)

if __name__ == '__main__':
    app.run(debug=True, port=5000)
