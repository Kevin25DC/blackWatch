from django.db import models
from django.contrib.auth.models import User

class Rol(models.Model):
    nombre = models.CharField(max_length=50, unique=True)
    descripcion = models.TextField()

    def __str__(self):
        return self.nombre

class Usuario(models.Model):
    TIPO_IDENTIFICACION_OPCIONES = [
        ('Cedula de Ciudadanía', 'Cedula de Ciudadanía'),
        ('Cedula de Extranjería', 'Cedula de Extranjería'),
        ('Pasaporte', 'Pasaporte'),
    ]

    usuario = models.OneToOneField(User, on_delete=models.CASCADE, default=1)
    nombre = models.CharField(max_length=100, verbose_name='Nombre del usuario')
    apellidos = models.CharField(max_length=100)
    correo_electronico = models.EmailField()
    telefono = models.CharField(max_length=15)
    direccion = models.CharField(max_length=200)
    tipo_identificacion = models.CharField(max_length=100, choices=TIPO_IDENTIFICACION_OPCIONES, null=False, blank=False, default='')
    numero_identificacion = models.CharField(max_length=100)
    roles = models.ManyToManyField(Rol)

    def __str__(self):
        return f"{self.nombre} {self.apellidos}"
    



