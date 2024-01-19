
# Crear serializadores para convertir objetos Python en formatos de datos compatibles con JSON.
"""
from rest_framework import serializers
from .models import Task

class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = ['title', 'description', 'completed', 'created_at']

"""
# importamos de la rest_framework la libreria serializers
from dataclasses import field
from rest_framework import serializers
from .models import Task

# Definimos la una class que serialize nuestro models
class TaskSerializer(serializers.ModelSerializer):
    class Meta: # Creamos una class Meta que recibirá el nombre de nuestro modelo
        model = Task # Nombre del modelo con el que vamos a trabajar
        fields = '__all__'# Nombre de los campos que utilizaremos del modelo mencionado. (En este caso usaremos todos)

        # Luego lo siguiente que haremos, es crear el archivo viewsets.py

