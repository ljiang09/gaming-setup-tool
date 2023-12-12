
from flask import Flask, request, jsonify
from flask_cors import CORS


app = Flask(__name__)
CORS(app)  # Enable CORS for all routes, including localhost


# TODO: change this function to run the classifier
@app.route('/hello', methods=['POST'])
def hello():
    data = request.get_json()
    name = data.get('name', '')
    response = {'message': f'Hello, {name}!'}
    return jsonify(response)

if __name__ == '__main__':
    app.run(debug=True)

