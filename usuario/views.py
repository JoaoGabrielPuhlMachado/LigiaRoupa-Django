from rest_framework.viewsets import ModelViewSet

from .models import Usuario
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework.response import Response
from .serializers import UsuarioSerializer
from .serializers import CustomTokenObtainPairSerializer

class UsuarioViewSet(ModelViewSet):
    queryset = Usuario.objects.all()
    serializer_class = UsuarioSerializer

# Em seu arquivo views.py

# views.py


class CustomTokenObtainPairView(TokenObtainPairView):
    serializer_class = CustomTokenObtainPairSerializer