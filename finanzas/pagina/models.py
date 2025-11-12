from django.db import models
from django.core.exceptions import ValidationError

# Todo crear una tabla para el login

class Perfil(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=50)
    descripcion = models.TextField(blank=True)

    def __str__(self):
        return f"{self.id} - {self.nombre}"

class Usuario(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=20)
    contraseña = models.CharField(max_length=20, default='contradefault') # NO BORRAR NO PUEDO HACER LAS MIGRACIONES SIN ESO XDDD
    perfil = models.ForeignKey('Perfil', on_delete=models.SET_NULL, related_name='usuarios', null=True, blank=True)
    score = models.IntegerField(default=0)

    def __str__(self):
        return f"{self.nombre} id: {self.id}"

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
    # esta parte trabaja los nombres de los perfiles en base al puntaje
    tipo_perfil = models.CharField(max_length=20, null=True, blank=True)

    def proceseishon_tipo_perfil(self):
        """Calcula la categoría textual según el puntaje numérico."""
        if self.puntaje is None:
            return None
        p = self.puntaje
        if 0 <= p <= 33:
            return 'Conservador'
        if 34 <= p <= 66:
            return 'Normal'
        if 67 <= p <= 100:
            return 'Arriesgado'
        return None

    def save(self, *args, **kwargs):
        # no toquen aca, esto ya esta ready
        try:
            self.tipo_perfil = self.proceseishon_tipo_perfil()
        except Exception:
            self.tipo_perfil = None
        super().save(*args, **kwargs)
    
    def __str__(self):
        return f"Quiz {self.id} - usuario: {self.id_us.nombre if self.id_us else 'N/A'}"

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