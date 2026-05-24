from django.db import models


class Certificado(models.Model):
    id = models.BigAutoField(primary_key=True)
    equipo = models.ForeignKey(
        'core.Equipo', models.DO_NOTHING,
        db_column='id_equipo', blank=True, null=True,
        db_constraint=False, related_name='certificados',
    )
    fecha_emision = models.DateTimeField(blank=True, null=True)
    fecha_venc = models.DateTimeField(blank=True, null=True)
    estatus = models.ForeignKey(
        'core.Estatus', models.DO_NOTHING,
        db_column='id_estatus', blank=True, null=True,
        db_constraint=False, related_name='certificados',
    )
    cod_oficial = models.CharField(blank=True, null=True)
    homologacion = models.ForeignKey(
        'Homologacion', models.DO_NOTHING,
        db_column='id_homologacion', blank=True, null=True,
        related_name='certificados',
    )
    id_equipo_hist = models.BigIntegerField(blank=True, null=True)
    qr_code_id = models.BigIntegerField(
        blank=True, null=True,
        db_comment='Código QR asociado al certificado',
    )
    qr_verification_url = models.CharField(
        max_length=200, blank=True, null=True,
        db_comment='URL para verificación del certificado mediante QR',
    )
    id_usuario = models.BigIntegerField(
        blank=True, null=True,
        db_comment='ID del usuario externo que posee este certificado',
    )
    id_solicitud = models.BigIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'acto\".\"certificado'

    def __str__(self):
        return self.cod_oficial or f'Certificado #{self.pk}'


class Director(models.Model):
    id = models.BigAutoField(primary_key=True)
    nombre = models.CharField(max_length=255, blank=True, null=True)
    cargo = models.CharField(max_length=255, blank=True, null=True)
    decreto = models.TextField(blank=True, null=True)
    ci = models.CharField(max_length=20, blank=True, null=True)
    fecha_creacion = models.DateTimeField(blank=True, null=True)
    fecha_modificacion = models.DateTimeField(blank=True, null=True)
    is_active = models.BooleanField()
    fecha_fin = models.DateField(blank=True, null=True)
    fecha_inicio = models.DateField(blank=True, null=True)
    firma = models.CharField(max_length=100, blank=True, null=True)
    sello = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'acto\".\"director'

    def __str__(self):
        return self.nombre or f'Director #{self.pk}'


class Homologacion(models.Model):
    id = models.BigAutoField(primary_key=True)
    fecha_emision = models.DateTimeField(blank=True, null=True)
    cod_homo = models.CharField(blank=True, null=True)
    id_solicitud = models.BigIntegerField()
    estatus = models.ForeignKey(
        'core.Estatus', models.DO_NOTHING,
        db_column='id_estatus', blank=True, null=True,
        db_constraint=False, related_name='homologaciones',
    )
    equipo = models.OneToOneField(
        'core.Equipo', models.DO_NOTHING,
        db_column='id_equipo', blank=True, null=True,
        db_constraint=False, related_name='homologacion',
        db_comment='ID del equipo específico para esta homologación',
    )

    class Meta:
        managed = False
        db_table = 'acto\".\"homologacion'

    def __str__(self):
        return self.cod_homo or f'Homologación #{self.pk}'
