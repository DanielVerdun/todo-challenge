
# Crear serializadores para convertir objetos Python en formatos de datos compatibles con JSON.


from dataclasses import field
from rest_framework import serializers # Importamos de rest_framework la libreria serializers
from .models import Task
# Importamos para manejar los token
from rest_framework.authtoken.models import Token

# Definimos la class para nuestro models
class TaskSerializer(serializers.ModelSerializer):
    class Meta: # Creamos una class Meta que recibirá el nombre de nuestro modelo
        model = Task # Nombre del modelo con el que vamos a trabajar
        fields = '__all__'# Nombre de los campos que utilizaremos del modelo mencionado. (En este caso usaremos todos)

        # Luego lo siguiente que haremos, es crear el archivo viewsets.py

# Definimos la class TokenSerializer
class TokenSerializer(serializers.ModelSerializer):
    class Meta:
        model = Token
        fields = ('key', 'user', 'created')
