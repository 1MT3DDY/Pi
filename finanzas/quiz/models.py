from django.db import models

# Create your models here.

class preguntas(models.Model):
    id_pregunta = models.AutoField(primary_key=True)
    pregunta = models.CharField() #texto de la pregunta
    respuesta_1 = 0 #valores respuestas
    respuesta_2 = 5
    respuesta_3 = 10

    def __str__(self): #recuerden que esto es para q cuando lo veamos en el admin, devuelva el id de la pregunta
        return str(self.id_pregunta)