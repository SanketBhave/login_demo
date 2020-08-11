from google.cloud import storage
from google.cloud import datastore

client = datastore.Client.from_service_account_json('C:/Users/Sanket Bhave/Downloads/Login-3e30937a13e2.json')
storage_client = storage.Client.from_service_account_json(
    json_credentials_path='C:/Users/Sanket Bhave/Downloads/Login-storage.json')


def store_image(uname, imgdata):
    bucket = storage_client.get_bucket('profile_pictures_login_demo')
    blob = bucket.blob(uname)
    blob.upload_from_string(imgdata)


def store_data(user_info, imgdata, uname):
    key = client.key('Username', uname)
    entity = datastore.Entity(key=key)
    entity.update(user_info)
    client.put(entity)
    store_image(uname, imgdata)


def get_data(uname):
    key = client.key('Username', uname)
    return client.get(key=key)


def get_image(uname):
    bucket = storage_client.get_bucket('profile_pictures_login_demo')
    blob = bucket.get_blob(uname)
    image = blob.download_as_string()
    return image
