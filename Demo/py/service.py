import base64
import json
from dao import store_data, get_data, get_image


def process_data(data):
    try:
        user_info = {
            'Name': data['name'],
            'Password': data['passwd'],
            'Contact number': data['number'],
            'Age': data['age'],
            'Email': data['email_id']
        }
        imgdata = base64.b64decode(data['photo'].split(',')[1])
        store_data(user_info, imgdata, data['uname'])
        return True
    except Exception as e:
        print(Exception(str(e)))
        return False


def process_get_data(uname, passwd):
    result = json.loads(json.dumps(get_data(uname)))
    if result is not None:
        if result['Password'] != passwd:
            return json.dumps({}), 500
        img = get_image(uname)
        result['photo'] = base64.b64encode(img).decode('utf-8')
        return result
    else:
        return json.dumps({}), 200
