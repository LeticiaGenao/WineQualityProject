from flask import Flask, request, render_template
import pickle
import numpy as np

app = Flask(__name__)

# Load the trained model 
model = pickle.load(open('best_ridge_model.pkl', 'rb'))

@app.route('/', methods=['GET'])
def home():
    # Display the HTML form to input wine features
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    try:
        # Retrieve data from form; 
        input_features = [
            float(request.form['density']),
            float(request.form['residual_sugar']),
            float(request.form['free_sulfur_dioxide']),
            float(request.form['alcohol'])
        ]
        features = np.array(input_features).reshape(1, -1)
        prediction = model.predict(features)[0]

        # Convert prediction to a string or relevant output format
        prediction = f"Predicted wine quality score: {prediction:.2f}"

        return render_template('index.html', prediction=prediction)
    except Exception as e:
        return f"Error: {e}"

if __name__ == '__main__':
    app.run(debug=True)
