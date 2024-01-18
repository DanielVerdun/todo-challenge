
from rest_framework import generics
from .models import Task #importamos models
from .serializers import TaskSerializer # importamos serializers
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import authentication_classes, permission_classes
from rest_framework.authentication import BasicAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

"""
@authentication_classes([BasicAuthentication])
@permission_classes([IsAuthenticated])
class TaskListCreateView(APIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    permission_classes = [IsAuthenticated]


@authentication_classes([BasicAuthentication])
@permission_classes([IsAuthenticated])
class TaskDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    permission_classes = [IsAuthenticated]

"""
class TaskListCreateView(APIView):
    def get(self, request):
        # Obtener la lista de tareas desde el modelo
        tasks = Task.objects.all()

        # Serializar las tareas
        serializer = TaskSerializer(tasks, many=True)

        # Devolver la respuesta
        return Response(serializer.data)

    def post(self, request):
        # Lógica para crear una nueva tarea
        serializer = TaskSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)