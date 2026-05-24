from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    # Deshabilitar username
    username = None
    
    # Usamos email como nombre de usuario principal
    identificacion = models.CharField(max_length=20, unique=True, verbose_name='Cédula, DNI o RIF')
    email = models.EmailField(unique=True)
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)



    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['identificacion', 'first_name', 'last_name']

    class Meta:

        db_table = 'customuser'


    def __str__(self):
        return f"{self.identificacion} - {self.email}"
