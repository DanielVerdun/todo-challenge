
# ToDo Challenge Invera

Una aplicación web utilizando Python, Django para la gestión de tareas, donde los usuarios pueden crear, eliminar, marcar como completadas y filtrar tareas. Se hace uso de librerías y paquetes estandares que reducen la cantidad de código propio añadido. Calidad y arquitectura de código. Facilidad de lectura y mantenimiento del código. Además, la aplicación poseé pruebas unitarias y mapeo de logs.

El desarrollo sigue las bases de PEP (Python Enhancement Proposals) y utiliza el estilo de codificación de PEP 8 como estándar para la escritura de código en Python. PEP 8 es la guía de estilo oficial de Python que proporciona recomendaciones sobre la forma de escribir código Python para que sea legible y consistente.

Algunas de las pautas de PEP 8 que son relevantes para el desarrollo en Django incluyen:

## Indentación:

  - Utilizar 4 espacios por nivel de sangrado.
  - No mezclar espacios y tabuladores para la sangría.

## Longitud de línea:

  - Líneas de código de hasta 79 caracteres.
  - Límites de 72 caracteres para docstrings y comentarios.

## Espacios en blanco en expresiones y declaraciones:

  - No colocar espacios alrededor de paréntesis, corchetes o llaves internos.
  - Colocar un espacio alrededor de operadores y después de comas.

## Convenciones de nombres:

  - Utilizar nombres en minúsculas para las funciones, métodos y variables.
  - Utilizar nombres en mayúsculas para constantes.
  - Utilizar el estilo snake_case para nombres de variables y funciones.

## Importaciones:

  - Agrupar las importaciones en tres secciones: estándar de Python, de terceros y locales.
  - Dejar una línea en blanco entre cada sección de importaciones.

## Docstrings:

  - Incluir docstrings en todas las funciones y módulos para documentar el código.

## Comentarios:

  - Utilizar comentarios con moderación y centrarse en explicar el "por qué" en lugar del "cómo".
  - Evitar comentarios obvios o redundantes.

## Convenciones específicas de Django:

  - Utilizar nombres explícitos para las rutas en las configuraciones de URL.
  - Utilizar Model.objects.get() en lugar de Model.objects.get_or_create() si solo se espera que exista un objeto.  


## Estado del Proyecto

  - En desarrollo
 

## Instalación

  1. Clona el repositorio: git clone git@github.com:DanielVerdun/todo-challenge.git
  2. En el mismo directorio crear un entorno virtual python: python3 -m venv env
  3. Activar entorno: source env/bin/activate
  4. Ingresa al directorio del proyecto: cd todo-challenge
  5. Cambiar a branch develop: git checkout develop
  6. Ingresar al directorio Core: cd Core/
  7. Instala las dependencias: pip3 install -r requirements.txt

## Estructura del proyecto
	  .
	  ├── Core
	  │   ├── asgi.py
	  │   ├── __init__.py
	  │   ├── __pycache__
	  │   ├── settings.py
	  │   ├── urls.py
	  │   └── wsgi.py
	  ├── db.sqlite3
	  ├── django.log
	  ├── manage.py
	  ├── requirements.txt
	  ├── TaskApp
	  │   ├── admin.py
	  │   ├── apps.py
	  │   ├── filters.py
	  │   ├── __init__.py
	  │   ├── migrations
	  │   ├── models.py
	  │   ├── __pycache__
	  │   ├── serializers.py
	  │   ├── tests.py
	  │   ├── urls.py
	  │   ├── viewsets.py
	  │   └── views.py
	  └── users
	      ├── admin.py
	      ├── apps.py
	      ├── __init__.py
	      ├── migrations
	      ├── models.py
	      ├── __pycache__
	      ├── serializers.py
	      ├── tests.py
	      ├── urls.py
	      └── views.py



## Uso:

1. Ejecutar server: python3 manage.py runserver

	La aplicación cuenta con un panel de administración donde se pueden administrar los usuarios autorizados y sus token. 
	http://127.0.0.1:8000/admin/
	Al momento del desarrollo, creamos un usaurio para poder testear la funcionalidad.
	
	email: usertest@gmail.com
	password: 123456

2. Para acceder a los endpoint de la aplicación debemos autenticarlos al siguiente url:

	solicitar token: http://127.0.0.1:8000/api/v1.0/authentication/token/
	
	Parámetros de entrada: 
		{
		"email":"usertest@gmail.com",
		"password": "123456"
		}
	
	Parámetros de salida si esta autenticado:
		{
		"token":"xxxxxxxxxxxxxxxxxxxxx"
		
		}
	
	
	Parámetros de salida si no esta autenticado:
		{
		"detail": "Authentication credentials were not provided."
		
		}
	
	Para autenticar debemos pasar el token por headers al realizar el request.

3. Una ves que estamos autenticados podremos acceder a todos los endpoint de la app:

	Obtener lista de tareas: http://127.0.0.1:8000/api/v1.0/tasks/  "GET"


4. Crear una tarea: http://127.0.0.1:8000/api/v1.0/tasks/   "POST"

	Ejemplo de parámetros de entrada: 
		{
		"title": "Tarea 4",
		"description": "Descripción de la tarea 4",
		"completed": false
		}
	
	
	5. Actualizar una tarea: http://127.0.0.1:8000/api/v1.0/tasks/{id} "PUT"
	
	Ejemplo de parámetros de entrada: 
		{
		"title": "Tarea 4",
		"description": "Descripción de la tarea 4",
		"completed": true
		}

5. Eliminar una tarea :
   	http://127.0.0.1:8000/api/v1.0/tasks/{id} "DELETE"


6. Filtrar por fecha y contenido de la tarea:
	http://127.0.0.1:8000/api/v1.0/tasks/?created_at__gte=2022-01-01&created_at__lte=2022-01-31&content__icontains=Probando_filtro
 
	
Disponibilidad para realizar una pequeña demo del proyecto al finalizar el challenge. (Se ha notificado por mail)
