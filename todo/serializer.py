from django.contrib.auth.models import Group, User
from rest_framework import serializers
from .models import Todo

# Serializers define the API representation.
class TdoSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['title', 'description', 'created_at']