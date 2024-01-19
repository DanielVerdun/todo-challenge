
from rest_framework import viewsets # Importamos librerias viewsets
from .serializers import TaskSerializer # importamos serializers
from .models import Task # Importamos models
from .filters import TaskFilter
from rest_framework import generics
import django_filters

class TaskViewSet(viewsets.ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer

class TaskListCreateView(generics.ListCreateAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    filter_backends = [django_filters.rest_framework.DjangoFilterBackend]
    filterset_class = TaskFilter

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)
