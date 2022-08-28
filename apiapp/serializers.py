from rest_framework import serializers
from .models import Apiapp
class TodoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Apiapp
        fields = ["id", "task", "completed", "timestamp", "updated", "user"]