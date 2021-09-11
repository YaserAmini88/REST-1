from rest_framework import serializers
from . models import Sports

class sportsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sports
        fields = '__all__'