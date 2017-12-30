from rest_framework import serializers
from . import models

class taskSerializer(serializers.ModelSerializer):
	class Meta:
		model = models.task
		fields= '__all__'