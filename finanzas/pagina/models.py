from django.db import models
from django.core.exceptions import ValidationError

# Todo crear una tabla para el login

class Usuario(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=20)
    contraseña = models.CharField(max_length=20, default='contradefault')  # NO BORRAR NO PUEDO HACER LAS MIGRACIONES SIN ESO XDDD
    perfil = models.ForeignKey('QuizIn', on_delete=models.CASCADE, related_name='usuarios')

class Perfiles(models.Model):
    id = models.AutoField(primary_key=True)
    tipo_perfil = models.CharField(max_length=50)
    puntaje_min = models.IntegerField()
    puntaje_max = models.IntegerField()

    def clean(self):
        if self.puntaje_min > self.puntaje_max:
            raise ValidationError("ta mal el puntake")

class QuizIn(models.Model):
    id = models.AutoField(primary_key=True)
    id_us = models.ForeignKey('Usuario', on_delete=models.CASCADE, related_name='losquiz')
    puntaje = models.ForeignKey(Perfiles, on_delete=models.CASCADE, related_name='quiz_resultados')
    valor_puntaje = models.IntegerField()
    
    @property
    def tipo_perfil(self):
        return self.puntaje.tipo_perfil

    def clean(self):
        if self.puntaje and self.valor_puntaje:
            if not (self.puntaje.puntaje_min <= self.valor_puntaje <= self.puntaje.puntaje_max):
                raise ValidationError(
                    f"El puntaje debe estar entre {self.puntaje.puntaje_min} y {self.puntaje.puntaje_max} lo pusiste mal 2"
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