from django.db import models

class AnalistaSolicitud(models.Model):
    id = models.BigIntegerField(blank=True, null=True)
    id_solicitud = models.BigIntegerField(primary_key=True)
    id_user = models.BigIntegerField(blank=True, null=True)
    fecha_reg = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = '"analisis"."analista_solicitud"'



class Categoria(models.Model):
    id = models.BigAutoField(primary_key=True)
    nombre = models.CharField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = '"analisis"."categoria"'



class ObservacionEquipo(models.Model):
    id = models.BigAutoField(primary_key=True)
    id_equipo = models.BigIntegerField(blank=True, null=True)
    id_user_analista = models.BigIntegerField(blank=True, null=True)
    observacion = models.CharField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = '"analisis"."observacion_equipo"'



class SubCategoria(models.Model):
    id = models.BigAutoField(primary_key=True)
    nombre = models.CharField(blank=True, null=True)
    id_categoria = models.ForeignKey(Categoria, models.DO_NOTHING, db_column='id_categoria', blank=True, null=True)

    class Meta:
        managed = False
        db_table = '"analisis"."sub_categoria"'
