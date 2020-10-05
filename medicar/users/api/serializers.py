from django.contrib.auth.hashers import make_password
from rest_framework.exceptions import ValidationError
from rest_framework.serializers import ModelSerializer
from medicar.users.models import UsuarioCustomizado


class UserRegistrationSerializer(ModelSerializer):
    class Meta:
        model = UsuarioCustomizado
        fields = ('email', 'name', 'password', 're_password')

    def create(self, validated_data):
        if validated_data['password'] != validated_data['re_password']:
            raise ValidationError("Senha e confirmar senha devem ser iguais!")
        user = UsuarioCustomizado(
            email=validated_data['email'],
            name=validated_data['name'],
            password=make_password(validated_data['password']),
            re_password=make_password(validated_data['re_password'])
        )
        user.save()
        return user
