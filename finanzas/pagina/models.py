from django.db import models
from django.core.exceptions import ValidationError

# Todo crear una tabla para el login

class Usuario(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=20)
    contraseña = models.CharField(max_length=20, default='contradefault') # NO BORRAR NO PUEDO HACER LAS MIGRACIONES SIN ESO XDDD
    perfil = models.ForeignKey('QuizIn', on_delete=models.CASCADE, related_name='usuarios', null=True, blank=True)

class QuizIn(models.Model):
    id = models.AutoField(primary_key=True)
    id_us = models.ForeignKey('Usuario', on_delete=models.CASCADE, related_name='losquiz')
    puntaje = models.IntegerField()
    
    def clean(self):
        if self.puntaje:
            if not (0 <= self.puntaje <= 100):  # Asumimos un rango válido de 0 a 100
                raise ValidationError(
                    f"El puntaje debe estar entre 0 y 100"
                )

class Login(models.Model):
    id = models.AutoField(primary_key=True)
    nombre_usuario = models.CharField(max_length=20)
    contraseña_usuario = models.CharField(max_length=20)
    fecha_login = models.DateTimeField(auto_now_add=True)
    
    def clean(self):
        try:
            usuario = Usuario.objects.get(nombre=self.nombre_usuario)
            if usuario.contraseña != self.contraseña_usuario:
                raise ValidationError("Contraseña incorrecta")
        except Usuario.DoesNotExist:
            raise ValidationError("Usuario no encontrado")