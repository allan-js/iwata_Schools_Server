from django.shortcuts import render

from rest_framework import viewsets
from rest_framework import filters
from django_filters.rest_framework import DjangoFilterBackend

from .models import StudentWork
from .serializers import StudentWorkSerializer

def homepage(request):
    return render(request, 'index.html', {})


class StudentWorkViewSet(viewsets.ModelViewSet):
    queryset = StudentWork.objects.all()
    serializer_class = StudentWorkSerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    filterset_fields = ['is_archived', 'student']
    search_fields = ['name', 'student']
    ordering_fields = ['created', 'updated']