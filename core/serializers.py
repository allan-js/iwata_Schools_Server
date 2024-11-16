from rest_framework import routers, serializers, viewsets

from .models import StudentWork

class StudentWorkSerializer(serializers.ModelSerializer):
    class Meta:
        model = StudentWork
        fields = ['id', 'student', 'name', 'file']