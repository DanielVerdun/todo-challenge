
from rest_framework import viewsets # Importamos librerias viewsets
from .serializers import TaskSerializer # importamos serializers
from .models import Task # Importamos models


class TaskViewSet(viewsets.ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer