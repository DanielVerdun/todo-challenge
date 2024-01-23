
# Importamos libreirias para necesarias para realizar los test
# ------------------------------------------------------------
from django.test import TestCase, RequestFactory
from .models import Task # Importamos models para realizar pruebas
from django.utils import timezone
from .serializers import TaskSerializer # Importamos serializers para realizar pruebas

# Importamos para realizar pruebas a la viewset TaskViewSet
from rest_framework.test import APIClient 
from rest_framework import status
# Importamos para realizar pruebas a la viewset TaskListCreateView
from .views import TaskListCreateView
from .filters import TaskFilter

# Ralizamos pruebas unitarias del model utilizado para la base de datos
#----------------------------------------------------------------------
class TaskModelTestCase(TestCase):

    def setUp(self):
        # Configuración inicial para las pruebas
        self.task = Task.objects.create(
            title='Tarea 1',
            description='Descripción de la tarea 1',
            completed=False,
        )

    def test_task_creation(self):
        # Verificar que se crea una tarea correctamente
        self.assertEqual(self.task.title, 'Tarea 1')
        self.assertEqual(self.task.description, 'Descripción de la tarea 1')
        self.assertFalse(self.task.completed)
        self.assertIsNotNone(self.task.created_at)

    def test_task_str_method(self):
        # Verificar que el método __str__ devuelve el título de la tarea
        self.assertEqual(str(self.task), 'Tarea 1')

    def test_task_completion(self):
        # Verificar que una tarea se puede marcar como completada
        self.task.completed = True
        self.task.save()
        self.assertTrue(self.task.completed)

    def test_task_created_at_auto_now_add(self):
        # Verificar que el campo created_at se establece automáticamente
        task = Task.objects.create(title='Tarea 1')
        self.assertIsNotNone(task.created_at)

    def test_task_created_at_timezone(self):
        # Verificar que el campo created_at utiliza la zona horaria actual
        task = Task.objects.create(title='Tarea 1')
        now = timezone.now()
        self.assertLess(task.created_at, now)



# Ralizamos pruebas unitarias del serializers utilizado para convertir la data a json
#------------------------------------------------------------------------------------
class TaskSerializerTestCase(TestCase):

    def setUp(self):
        # Configuración inicial para las pruebas
        self.task_data = {
            'title': 'Tarea 1',
            'description': 'Descripción de la tarea 1',
            'completed': False,
        }
        self.task_instance = Task.objects.create(**self.task_data)
        self.serializer = TaskSerializer(instance=self.task_instance)

    def test_serializer_data(self):
        # Verificar que el serializador contiene los datos correctos
        self.assertEqual(self.serializer.data['title'], 'Tarea 1')
        self.assertEqual(self.serializer.data['description'], 'Descripción de la tarea 1')
        self.assertEqual(self.serializer.data['completed'], False)

    def test_serializer_create(self):
        # Verificar que el serializador crea una tarea correctamente
        new_task_data = {
            'title': 'Tarea 2',
            'description': 'Descripción de la tarea 2',
            'completed': True,
        }
        serializer = TaskSerializer(data=new_task_data)
        self.assertTrue(serializer.is_valid())
        new_task = serializer.save()
        self.assertEqual(new_task.title, 'Tarea 2')
        self.assertEqual(new_task.description, 'Descripción de la tarea 2')
        self.assertEqual(new_task.completed, True)

    def test_serializer_update(self):
        # Verificar que el serializador actualiza una tarea correctamente
        updated_task_data = {
            'title': 'Tarea 1',
            'description': 'Descripción de la tarea 1',
            'completed': True,
        }
        serializer = TaskSerializer(instance=self.task_instance, data=updated_task_data, partial=True)
        self.assertTrue(serializer.is_valid())
        updated_task = serializer.save()
        self.assertEqual(updated_task.title, 'Tarea 1')
        self.assertEqual(updated_task.description, 'Descripción de la tarea 1')
        self.assertEqual(updated_task.completed, True)


# Ralizamos pruebas unitarias al viewset TaskViewSet
#----------------------------------------------------------------------

# Estos tests fallan por que no se obtiene el status code esperado.(En desarrollo)

"""
class TaskViewSetTestCase(TestCase):

    def setUp(self):
        # Configuración inicial para las pruebas
        self.task = Task.objects.create(
            title='Tarea 1',
            description='Descripción de la tarea 1',
            completed=False,
        )
        self.client = APIClient()

    def test_get_task_list(self):
        # Verificar que se puede obtener la lista de tareas
        response = self.client.get('http://127.0.0.1:8000/api/tasks/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertGreater(len(response.data), 0)

    def test_create_task(self):
        # Verificar que se puede crear una nueva tarea
        data = {'title': 'Tarea 1', 'description': 'Descripción de la tarea 1', 'completed': False}
        response = self.client.post('/api/tasks/', data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Task.objects.filter(title='Tarea 1').count(), 1)

    def test_update_task(self):
        # Verificar que se puede actualizar una tarea existente
        data = {'title': 'Tarea 1', 'description': 'Descripción de la tarea 1', 'completed': True}
        response = self.client.put(f'/api/tasks/{self.task.id}/', data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.task.refresh_from_db()
        self.assertEqual(self.task.title, 'Tarea 1')
        self.assertEqual(self.task.description, 'Descripción de la tarea 1')
        self.assertTrue(self.task.completed)

    def test_delete_task(self):
        # Verificar que se puede eliminar una tarea existente
        response = self.client.delete(f'/api/tasks/{self.task.id}/')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Task.objects.filter(id=self.task.id).count(), 0)

"""


# Ralizamos pruebas unitarias al viewset TaskViewSet
#----------------------------------------------------------------------

"""
class TaskListCreateViewTestCase(TestCase):

    def setUp(self):
        # Configuración inicial para las pruebas
        self.factory = RequestFactory()
        self.task = Task.objects.create(
            title='Tarea 1',
            description='Descripción de la tarea',
            completed=False,
        )

    def test_task_list_view(self):
        # Prueba para verificar que la vista devuelve una lista de tareas
        request = self.factory.get('/tasks/')
        view = TaskListCreateView.as_view()
        response = view(request)
        self.assertEqual(response.status_code, 200)

    def test_task_create_view(self):
        # Prueba para verificar que se puede crear una nueva tarea a través de la vista
        data = {'title': 'Tarea 1', 'description': 'Descripción de la tarea', 'completed': False}
        request = self.factory.post('/tasks/', data)
        view = TaskListCreateView.as_view()
        response = view(request)
        self.assertEqual(response.status_code, 201)
        self.assertEqual(Task.objects.count(), 2)  # Asegurar que se ha creado una nueva tarea

    def test_task_list_view_with_filter(self):
        # Prueba para verificar que la vista devuelve una lista filtrada de tareas
        request = self.factory.get('/tasks/', {'completed': 'true'})
        view = TaskListCreateView.as_view()
        response = view(request)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.data), 0)  # Asegurar que no hay tareas completadas en la respuesta

"""