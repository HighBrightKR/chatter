import firebase_admin
from certifi import where
from firebase_admin import credentials, firestore
from datetime import datetime
import platform
import os
import requests
from google.cloud.firestore_v1 import FieldFilter
from google.cloud.firestore_v1.base_query import BaseCompositeFilter
from crypt import Cryptor

cryptor = Cryptor()

class DataBase:
    def __init__(self):
        cred = credentials.Certificate('cred.json')
        firebase_admin.initialize_app(cred)
        self.db = firestore.client()

    def registration(self, user_id, user_pw, username, auth):
        user_pw = cryptor.enc_pw(user_pw)
        user_ref = self.db.collection('user').document(user_id)
        user_data = {
            'username': username,
            'pw': user_pw,
            'auth' : auth,
            'intro' : "",

        }
        user_ref.set(user_data)

    def get_user_data(self, user_id):
        user_ref = self.db.collection('user').document(user_id)
        user_data = user_ref.get().to_dict()
        user_data['user_id'] = str(user_id)
        return user_data


    def login_log(self, user_id):
        response = requests.get('https://ipinfo.io')
        data = response.json()
        ip = data['ip']
        try: country = data['country']
        except: country = "알 수 없음"
        current_time = datetime.now()
        login_ref = self.db.collection('user').document(user_id).collection("login_log").document(str(current_time.timestamp()).replace(".", ""))
        os_name = platform.system()
        architecture = platform.architecture()[0]
        if os_name == 'Windows':
            os_version = platform.release()
            result = f"{os_name} {os_version} {architecture}"
        elif os_name == 'Linux':
            uname_info = os.uname()
            os_version = uname_info.release
            os_name = uname_info.sysname
            result = f"{os_name} {os_version} {architecture}"
        else:
            result = f"{os_name} {architecture}"
        login_data = {
            "time" : current_time.strftime("UTC %Y년 %m월 %d일 %H시 %M분"),
            "os" : result,
            "country" : country,
            "ip" : ip,
        }
        login_ref.set(login_data)

    def get_login_log(self, user_id):
        login_ref = self.db.collection('user').document(user_id).collection('login_log')
        return login_ref.get()

    def profile_change(self, user_id, data):
        user_ref = self.db.collection('user').document(user_id)
        user_ref.update(data)

    def get_user_list(self):
        user_ref = self.db.collection('user')
        return user_ref.get()

    def load_chat(self, user_id, cp_user_id):
        ff1 = FieldFilter('sender', 'in', [user_id, cp_user_id])
        ff2 = FieldFilter('receiver', 'in', [user_id, cp_user_id])
        chat_ref = self.db.collection('chat').where(filter=BaseCompositeFilter("AND", [ff1, ff2])) \
            .order_by('time')
        return chat_ref.get()

    def send_chat(self, user_id, cp_user_id, msg):
        chat_ref = self.db.collection('chat')
        #current_time = datetime.now()
        data = {
            "msg" : msg,
            "time" : firestore.SERVER_TIMESTAMP,
            "sender" : user_id,
            "receiver" : cp_user_id,
        }
        chat_ref.add(data)

    def get_name_by_id(self, user_id):
        user_ref = self.db.collection('user').document(user_id)
        return user_ref.get().get('username')

    def get_icon_by_id(self, user_id):
        user_ref = self.db.collection('user').document()

    def get_pw_by_id(self, user_id):
        user_ref = self.db.collection('user').document(user_id)
        return user_ref.get().get('pw')

    def add_sus_log(self, user_id, log:dict):
        user_ref = self.db.collection('user').document(user_id).collection('suspend_log')
        data = {
            "when" : firestore.SERVER_TIMESTAMP,
            "reason" : log['reason'],
            "manager" : log['manager'],
            "period" : log['period'],
            "until" : log['until'],
        }
        user_ref.add(data)