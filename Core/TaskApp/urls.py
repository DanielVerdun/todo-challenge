
# En este archivo es indispensable importar la siguientes librerias
from rest_framework import routers

from TaskApp.viewsets import TaskViewSet
#from rest_framework.routers import DefaultRouter

router = routers.SimpleRouter() # Define las rutas para nuestro modelo. GET,POST,PUT,DELETE
router.register('tasks', TaskViewSet) # registramos la url y recibe el ViewSet como segundo parámetro

urlpatterns = router.urls

