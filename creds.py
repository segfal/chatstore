import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore
from google.oauth2 import service_account
import json 

# Use the application default credentials.
#load credentials from json file
with open('creds.json') as f:
    gcp_cred = json.load(f)

#initialize credentials
cred = credentials.Certificate(gcp_cred)



firebase_admin.initialize_app(cred)

db = firestore.client()

