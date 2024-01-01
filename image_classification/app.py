
from flask import Flask, request, jsonify
from flask_cors import CORS
import base64
import numpy as np
from PIL import Image
import io

from new_img_classifier import classify_image
from color_identifier import get_dominant_color


app = Flask(__name__)
CORS(app)  # Enable CORS for all routes, including localhost


# TODO: change this function to run the classifier
@app.route('/classifyImage', methods=['POST'])
def classifyImage():
    data = request.get_json()
    img_data_base64 = data.get('imgData', '')
    img_data_bytes = base64.b64decode(img_data_base64.split(',')[1])
    img_np_array = np.array(Image.open(io.BytesIO(img_data_bytes)))
    result = classify_image(img_np_array)
    response = {'result': result}
    return jsonify(response)

@app.route('/getColors', methods=['POST'])
def getColors():
    data = request.get_json()
    img_data_base64 = data.get('imgData', '')
    img_data_bytes = base64.b64decode(img_data_base64.split(',')[1])
    img_np_array = np.array(Image.open(io.BytesIO(img_data_bytes)))
    image = Image.fromarray(img_np_array)
    result = get_dominant_color(image)
    response = {'result': result}
    return jsonify(response)

if __name__ == '__main__':
    app.run(port=5000, debug=True)

