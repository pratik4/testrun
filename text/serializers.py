from rest_framework import serializers

from .models import Text

class textSerializers(serializers.ModelSerializer):

	class Meta:
		model = Text
		fields = 'id', 'text'


