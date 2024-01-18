from django.urls import path
from TaskApp.views import TaskListCreateView

urlpatterns = [
    #path('tasks/', TaskListCreateView.as_view(), name='task-list-create'),
    #path('tasks/<int:pk>/', TaskDetailView.as_view(), name='task-detail'),
    path('api/tasks/', TaskListCreateView.as_view(), name='task-list-create'),
]
