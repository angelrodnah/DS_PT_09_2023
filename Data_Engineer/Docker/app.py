import os
import numpy as np
from flask import Flask, render_template, request
import joblib
# Set current folder as working directory
os.chdir(os.path.dirname(__file__))

# Constants
TEMPLATE_DIR = os.path.join(os.path.dirname(__file__), 'templates')
STATIC_DIR = os.path.join(os.path.dirname(__file__), 'static')
IRIS_LABELS = {1: "Iris-setosa", 2: "Iris-versicolor", 3: "Iris-virginica"}

# Load the model
model_file = open('model.pkl', 'rb')
model = joblib.load(model_file)

# Create the Flask app
app = Flask(__name__, template_folder=TEMPLATE_DIR, static_folder=STATIC_DIR)

@app.route('/')
def home():
    """Render the home page."""
    return render_template('index.html')

@app.route('/predict', methods=['GET', 'POST'])
def predict():
    """Handle prediction requests."""
    if request.method == 'POST':
        try:
            # Get user input and convert to floats
            sepal_length = float(request.form['sepal_length'])
            sepal_width = float(request.form['sepal_width'])
            petal_length = float(request.form['petal_length'])
            petal_width = float(request.form['petal_width'])

            # Validate input (optional)
            if any(value < 0 for value in [sepal_length, sepal_width, petal_length, petal_width]):
                error_message = "Todos los valores deben ser números positivos."
                return render_template('predict.html', error=error_message)

            # Prepare prediction input
            pred_args = np.array([sepal_length, sepal_width, petal_length, petal_width]).reshape(1, -1)

            # Make prediction
            model_prediction = model.predict(pred_args)[0]
            prediction = IRIS_LABELS[model_prediction]

            return render_template('predict.html', prediction=prediction)
        except ValueError:
            error_message = "Error: Ingrese valores numéricos válidos."
            return render_template('predict.html', error=error_message)
    else:
        return render_template('predict.html')

if __name__ == '__main__':
    app.run(debug=True)
