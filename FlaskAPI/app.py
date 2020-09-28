import pickle
import flask
from flask import Flask, jsonify, request
import json
import numpy as np
from data_input import data_in







app = Flask(__name__)
@app.route('/predict', methods=['GET'])



def load_models():
    file_name = "models/model_file.p"
    with open(file_name, 'rb') as pickled:
        data = pickle.load(pickled)
        model = data['model']
    return model


def predict():
    request_json = request.get_json()
    x=request_json['input']
    x_in = np.array(x).reshape(1,-1)
    model =load_models()
    response = json.dumps({'response': prediction})
    return response, 200




if __name__ == '__main__':
    application.run(debug=True)