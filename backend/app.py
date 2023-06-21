from flask import Flask, request
from flask_cors import CORS
from sklearn.ensemble import RandomForestRegressor
from sklearn.neighbors import KNeighborsClassifier
import pickle
import os
import numpy as np

# 'tensorflow-local'
# import tensorflow as tf

import pandas as pd

from PIL import Image
from io import BytesIO
import base64
import json
import re
import sys

app = Flask(__name__)
CORS(app)
app.config['MAX_CONTENT_LENGTH'] = 16 * 1000 * 1000

mnist_model = None

# 'tensorflow-local'
# cats_model = None

def load_mnist_model():
    # load the pre-trained model (here we are using a model
    # pre-trained of week 8, but you can
    # substitute in your own networks just as easily)
    global mnist_model
        # create prediction
    mnist_model = KNeighborsClassifier(n_neighbors=4, weights='distance')
    model_filename = os.path.join(os.path.dirname(os.path.abspath(__file__)), "knn_clf.pkl")
    with open(model_filename, 'rb') as f:
        mnist_model = pickle.load(f)


"""
# 'tensorflow-local'
def load_cats_model():
    global cats_model
    cats_model = tf.keras.models.load_model('cats_model')
"""

@app.route('/api/prediction/mnist', methods=['POST'])
def predict_mnist():
    try:
        image_data = re.sub('^data:image/.+;base64,', '', request.get_json()['image'])
        im = Image.open(BytesIO(base64.b64decode(image_data)))
        # im.save('canvas.png')
        im28x28 = im.resize((28, 28)).convert('L') #resize the image to 28x28 and converts it to gray scale

        # image to numpy
        np_image = np.asarray(im28x28)
        # assert(np_image.shape == (28, 28))
        print(np.abs(np_image.reshape(28*28)-[255]))

        # np.abs(np_image.reshape(28*28)-[255])
        # reshapes the image to 28x28 pixes, substracts 255 from every value and applys abs to the matrix.
        # this has to be done, becuase the mnist values are "Pixel values are 0 to 255. 0 means background (white), 255 means foreground (black). " (s. http://yann.lecun.com/exdb/mnist/)
        # Grayscale uses 0 for black and 255 for white.
        predicted_number = mnist_model.predict([np.abs(np_image.reshape(28*28)-[255])])
        print(predicted_number)

        buffered = BytesIO()
        im28x28.save(buffered, format="PNG")
        # im28x28.save('canvas2.png')
        img_str = base64.b64encode(buffered.getvalue())
        img_base64 = bytes("data:image/png;base64,", encoding='utf-8') + img_str
        return json.dumps({'image': str(img_base64.decode('utf-8')), 'prediction': predicted_number[0]}), 200, {'ContentType': 'application/json'}
    except Exception as err:
        return json.dumps({'error': str(err)})

"""
pythonanywhere free can't load tensorflow because the package is to large.
if you want to use it localy, remove the comments 'tensorflow-local' in this file
@app.route('/api/prediction/cats', methods=['POST'])
def predict_cats():
    try:
        image_data = re.sub('^data:image/.+;base64,', '', request.get_json()['image'])
        im = Image.open(BytesIO(base64.b64decode(image_data)))
        im.save('cat.png')
        cat = im.resize((160, 160)).convert('RGB')
         #singel_tmp_image = tf.keras.utils.load_img('leopard.jpg',
                                            #target_size=IMG_SIZE,
                                            #interpolation="nearest")
        # image to numpy
        np_image = np.asarray(cat)
        np_image = np.reshape(np.asarray(np_image), ((1, 160, 160, 3)))
        predicted_cats = cats_model.predict([np_image])
        class_names = ['cheetah', 'leopard', 'lion', 'tiger']
        print(predicted_cats)

        return json.dumps({'prediction': list(zip(class_names, predicted_cats[0].astype(float)))}), 200, {'ContentType': 'application/json'}
    except Exception as err:
        return json.dumps({'error': str(err)})
"""

@app.route("/")
def hello_world():

    print(request.args)
    return "<p>Current model!</p>" + str(mnist_model)

# if this is the main thread of execution first load the model and
# then start the server
if __name__ == "__main__" or __name__ == "app" or __name__ == "flask_app":
    print(("* Loading model and Flask starting server..."
        "please wait until server has fully started"))
    load_mnist_model()

    # 'tensorflow-local'
    #load_cats_model()

    print(sys.executable)
    print('running')
