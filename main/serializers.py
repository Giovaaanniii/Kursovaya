from rest_framework import serializers
from .models import Task, Excursions

class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = '__all__'
        
class ExcursionsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Excursions
        fields = '__all__'