
from rest_framework import viewsets # Importamos librerias viewsets
from .serializers import TaskSerializer # importamos serializers
from .models import Task # Importamos models
from .filters import TaskFilter
from rest_framework import generics
import django_filters
import logging
from rest_framework.response import Response
from rest_framework import status

# Importamos para implementar autenticación
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication

# Importamos para manejar los token
from django.contrib.auth.models import User
#from rest_framework import viewsets
from rest_framework.authtoken.models import Token
from .serializers import TokenSerializer
from django_filters.rest_framework import DjangoFilterBackend

logger = logging.getLogger(__name__)

class TaskViewSet(viewsets.ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    authentication_classes = [TokenAuthentication]  # Nos Asegúramos de importar TokenAuthentication
    permission_classes = [IsAuthenticated]

    filter_backends = [DjangoFilterBackend]
    filterset_class = TaskFilter
    
class TaskListCreateView(generics.ListCreateAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    filter_backends = [django_filters.rest_framework.DjangoFilterBackend]
    filterset_class = TaskFilter
    authentication_classes = [TokenAuthentication]  # Nos Asegúramos de importar TokenAuthentication
    permission_classes = [IsAuthenticated]

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)
