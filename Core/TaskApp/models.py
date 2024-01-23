from django.db import models

# Create your models here.


class Task(models.Model):
# Cramos el modelo Task : El cual se encargará de almacenar las datos cada una de las tareas
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    completed = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

