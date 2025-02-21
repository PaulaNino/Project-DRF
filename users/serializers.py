from rest_framework import serializers
from .models import User
from datetime import date
from rest_framework import serializers
from rest_framework_simplejwt.tokens import RefreshToken
from django.utils import timezone
import re



class UserLoginSerializer(serializers.Serializer):
    email = serializers.EmailField(max_length=255, required=True)
    password = serializers.CharField(max_length=255, required=True)

    def validate(self, data):
        email = data.get('email')
        password = data.get('password')


        #ORM para validar que el usuario ingresado este en la bd
        try:
            user = User.objects.get(email=email)
        except User.DoesNotExist:
            raise serializers.ValidationError({'email': 'El email no está registrado.'})

        if not user.is_active:
            raise serializers.ValidationError({'email': 'El usuario está inactivo.'})

        if not user.check_password(password):
            raise serializers.ValidationError({'password': 'La contraseña es incorrecta.'})

        return data





class UserSerializer(serializers.ModelSerializer):
    """
    Serializador para los usuarios
    No es necesario pasar todos los campos
    Podemos aplicar el exclude o poner uno por uno los que 
    deseamos poner en el serealizador
    """

    class Meta:
        model = User
        fields = '__all__'
 