from dj_rest_auth.registration.serializers import RegisterSerializer
from dj_rest_auth.serializers import LoginSerializer
from rest_framework import serializers
from django.contrib.auth import authenticate
from django.contrib.auth import get_user_model



User = get_user_model()

class CustomRegisterSerializer(RegisterSerializer):

    identificacion = serializers.CharField(max_length=20, required=True)
    first_name = serializers.CharField(max_length=150, required=True)
    last_name = serializers.CharField(max_length=150, required=True)
    username = None

    def validate_email(self, value):

        email = value.lower()
        if User.objects.filter(email=email).exists():
            raise serializers.ValidationError(
                "Ya existe un usuario registrado con este correo electrónico."
            )
        return email

    def validate_identificacion(self, value):
        if not value or not value.strip():
            raise serializers.ValidationError(
                "La identificación es requerida."
            )
        if User.objects.filter(identificacion=value).exists():
            raise serializers.ValidationError(
                "Ya existe un usuario registrado con esta identificación."
            )
        return value

    def get_cleaned_data(self):
        data = super().get_cleaned_data()
        data['identificacion'] = self.validated_data.get('identificacion', '')
        data['first_name'] = self.validated_data.get('first_name', '')
        data['last_name'] = self.validated_data.get('last_name', '')
        data.pop('username', None)
        return data

    def save(self, request):
        cleaned_data = self.get_cleaned_data()
        user = User(
            email=cleaned_data['email'],
            identificacion=cleaned_data['identificacion'],
            first_name=cleaned_data.get('first_name', ''),
            last_name=cleaned_data.get('last_name', ''),
        )
        user.set_password(cleaned_data['password1'])
        user.save()
        return user



class CustomLoginSerializer(LoginSerializer):
    username = None

    def validate(self, attrs):
        email = attrs.get('email')
        password = attrs.get('password')

        if email and password:
        
            user = User.objects.filter(email=email).first()
            if user and user.check_password(password):
                attrs['user'] = user
            else:
                raise serializers.ValidationError(
                    'No se puede iniciar sesión con las credenciales proporcionadas'
                )
        else:
            raise serializers.ValidationError(
                'Debe incluir "correo electrónico" y "contraseña".'
            )

        return attrs