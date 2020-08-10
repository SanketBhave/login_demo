from google.cloud import datastore
from flask import Flask, request
import json
import base64
from google.cloud import storage
from flask_cors import CORS, cross_origin

app = Flask(__name__)
CORS(app)

client = datastore.Client.from_service_account_json('C:/Users/Sanket Bhave/Downloads/Login-3e30937a13e2.json')
storage_client = storage.Client.from_service_account_json(
    json_credentials_path='C:/Users/Sanket Bhave/Downloads/Login-storage.json')


def store_image(uname, imgdata):
    try:
        bucket = storage_client.get_bucket('profile_pictures_login_demo')
        blob = bucket.blob(uname)
        blob.upload_from_string(imgdata)
    except Exception as e:
        print(e)
        raise Exception("Cannot store image")


def get_image(uname):
    bucket = storage_client.get_bucket('profile_pictures_login_demo')
    blob = bucket.get_blob(uname)
    image = blob.download_as_string()
    return image


@app.route('/submit', methods=['POST'])
def store():
    try:
        data = json.loads(request.data.decode('utf-8'))
        print(data)
        key = client.key('Username', data['uname'])
        entity = datastore.Entity(key=key)
        entity.update({
            'Name': data['name'],
            'Password': data['passwd'],
            'Contact number': data['number'],
            'Age': data['age'],
            'Email': data['email_id']
        })
        client.put(entity)
        imgdata = base64.b64decode(data['photo'].split(',')[1])
        store_image(data['uname'], imgdata)
        return json.dumps({'success': True}), 200
    except Exception as e:
        return json.dumps({'success': False}), 500


@app.route('/getdata/<uname>/<passwd>', methods=['GET'])
@cross_origin()
def get_data(uname, passwd):
    key = client.key('Username', uname)
    result = json.loads(json.dumps(client.get(key=key)))
    if result is not None:
        if result['Password'] != passwd:
            return json.dumps({}), 500
        img = get_image(uname)
        result['photo'] = base64.b64encode(img).decode('utf-8')
        return result
    else:
        return json.dumps({}), 200


if __name__ == "__main__":
    app.run(port=8000)
