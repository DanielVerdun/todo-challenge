from django.db import models

# Create your models here.

# Cramos el modelo Task : El cual se encargará de almacenar las datos cada una de las tareas
class Task(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    completed = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title