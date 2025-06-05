from django.db import models

# Create your models here.
class Monumento(models.Model):
    nombre = models.CharField(max_length=100)
    ubicacion = models.CharField(max_length=200)
    descripcion = models.TextField(blank=True, null=True)
    imagen = models.ImageField(upload_to='monumentos/', blank=True, null=True)

class VisitaGuiada(models.Model):
    monumento = models.ForeignKey(Monumento, on_delete=models.CASCADE, related_name='visitas')
    fecha = models.DateField()
    guia = models.CharField(max_length=100)
    duracion_minutos = models.PositiveIntegerField()
    observaciones = models.TextField(blank=True, null=True)