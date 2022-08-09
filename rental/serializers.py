from rest_framework import serializers
from .models import cycle,sport,electronic

class cycleSerializer (serializers.ModelSerializer):
    class Meta:
        model = cycle
        fields = ['id', 'name', 'email','contact', 'describe']

class sportSerializer (serializers.ModelSerializer):
    class Meta:
        model = sport
        fields = ['id', 'name', 'email','contact', 'describe']

class electronicSerializer (serializers.ModelSerializer):
    class Meta:
        model = electronic
        fields = ['id', 'name', 'email','contact', 'describe']