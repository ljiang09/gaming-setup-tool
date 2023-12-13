
from flask import Flask, request, jsonify
from flask_cors import CORS
from new_img_classifier import classify_image


app = Flask(__name__)
CORS(app)  # Enable CORS for all routes, including localhost


# TODO: change this function to run the classifier
@app.route('/classifyImage', methods=['POST'])
def classifyImage():
    result = classify_image()
    response = {'result': result}
    return jsonify(response)

if __name__ == '__main__':
    app.run(port=5000, debug=True)

