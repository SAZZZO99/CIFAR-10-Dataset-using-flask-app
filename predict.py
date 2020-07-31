#BACKEND

import base64
import numpy as np
import io
from PIL import Image
import tensorflow.keras as keras
from tensorflow.keras.models import Sequential
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing.image import ImageDataGenerator
from tensorflow.keras.preprocessing.image import img_to_array
from flask import request
from flask import jsonify
from flask import Flask

app = Flask(__name__)


def get_model():
    global model
    model = load_model("keras_cifar10_trained_model.h5")
    print("*model is loaded")


def preprocess_image(image, target_size):
    if image.mode != "RGB":
        image = image.convert("RGB")
    image = image.resize(target_size)
    image = img_to_array(image)
    image = np.expand_dims(image, axis=0)

    return image


print(" *Loading Keras model....")
get_model()


@app.route("/predict", methods=["POST"])
def predict():
    message = request.get_json(force=True)
    encoded = message['image']
    decoded = base64.b64decode(encoded)
    image = Image.open(io.BytesIO(decoded))
    processed_image = preprocess_image(image, target_size=(32, 32))

    prediction = model.predict(processed_image).tolist()

    response = {
        'prediction': {
            'airplane': prediction[0][0],
            'automobile': prediction[0][1],
            'bird': prediction[0][2],
            'cat': prediction[0][3],
            'deer': prediction[0][4],
            'dog': prediction[0][5],
            'frog': prediction[0][6],
            'horse': prediction[0][7],
            'ship': prediction[0][8],
            'truck': prediction[0][9]

        }
    }
    return jsonify(response)
