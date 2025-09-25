# Desafío de Desarrollo - [Invera ToDo-List]

Este repositorio contiene la solución al desafío de desarrollo propuesto, implementando una aplicación web con Django/Django Rest Framework, PostgreSQL, Gunicorn y Nginx, todo orquestado con Docker Compose.

La solución se encuentra desarrollada en la rama `develop`.

## 🚀 Cómo Ejecutar la Solución

Sigue estos pasos para poner en marcha la aplicación en tu entorno local:

### 1. Requisitos Previos

Asegúrate de tener instalado lo siguiente:

* **Docker Desktop** (o Docker Engine y Docker Compose)
* **Git**

### 2. Clonar el Repositorio

Si aún no lo has hecho, clona el repositorio:


    git clone https://github.com/DanielVerdun/todo-challenge.git
    cd todo-challenge 

### 3. Cambiar a la Rama de Desarrollo


    git checkout develop

### 4. Configuración del Entorno (.env)

Crea un archivo .env en la raíz del proyecto. Este archivo contendrá las variables de entorno necesarias para la base de datos y la aplicación. Puedes usar el siguiente ejemplo como base:


    # Variables de Base de Datos PostgreSQL
    POSTGRES_DB=mydatabase
    POSTGRES_USER=myuser
    POSTGRES_PASSWORD=mypassword
    DATABASE_HOST=postgres
    DATABASE_PORT=5432
    
    # Configuración de Django
    DJANGO_SECRET_KEY='tu_secret_key_aqui'
    DJANGO_DEBUG=True # Cambiar a False en producción
    ALLOWED_HOSTS='localhost,127.0.0.1' # Añadir otros hosts si es necesario
    CSRF_TRUSTED_ORIGINS='http://localhost:8000' # Importante para Nginx y CSRF
    
    # Otras configuraciones
    # Puede que necesites añadir variables específicas de tu aplicación

### 5. Iniciar la Aplicación con Docker Compose

Una vez configurado el archivo .env, puedes construir e iniciar todos los servicios:


    docker-compose up --build

Este comando:

Construirá las imágenes de Docker (si hay cambios).

Creará y levantará los contenedores de postgres, web y nginx.

Ejecutará las migraciones de Django y recolectará los archivos estáticos.

### 6. Crear un Superusuario (Para autenticar y acceder al Admin)

Para acceder al panel de administración de Django, necesitarás un superusuario. Correr el siguiente comando en una terminal paralera mientras corren los servicios:


    docker-compose exec web python manage.py createsuperuser

Sigue las instrucciones en la terminal para crear tu usuario.

### 7. Acceder a la Aplicación

La aplicación estará disponible en tu navegador en:

Aplicación principal: http://localhost:8000/

Panel de Administración de Django: http://localhost:8000/admin/

===========================================================================

## 🛠️ Prueba de la API (con Postman)

Para probar los endpoints de la API, puedes usar Postman o cualquier otro cliente HTTP.

### 1. Obtener un Token de Autenticación

Realiza una solicitud POST a /api/v1.0/authentication/token/ con tus credenciales de superusuario (o cualquier usuario).

URL: http://localhost:8000/api/v1.0/authentication/token/

Método: POST

Body (raw, JSON):

    {
    "email": "tu_email",
    "password": "tu_contraseña"
    }

Recibirás una respuesta con tu token:

    {
    "token": "token_generado"
    }

### 2. Acceder a un Endpoint Protegido ( GET: /api/v1.0/tasks/)

Usa el token obtenido para acceder a un endpoint que requiera autenticación.

URL: http://127.0.0.1:8000/api/v1.0/tasks/

Método: GET

Headers:

Key: Authorization

Value: Token token_generado (reemplaza "token_generado" con el token real)

Deberías obtener una respuesta exitosa con los datos de las tareas.

===========================================================================

## 📸 Evidencias de Funcionamiento
A continuación, se presentan algunas capturas de pantalla para demostrar el correcto funcionamiento de la solución.(Puedes usar estos datos para test)

### Obtener token de autenticacion para un Usuario:

POST: http://127.0.0.1:8000/api/v1.0/authentication/token/
<img width="1005" height="356" alt="image" src="https://github.com/user-attachments/assets/0ce5590f-bda3-474c-8491-a73c2961e645" />

### List Task:

GET: http://127.0.0.1:8000/api/v1.0/tasks/
<img width="1476" height="841" alt="image" src="https://github.com/user-attachments/assets/e697fdc0-efa0-4a0e-b8ad-9f663ede28f0" />

### Create Task:

POST: http://127.0.0.1:8000/api/v1.0/tasks/
<img width="1007" height="478" alt="image" src="https://github.com/user-attachments/assets/ffb4753f-81d8-4cf9-89a2-a53ea898e0c9" />

### Update Task:

PUT: http://127.0.0.1:8000/api/v1.0/tasks/{id}/
<img width="1007" height="486" alt="image" src="https://github.com/user-attachments/assets/25398deb-678f-453e-9be3-842e3c040b28" />

### Delete Task
DELETE: http://127.0.0.1:8000/api/v1.0/tasks/{id}/
<img width="1013" height="388" alt="image" src="https://github.com/user-attachments/assets/85edc5d8-f652-47f2-bc1a-fee4208b9cce" />


  
