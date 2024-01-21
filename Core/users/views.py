from rest_framework import generics, authentication, permissions
#from users.models import User # importamos model
from users.serializers import UserSerializer, AuthTokenSerializer# importamos serializer

from rest_framework.authtoken.views import ObtainAuthToken # importamos para autenticar

# Clase para crear usuarios desde endpoint
class CreateUserView(generics.CreateAPIView):
    serializer_class = UserSerializer

# Clase para ver y actualizar informacion del usuario: Debe estar autenticado
class RetreiveUpdateUserView(generics.RetrieveUpdateAPIView):
    serializer_class = UserSerializer
    authentication_classes = [authentication.TokenAuthentication]
    permission_classes = [permissions.IsAuthenticated]

    def get_object(self):
        return self.request.user

class CreateTokenView(ObtainAuthToken):
    """Vista para crear un token"""
    serializer_class = AuthTokenSerializer