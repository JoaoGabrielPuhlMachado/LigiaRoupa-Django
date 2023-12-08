from rest_framework import serializers
from rest_framework.serializers import ModelSerializer, SlugRelatedField
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from django.contrib.auth.models import Group

from uploader.models import Image
from uploader.serializers import ImageSerializer

from .models import Usuario


class GroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = Group
        fields = ['id', 'name']

class UsuarioSerializer(ModelSerializer):
    foto_attachment_key = SlugRelatedField(
        source="foto",
        queryset=Image.objects.all(),
        slug_field="attachment_key",
        required=False,
        write_only=True,
    )
    foto = ImageSerializer(required=False, read_only=True)
    grupos = GroupSerializer(many=True, read_only=True)  # Adicione esta linha para serializar os grupos

    class Meta:
        model = Usuario
        fields = "__all__"



class CustomTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super(CustomTokenObtainPairSerializer, cls).get_token(user)

        # Adicione informações do usuário aqui
        token["email"] = user.email
        token["tipo_usuario"] = user.tipo_usuario

        return token

    def validate(self, attrs):
        data = super().validate(attrs)
        refresh = self.get_token(self.user)

        data["refresh"] = str(refresh)
        data["access"] = str(refresh.access_token)

        # Informações do usuário
        user_data = UsuarioSerializer(self.user).data
        data["user"] = user_data

        return data
