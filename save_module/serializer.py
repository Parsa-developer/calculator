from rest_framework import serializers
from .models import SaveData

class DataSerializer(serializers.ModelSerializer):
    text = serializers.JSONField()
    class Meta:
        model = SaveData
        fields = ['text']