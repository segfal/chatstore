

import time 
import datetime
import firebase_admin
from firebase_admin import firestore
from creds import db
class Message:
    def __init__(self,message,username):
        self.message = message
        self.username = username
        self.timestamp = datetime.datetime.fromtimestamp(time.time()).strftime('%Y-%m-%d %H:%M:%S')


msg = Message('segfal','Hello World')





while True:
    username = input('Enter your username: ')
    message = input('Enter your message: ')
    msg = Message(message,username)
    doc_ref = db.collection(u'chatstore').document(f'{msg.timestamp} + {msg.username}')
    doc_ref.set({
        u'message': msg.message,
        u'username': msg.username,
        u'timestamp': msg.timestamp
    })
    print('Message sent!')
    time.sleep(4)