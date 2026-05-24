from django.db import models

class Banco(models.Model):
    id = models.BigAutoField(primary_key=True)
    nombre = models.CharField(blank=True, null=True)
    codigo = models.CharField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = '"recaudacion"."banco"'



class Pago(models.Model):
    id = models.BigAutoField(primary_key=True)
    ci_rif = models.CharField(blank=True, null=True)
    tlf = models.CharField(blank=True, null=True)
    id_banco = models.ForeignKey(Banco, models.DO_NOTHING, db_column='id_banco', blank=True, null=True)
    nro_referencia = models.CharField(blank=True, null=True)
    monto = models.DecimalField(max_digits=20, decimal_places=2, blank=True, null=True)
    fecha = models.DateTimeField(blank=True, null=True)
    id_solicitud = models.BigIntegerField(blank=True, null=True)
    id_transaccion = models.ForeignKey('Transaccion', models.DO_NOTHING, db_column='id_transaccion', blank=True, null=True)

    class Meta:
        managed = False
        db_table = '"recaudacion"."pago"'



class TasaTrans(models.Model):
    id = models.BigAutoField(primary_key=True)
    cantidad = models.IntegerField(blank=True, null=True)
    id_tipo_solicitud = models.BigIntegerField(blank=True, null=True)
    cant_equipo = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = '"recaudacion"."tasa_trans"'



class TasaUt(models.Model):
    id = models.BigAutoField(primary_key=True)
    valor = models.DecimalField(max_digits=20, decimal_places=2, blank=True, null=True)
    estatus = models.IntegerField(blank=True, null=True)
    fecha = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = '"recaudacion"."tasa_ut"'



class Transaccion(models.Model):
    id = models.BigAutoField(primary_key=True)
    nombre = models.CharField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = '"recaudacion"."transaccion"'



class TrazaPago(models.Model):
    id = models.BigAutoField(primary_key=True)
    msj = models.CharField(blank=True, null=True)
    id_solicitud = models.BigIntegerField(blank=True, null=True)
    fecha = models.DateTimeField(blank=True, null=True)
    id_pago = models.ForeignKey(Pago, models.DO_NOTHING, db_column='id_pago', blank=True, null=True)

    class Meta:
        managed = False
        db_table = '"recaudacion"."traza_pago"'
