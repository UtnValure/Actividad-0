from django.db import models

class.pregunta(models.Model):
    pregunta = models.charField(max_lenght=200)
    pub_date = models.DateTimeField('fecha de publicacion')

class.opcion(models.Model):
    pregunta = models.ForeignKey(pregunta, on_delete=models.CASCADE)
    opcion = models.CharField(max_lenght=200)
    votos = models.IntegerField(default=0)
