import numpy as np
from flask import Flask,render_template, redirect, url_for, request, jsonify
import pickle

with open("model.pkl", "rb") as file:
    model = pickle.load(file)
app = Flask(__name__)

@app.route("/")
def home():   
            return render_template("test.html")
@app.route("/predict", methods=["POST"])
def predict():
    float_values = [float(x) for x in request.form.values()]
    features = [np.array(float_values)]
    prediction = model.predict(features)
    species= ['Iris-setosa','Iris-versicolor','Iris-virginica']
    if prediction == 0:
        output = species[0]
    elif prediction== 1:
        output = species[1]
    else:
        output = species[2]
    return render_template("test.html", prediction_text="The Flower specie is: {}" .format(output))

if __name__ == "__main__":
    app.run(debug = True)