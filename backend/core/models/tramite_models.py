from django.db import models

class CertificacionPendiente(models.Model):
    id = models.BigAutoField(primary_key=True)
    id_solicitud = models.BigIntegerField()
    id_equipo = models.BigIntegerField(blank=True, null=True)
    id_equipo_hist = models.BigIntegerField(blank=True, null=True)
    tipo_equipo = models.CharField(max_length=20)
    cod_oficial = models.CharField(max_length=255, blank=True, null=True)
    fecha_creacion = models.DateTimeField()
    fecha_modificacion = models.DateTimeField()
    is_active = models.BooleanField()

    class Meta:
        managed = False
        db_table = '"tramite"."certificacion_pendiente"'
        unique_together = (('id_solicitud', 'id_equipo', 'id_equipo_hist'), ('id_solicitud', 'id_equipo', 'id_equipo_hist'),)



class ColaAsignacion(models.Model):
    id = models.BigAutoField(primary_key=True)
    fecha_ingreso = models.DateTimeField()
    fecha_asignacion = models.DateTimeField(blank=True, null=True)
    estado = models.BooleanField()
    intentos = models.IntegerField()
    error_message = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    evaluador_asignado_id = models.BigIntegerField(blank=True, null=True)
    solicitud = models.OneToOneField('Solicitud', models.DO_NOTHING)
    prioridad = models.CharField(max_length=20, blank=True, null=True)
    evaluadores_disponibles_count = models.IntegerField(blank=True, null=True)
    solicitudes_en_cola_count = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = '"tramite"."cola_asignacion"'



class DocumentoSolicitante(models.Model):
    id = models.BigAutoField(primary_key=True)
    id_solicitante = models.BigIntegerField()
    tipo_documento = models.CharField(max_length=20)
    archivo = models.CharField(max_length=100)
    nombre_archivo = models.CharField(max_length=255)
    tamaño_archivo = models.BigIntegerField()
    fecha_subida = models.DateTimeField()
    fecha_modificacion = models.DateTimeField()
    is_active = models.BooleanField()

    class Meta:
        managed = False
        db_table = '"tramite"."documento_solicitante"'
        unique_together = (('id_solicitante', 'tipo_documento'),)



class Estado(models.Model):
    id = models.BigAutoField(primary_key=True)
    nombre = models.CharField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = '"tramite"."estado"'



class Fabricante(models.Model):
    id = models.BigAutoField(primary_key=True)
    nombre = models.CharField(blank=True, null=True)
    direccion = models.CharField(blank=True, null=True)
    id_pais = models.BigIntegerField(blank=True, null=True)
    cod_postal = models.CharField(blank=True, null=True)
    tlf = models.CharField(blank=True, null=True)
    correo = models.CharField(blank=True, null=True)
    nombre_cont = models.CharField(blank=True, null=True)
    tlf_cont = models.CharField(blank=True, null=True)
    correo_cont = models.CharField(blank=True, null=True)
    id_equipo = models.BigIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = '"tramite"."fabricante"'



class Municipio(models.Model):
    id = models.BigAutoField(primary_key=True)
    nombre = models.CharField(blank=True, null=True)
    id_estado = models.ForeignKey(Estado, models.DO_NOTHING, db_column='id_estado', blank=True, null=True)

    class Meta:
        managed = False
        db_table = '"tramite"."municipio"'



class ObservacionSolicitud(models.Model):
    id = models.BigAutoField(primary_key=True)
    id_solicitud = models.BigIntegerField()
    id_user = models.BigIntegerField()
    etapa = models.CharField(max_length=50)
    observacion = models.TextField(blank=True, null=True)
    fecha_creacion = models.DateTimeField()
    fecha_modificacion = models.DateTimeField()
    is_active = models.BooleanField()

    class Meta:
        managed = False
        db_table = '"tramite"."observacion_solicitud"'



class Pais(models.Model):
    id = models.BigAutoField(primary_key=True)
    nombre = models.CharField(blank=True, null=True)
    cod_tlf = models.CharField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = '"tramite"."pais"'



class Parroquia(models.Model):
    id = models.BigAutoField(primary_key=True)
    nombre = models.CharField(blank=True, null=True)
    id_municipio = models.ForeignKey(Municipio, models.DO_NOTHING, db_column='id_municipio', blank=True, null=True)

    class Meta:
        managed = False
        db_table = '"tramite"."parroquia"'



class Solicitante(models.Model):
    razon_social = models.CharField(blank=True, null=True)
    id_tipo_solicitante = models.ForeignKey('TipoSolicitante', models.DO_NOTHING, db_column='id_tipo_solicitante', blank=True, null=True)
    id_estado = models.ForeignKey(Estado, models.DO_NOTHING, db_column='id_estado', blank=True, null=True)
    id_municipio = models.ForeignKey(Municipio, models.DO_NOTHING, db_column='id_municipio', blank=True, null=True)
    id_parroquia = models.ForeignKey(Parroquia, models.DO_NOTHING, db_column='id_parroquia', blank=True, null=True)
    direccion = models.CharField(blank=True, null=True)
    cod_postal = models.CharField(blank=True, null=True)
    tlf = models.CharField(blank=True, null=True)
    correo = models.CharField(blank=True, null=True)
    documento = models.CharField(blank=True, null=True)
    nombre_contacto = models.CharField(blank=True, null=True)
    tlf_cont = models.CharField(blank=True, null=True)
    correo_cont = models.CharField(blank=True, null=True)
    fecha_reg = models.DateTimeField(blank=True, null=True)
    fecha_mod = models.DateTimeField(blank=True, null=True)
    archivo_documento = models.CharField(blank=True, null=True)
    id_user = models.BigIntegerField(blank=True, null=True)
    id = models.BigAutoField(primary_key=True)

    class Meta:
        managed = False
        db_table = '"tramite"."solicitante"'



class Solicitud(models.Model):
    cod_solicitud = models.CharField(blank=True, null=True)
    id_solicitante = models.ForeignKey(Solicitante, models.DO_NOTHING, db_column='id_solicitante', blank=True, null=True)
    fecha_reg = models.DateTimeField(blank=True, null=True)
    fecha_mod = models.DateTimeField(blank=True, null=True)
    id_estatus_int = models.IntegerField(blank=True, null=True)
    id_estatus_ext = models.IntegerField(blank=True, null=True)
    id_tipo_solicitud = models.ForeignKey('TipoSolicitud', models.DO_NOTHING, db_column='id_tipo_solicitud', blank=True, null=True)
    id = models.BigAutoField(primary_key=True)
    id_aprobador = models.BigIntegerField(blank=True, null=True)
    id_confirmador = models.BigIntegerField(blank=True, null=True)
    id_evaluador = models.BigIntegerField(blank=True, null=True)
    paso_actual = models.IntegerField(blank=True, null=True)
    is_activate = models.BooleanField(blank=True, null=True)
    fecha_asignacion_confirmador = models.DateTimeField(blank=True, null=True)
    fecha_finalizacion_confirmador = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = '"tramite"."solicitud"'



class TipoSolicitante(models.Model):
    id = models.BigAutoField(primary_key=True)
    nombre = models.CharField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = '"tramite"."tipo_solicitante"'



class TipoSolicitud(models.Model):
    id = models.BigAutoField(primary_key=True)
    nombre = models.CharField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = '"tramite"."tipo_solicitud"'
