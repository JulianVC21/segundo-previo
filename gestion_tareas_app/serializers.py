from . import models
from rest_framework import serializers

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.User
        fields = '__all__'
        
class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Task
        fields = '__all__'

class CompleteTaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Task
        fields = ['id', 'isDone']