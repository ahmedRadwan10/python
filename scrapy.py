

import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore

cred = credentials.Certificate("nlp-analysis-20947-firebase-adminsdk-elwlv-ba0bac792f.json")
firebase_admin.initialize_app(cred)

db = firestore.client()

names = db.collection("names")

names.document().set({
    'name': "YASSER"
})
