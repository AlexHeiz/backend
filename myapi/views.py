from django.shortcuts import render, redirect
from tasks.models import Task

from rest_framework import viewsets
from .serializers import TaskSerializer


class TaskViewSet(viewsets.ModelViewSet):
    queryset = Task.objects.all().order_by('name')
    serializer_class = TaskSerializer



# Create your views here.
