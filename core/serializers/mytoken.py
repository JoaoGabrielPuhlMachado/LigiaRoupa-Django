from rest_framework_simplejwt.serializers import TokenObtainPairSerializer


class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)
        isAdmin = False
        for group in user.groups.all():
            if group.name == "Administradores":
                isAdmin = True
        token["isAdmin"] = isAdmin

        return token
