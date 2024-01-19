"""
from django.urls import path
from TaskApp.views import TaskListCreateView, TaskDetailView

urlpatterns = [
    #path('tasks/', TaskListCreateView.as_view(), name='task-list-create'),
    #path('tasks/<int:pk>/', TaskDetailView.as_view(), name='task-detail'),
    path('api/tasks/', TaskListCreateView.as_view(), name='task-list-create'),
    path('api/tasks/<int:task_id>/', TaskDetailView.as_view(), name='task-detail'),
]
"""

# En este archivo es indispensable importar la siguientes librerias
from rest_framework import routers
from TaskApp.viewsets import TaskViewSet

router = routers.SimpleRouter() # Define las rutas para nuestro modelo. GET,POST,PUT,DELETE
router.register('tasks', TaskViewSet) # registramos la url y recibe el ViewSet como segundo parámetro

urlpatterns = router.urls
