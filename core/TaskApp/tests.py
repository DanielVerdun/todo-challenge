from rest_framework.test import APITestCase
from rest_framework import status
from django.contrib.auth import get_user_model
from TaskApp.models import Task

User = get_user_model()


class TaskAPITestCase(APITestCase):

    def setUp(self):
        # Crear usuario de prueba
        self.user = User.objects.create_user(

            email="user_test@gmail.com",
            password="123456"
        )
        # Obtener token de autenticación
        response = self.client.post(
            "/api/v1.0/authentication/token/",
            {"email": "user_test@gmail.com", "password": "123456"},
            format="json"
        )
        self.token = response.data.get("token")
        self.client.credentials(HTTP_AUTHORIZATION=f"Token {self.token}")

        # Crear tarea inicial para pruebas GET/PUT/DELETE
        self.task = Task.objects.create(
            title="Tarea inicial",
            description="Descripción inicial",
            completed=False,
            created_at="2024-01-23T00:06:31Z"
        )

    def test_get_tasks(self):
        response = self.client.get("/api/v1.0/tasks/")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn("title", response.data[0])

    def test_create_task(self):
        data = {
            "title": "Tarea_testing",
            "description": "Descripción de la tarea testing",
            "completed": True,
        }
        response = self.client.post("/api/v1.0/tasks/", data, format="json")
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data["title"], "Tarea_testing")

    def test_filter_task(self):
        created_date = self.task.created_at.date()
        response = self.client.get(f"/api/v1.0/tasks/?created_at_after={created_date}&created_at_before={created_date}&description={self.task.description}")
        self.assertGreaterEqual(len(response.data), 1)

    def test_update_task(self):
        data = {
            "title": "Tarea modificada",
            "description": "Descripción modificada",
            "completed": True,
        }
        response = self.client.put(f"/api/v1.0/tasks/{self.task.id}/", data, format="json")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["title"], "Tarea modificada")

    def test_delete_task(self):
        response = self.client.delete(f"/api/v1.0/tasks/{self.task.id}/")
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertFalse(Task.objects.filter(id=self.task.id).exists())
