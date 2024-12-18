from rest_framework import serializers
from .models import Histoy

class HistoySerializer(serializers.ModelSerializer):
    class Meta:
        model = Histoy
        fields = '__all__'
        