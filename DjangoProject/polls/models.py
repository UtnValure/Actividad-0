from django.db import models
from django.utils import timezone

class pregunta(models.Model):
    pregunta = models.CharField(max_length=200)
    pub_date = models.DateTimeField('fecha de publicacion')
    def __str__(self):
        return self.pregunta
    def fue_publicada_recientemente(self):
        return self.pub_date >= timezone.now() - timezone.timedelta(days=1)

class opcion(models.Model):
    pregunta = models.ForeignKey(pregunta, on_delete=models.CASCADE)
    opcion = models.CharField(max_length=200)
    votos = models.IntegerField(default=0)
    def __str__ (self):
        return self.opcion