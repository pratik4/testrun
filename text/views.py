
# Create your views here.

from django.shortcuts import get_object_or_404

from rest_framework import status

from rest_framework import status
from rest_framework.views import APIView

from rest_framework.response import Response 

from text.serializers import textSerializers

from text.models import Text


#Initialize Firebase
config = {
    'apiKey': "AIzaSyA5gYcZ_MgnzGLxpdL0gcrxUnn6vMWXzhM",
    'authDomain': "circle-cb012.firebaseapp.com",
    'databaseURL': "https://circle-cb012.firebaseio.com",
    'projectId': "circle-cb012",
    'storageBucket': "circle-cb012.appspot.com",
    'messagingSenderId': "180871157784",}

import pyrebase

firebase = pyrebase.initialize_app(config)

database = firebase.database()

# def create(request):

# 	data = {
# 		'text' = 'text',
# 	}
# 	database.child('testruns').set(data)
# 	return Response()



# var admin = require("firebase-admin");

# var serviceAccount = require("/home/turing/startup/testing/circle-cb012-firebase-adminsdk-prsh0-6e6294c720.json");

# admin.initializeApp({
#   credential: admin.credential.cert(serviceAccount),
#   databaseURL: "https://circle-cb012.firebaseio.com"
# });

# cred = credentials.Certificate('/home/turing/startup/testing/circle-cb012-firebase-adminsdk-prsh0-6e6294c720.json')
# # default_app = firebase_admin.initialize_app(cred)

# # Use the application default credentials
# # cred = credentials.ApplicationDefault()
# firebase_admin.initialize_app(cred, {
#   'projectId': 'circle-cb012',
# })

# db = firestore.client()

# doc_ref = db.collection(u'users').document(u'alovelace')
# doc_ref.set({
#     u'first': u'Ada',
#     u'last': u'Lovelace',
#     u'born': 1815
# })

import time
class textListView(APIView):
	def get(self, request):
		texts = Text.objects.all()
		serializer = textSerializers(texts, many=True)
		k = database.child('testruns').get().val()
		data = [k[i] for i in k.keys()]
		return Response(data)


	def put(self, request):

		serializer = textSerializers(data=request.data)
		# if serializer.is_valid():
		# 	serializer.save()
		if serializer.is_valid():
			print(serializer)
			t = int(time.time())

			database.child('testruns').child(t).set(serializer.data)

			return Response(serializer.data)

class textDetailView(APIView):
	def get(self, request, pk):
		texts = get_object_or_404(Text, pk=pk)
		serializer = textSerializers(texts)

		return Response(serializer.data)

	def delete(self, request, pk):
		text = get_object_or_404(Text,pk=pk)
		text.delete()
		return Response(status.HTTP_204_NO_CONTENT)