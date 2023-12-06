from rest_framework.serializers import ModelSerializer, SlugRelatedField
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework import serializers
from .models import Usuario


class UsuarioSerializer(ModelSerializer):
    class Meta:
        model = Usuario
        fields = "__all__"

class CustomTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super(CustomTokenObtainPairSerializer, cls).get_token(user)

        # Adicione informações do usuário aqui
        token['email'] = user.email
        token['tipo_usuario'] = user.tipo_usuario
        # Inclua outras informações do usuário conforme necessário

        return token

    def validate(self, attrs):
        data = super().validate(attrs)
        refresh = self.get_token(self.user)

        data['refresh'] = str(refresh)
        data['access'] = str(refresh.access_token)

        # Informações do usuário
        user_data = UsuarioSerializer(self.user).data
        data['user'] = user_data

        return data