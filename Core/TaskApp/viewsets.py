
from rest_framework import viewsets # Importamos librerias viewsets
from .serializers import TaskSerializer # importamos serializers
from .models import Task # Importamos models
from .filters import TaskFilter
from rest_framework import generics
import django_filters
import logging
from rest_framework.response import Response
from rest_framework import status

logger = logging.getLogger(__name__)

class TaskViewSet(viewsets.ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
"""
    # Agragamos funciones para registro de logs
    def perform_create(self, serializer):
        try:
            serializer.save()
            logger.info('Nueva tarea creada')
        except Exception as e:
            logger.error(f'Error al crear una tarea: {str(e)}')

    def perform_update(self, serializer):
        try:
            serializer.save()
            logger.info('Tarea actualizada')
        except Exception as e:
            logger.error(f'Error al actualizar una tarea: {str(e)}')

    def perform_destroy(self, instance):
        try:
            instance.delete()
            logger.info('Tarea eliminada')
        except Exception as e:
            logger.error(f'Error al eliminar una tarea: {str(e)}')
"""
class TaskListCreateView(generics.ListCreateAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    filter_backends = [django_filters.rest_framework.DjangoFilterBackend]
    filterset_class = TaskFilter

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)
"""
    def get(self, request, *args, **kwargs):
        try:
            return self.list(request, *args, **kwargs)
        except Exception as e:
            logger.error(f'Error al obtener la lista de tareas: {str(e)}')
            return Response({'detail': 'Error en la solicitud'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    def perform_create(self, serializer):
        try:
            serializer.save()
            logger.info('Nueva tarea creada')
        except Exception as e:
            logger.error(f'Error al crear una tarea: {str(e)}')
"""