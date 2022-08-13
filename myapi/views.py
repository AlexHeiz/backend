from django.http import JsonResponse, HttpResponse
from tasks.models import Task
from rest_framework import viewsets
from .serializers import TaskSerializer


class TaskViewSet(viewsets.ModelViewSet):
    queryset = Task.objects.all().order_by('created_date')
    serializer_class = TaskSerializer

def set_complete(request, pk):
    task = Task.objects.get(pk=pk)
    task.completed = True
    task.save()
    response = JsonResponse({
        'id': task.id,
        'name': task.name,
        'description': task.description,
        'completed': task.completed,
        'created_date': task.created_date,
    })

    return response