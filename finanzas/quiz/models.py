from django.db import models

# Create your models here.

class preguntas(models.Model):
    id_pregunta = models.AutoField(primary_key=True)
    pregunta = models.CharField(max_length=500) #texto de la pregunta
    respuesta_1 = models.IntegerField(default=0)
    respuesta_2 = models.IntegerField(default=5)
    respuesta_3 = models.IntegerField(default=10)
    opcion_1 = models.CharField(max_length=500, blank=True)
    opcion_2 = models.CharField(max_length=500, blank=True)
    opcion_3 = models.CharField(max_length=500, blank=True)

    def __str__(self): #recuerden que esto es para q cuando lo veamos en el admin, devuelva el id de la pregunta
        return str(self.id_pregunta) + " " + self.pregunta