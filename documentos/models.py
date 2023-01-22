from django.db import models

# Create your models here.
class docAnalisisModel(models.Model):
    usuario = models.CharField(null=False, max_length=75, default="")
    nombre = models.CharField(null=False, max_length=75, default="")
    objetivo = models.CharField(null=False, max_length=500, default="")
    identificador = models.CharField(null=False, max_length=30, default="")
    ind_met = models.CharField(null=False, max_length=500, default="")
    des_actividades = models.CharField(null=False, max_length=750, default="")
    diagrama_flujo = models.ImageField(upload_to="diagramas_flujo", null=False)
    categoria = models.CharField(null=False, max_length=75, default="")
    salida = models.CharField(null=False, max_length=500, default="")
    frecuencia = models.CharField(null=False, max_length=100, default="")
    introE = models.CharField(null=False, max_length=500, default="")
    alcanceE = models.CharField(null=False, max_length=500, default="")
    objetivosE = models.CharField(null=False, max_length=500, default="")
    arq1 = models.ImageField(upload_to="arquitectura", null=True, blank=True)
    arq2 = models.ImageField(upload_to="arquitectura", null=True, blank=True)
    arq3 = models.ImageField(upload_to="arquitectura", null=True, blank=True)
    comp1 = models.ImageField(upload_to="componentes", null=True, blank=True)
    comp2 = models.ImageField(upload_to="componentes", null=True, blank=True)
    comp3 = models.ImageField(upload_to="componentes", null=True, blank=True)
    des_componentesE = models.CharField(null=False, max_length=500, default="")