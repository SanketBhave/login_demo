
from flask import Flask, request
import json

from flask_cors import CORS, cross_origin
from service import process_data, process_get_data

app = Flask(__name__)
CORS(app)


@app.route('/submit', methods=['POST'])
def store():
    data = json.loads(request.data.decode('utf-8'))
    if process_data(data):
        return json.dumps({'success': True}), 200
    else:
        return json.dumps({'success': False}), 500


@app.route('/getdata/<uname>/<passwd>', methods=['GET'])
@cross_origin()
def get_data(uname, passwd):
    return process_get_data(uname, passwd)


if __name__ == "__main__":
    app.run(port=8000)
