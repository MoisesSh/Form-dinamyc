from django.db import models


class Equipo(models.Model):
    id = models.BigAutoField(primary_key=True)
    cod_equipo = models.CharField(blank=True, null=True)
    id_solicitud = models.BigIntegerField(blank=True, null=True)
    marca = models.CharField(blank=True, null=True)
    modelo = models.CharField(blank=True, null=True)
    cert_ext = models.IntegerField(blank=True, null=True)
    paises = models.JSONField(blank=True, null=True)
    ia = models.IntegerField(blank=True, null=True)
    categoria = models.JSONField(blank=True, null=True)
    sub_categoria = models.JSONField(blank=True, null=True)
    aprobado = models.IntegerField(blank=True, null=True)
    foto = models.CharField(blank=True, null=True)
    fecha_mod = models.DateTimeField(blank=True, null=True)
    archivo_pdf = models.CharField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tecnico\".\"equipo'

    def __str__(self):
        return f'{self.marca} {self.modelo} ({self.cod_equipo})'


class EquipoHist(models.Model):
    id = models.BigAutoField(primary_key=True)
    cod_equipo = models.CharField()
    marca = models.CharField()
    modelo = models.CharField()
    norma = models.CharField(blank=True, null=True)
    categoria = models.CharField(blank=True, null=True)
    sub_categoria = models.CharField(blank=True, null=True)
    fecha_aprob = models.DateField(blank=True, null=True)
    aprobacion = models.CharField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tecnico\".\"equipo_hist'

    def __str__(self):
        return f'{self.marca} {self.modelo} ({self.cod_equipo})'


class Marca(models.Model):
    id = models.BigAutoField(primary_key=True)
    nombre = models.CharField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tecnico\".\"marca'

    def __str__(self):
        return self.nombre or f'Marca #{self.pk}'


class Modelo(models.Model):
    id = models.BigAutoField(primary_key=True)
    nombre = models.CharField(blank=True, null=True)
    marca = models.ForeignKey(
        Marca, models.DO_NOTHING,
        db_column='id_marca', blank=True, null=True,
        related_name='modelos',
    )

    class Meta:
        managed = False
        db_table = 'tecnico\".\"modelo'

    def __str__(self):
        return self.nombre or f'Modelo #{self.pk}'


class Organismo(models.Model):
    id = models.BigAutoField(primary_key=True)
    nombre = models.CharField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tecnico\".\"organismo'

    def __str__(self):
        return self.nombre or f'Organismo #{self.pk}'


class CertExt(models.Model):
    id = models.BigAutoField(primary_key=True)
    cod_cert = models.CharField(blank=True, null=True)
    organismo = models.ForeignKey(
        Organismo, models.DO_NOTHING,
        db_column='id_organismo', blank=True, null=True,
        related_name='certificaciones',
    )
    acreditado = models.CharField(blank=True, null=True)
    id_pais = models.BigIntegerField(blank=True, null=True)
    fecha_emision = models.DateField(blank=True, null=True)
    equipo = models.ForeignKey(
        Equipo, models.DO_NOTHING,
        db_column='id_equipo', blank=True, null=True,
        related_name='certificaciones_externas',
    )
    cert_doc = models.CharField(blank=True, null=True)
    asunto = models.CharField(blank=True, null=True)
    otro = models.CharField(blank=True, null=True)
    archivo_pdf = models.CharField(max_length=500, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tecnico\".\"cert_ext'

    def __str__(self):
        return self.cod_cert or f'CertExt #{self.pk}'


class Evaluaciones(models.Model):
    id = models.BigAutoField(primary_key=True)
    equipo = models.ForeignKey(
        Equipo, models.DO_NOTHING,
        db_column='id_equipo', blank=True, null=True,
        related_name='evaluaciones',
    )
    cod_informe = models.CharField(blank=True, null=True)
    norma = models.CharField(blank=True, null=True)
    nom_laboratorio = models.CharField(blank=True, null=True)
    id_pais = models.BigIntegerField(blank=True, null=True)
    informe_doc = models.CharField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tecnico\".\"evaluaciones'

    def __str__(self):
        return self.cod_informe or f'Evaluación #{self.pk}'


class InterfazAlam(models.Model):
    id = models.BigAutoField(primary_key=True)
    equipo = models.ForeignKey(
        Equipo, models.DO_NOTHING,
        db_column='id_equipo', blank=True, null=True,
        related_name='interfaces_alambricas',
    )
    impedancia = models.CharField(blank=True, null=True)
    ancho_banda = models.CharField(blank=True, null=True)
    tipo_modulacion = models.CharField(blank=True, null=True)
    protocolos_trans = models.CharField(blank=True, null=True)
    protocolos_sennal = models.CharField(blank=True, null=True)
    medio_trans = models.CharField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tecnico\".\"interfaz_alam'

    def __str__(self):
        return f'InterfazAlam equipo #{self.equipo_id}'


class ParametroRecep(models.Model):
    id = models.BigAutoField(primary_key=True)
    equipo = models.ForeignKey(
        Equipo, models.DO_NOTHING,
        db_column='id_equipo', blank=True, null=True,
        related_name='parametros_recepcion',
    )
    banda_limit_inf = models.CharField(blank=True, null=True)
    banda_limit_sup = models.CharField(blank=True, null=True)
    ganancia = models.CharField(blank=True, null=True)
    sensibilidad = models.CharField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tecnico\".\"parametro_recep'

    def __str__(self):
        return f'ParamRecep equipo #{self.equipo_id}'


class ParametroTran(models.Model):
    id = models.BigAutoField(primary_key=True)
    equipo = models.ForeignKey(
        Equipo, models.DO_NOTHING,
        db_column='id_equipo', blank=True, null=True,
        related_name='parametros_transmision',
    )
    tipo_modula = models.CharField(blank=True, null=True)
    tecn_acceso = models.CharField(blank=True, null=True)
    banda_limit_inf = models.CharField(blank=True, null=True)
    banda_limit_sup = models.CharField(blank=True, null=True)
    ancho_banda_canal = models.CharField(blank=True, null=True)
    potencia = models.CharField(blank=True, null=True)
    ganancia = models.CharField(blank=True, null=True)
    pire = models.CharField(blank=True, null=True)
    clase_emision = models.CharField(blank=True, null=True)
    capacidad = models.CharField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tecnico\".\"parametro_tran'

    def __str__(self):
        return f'ParamTran equipo #{self.equipo_id}'
