
# Create your views here.

from django.shortcuts import get_object_or_404

from rest_framework import status

from rest_framework import status
from rest_framework.views import APIView

from rest_framework.response import Response 

from text.serializers import textSerializers

from text.models import Text

class textListView(APIView):
	def get(self, request):
		texts = Text.objects.all()
		serializer = textSerializers(texts, many=True)

		return Response(serializer.data)


	def put(self, request):

		serializer = textSerializers(data=request.data)
		if serializer.is_valid():
			serializer.save()

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