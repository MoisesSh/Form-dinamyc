from django.db import models



class ConsejoDirectivo(models.Model):
    id = models.BigAutoField(primary_key=True)
    nombre_completo = models.CharField(max_length=255, blank=True, null=True)
    cargo = models.CharField(max_length=255, blank=True, null=True)
    decreto = models.TextField(blank=True, null=True)
    C_I = models.CharField(max_length=20, blank=True, null=True)
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    fecha_modificacion = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=True)
    fecha_fin = models.DateField(blank=True, null=True)
    fecha_inicio = models.DateField(blank=True, null=True)
    firma = models.FileField(upload_to='firmas/', blank=True, null=True)
    sello = models.FileField(upload_to='sellos/', blank=True, null=True)
    gaceta_nro = models.CharField(max_length=20, blank=True, null=True)
    gaceta_fecha = models.DateField(blank=True, null=True)
    