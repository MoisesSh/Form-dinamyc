from rest_framework import serializers

from core.models.tecnico_models import (
    Equipo, Marca, Organismo, CertExt, Evaluaciones,
    InterfazAlam, ParametroRecep, ParametroTran,
)
from core.models.acto_models import Homologacion, Certificado
from core.models.analisis_models import Categoria, SubCategoria


class MarcaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Marca
        fields = ['id', 'nombre']


class SubCategoriaSerializer(serializers.ModelSerializer):
    class Meta:
        model = SubCategoria
        fields = ['id', 'nombre']


class CategoriaSerializer(serializers.ModelSerializer):
    sub_categorias = SubCategoriaSerializer(
        many=True, read_only=True, source='subcategoria_set',
    )

    class Meta:
        model = Categoria
        fields = ['id', 'nombre', 'sub_categorias']


class OrganismoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Organismo
        fields = ['id', 'nombre']


class HomologacionSerializer(serializers.ModelSerializer):
    estatus_nombre = serializers.CharField(
        source='estatus.nombre', read_only=True, default=None,
    )

    class Meta:
        model = Homologacion
        fields = ['cod_homo', 'fecha_emision', 'estatus_nombre']


class CertificadoSerializer(serializers.ModelSerializer):
    estatus_nombre = serializers.CharField(
        source='estatus.nombre', read_only=True, default=None,
    )

    class Meta:
        model = Certificado
        fields = ['cod_oficial', 'fecha_emision', 'fecha_venc', 'estatus_nombre']


class ParametroTranSerializer(serializers.ModelSerializer):
    class Meta:
        model = ParametroTran
        fields = [
            'tipo_modula', 'tecn_acceso', 'banda_limit_inf',
            'banda_limit_sup', 'ancho_banda_canal', 'potencia',
            'ganancia', 'pire', 'clase_emision', 'capacidad',
        ]


class ParametroRecepSerializer(serializers.ModelSerializer):
    class Meta:
        model = ParametroRecep
        fields = ['banda_limit_inf', 'banda_limit_sup', 'ganancia', 'sensibilidad']


class InterfazAlamSerializer(serializers.ModelSerializer):
    class Meta:
        model = InterfazAlam
        fields = [
            'impedancia', 'ancho_banda', 'tipo_modulacion',
            'protocolos_trans', 'protocolos_sennal', 'medio_trans',
        ]


class EvaluacionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Evaluaciones
        fields = ['cod_informe', 'norma', 'nom_laboratorio', 'id_pais']


class CertExtSerializer(serializers.ModelSerializer):
    organismo_nombre = serializers.CharField(
        source='organismo.nombre', read_only=True, default=None,
    )

    class Meta:
        model = CertExt
        fields = [
            'cod_cert', 'acreditado', 'organismo_nombre',
            'id_pais', 'fecha_emision', 'asunto',
        ]


class EquipoHomologadoListSerializer(serializers.ModelSerializer):
    
    cod_homologacion = serializers.CharField(
        source='homologacion.cod_homo', read_only=True, default=None,
    )
    fecha_homologacion = serializers.DateTimeField(
        source='homologacion.fecha_emision', read_only=True, default=None,
    )
    estatus_homologacion = serializers.CharField(
        source='homologacion.estatus.nombre', read_only=True, default=None,
    )

    class Meta:
        model = Equipo
        fields = [
            'id', 'cod_equipo', 'marca', 'modelo', 'foto', 'paises',
            'cod_homologacion', 'fecha_homologacion', 'estatus_homologacion',
        ]


class EquipoHomologadoDetailSerializer(serializers.ModelSerializer):

    homologacion = HomologacionSerializer(read_only=True)
    certificados = CertificadoSerializer(many=True, read_only=True)
    parametros_transmision = ParametroTranSerializer(
        many=True, read_only=True,
    )
    parametros_recepcion = ParametroRecepSerializer(
        many=True, read_only=True,
    )
    interfaces_alambricas = InterfazAlamSerializer(
        many=True, read_only=True,
    )
    evaluaciones = EvaluacionSerializer(many=True, read_only=True)
    certificaciones_externas = CertExtSerializer(many=True, read_only=True)

    class Meta:
        model = Equipo
        fields = [
            'id', 'cod_equipo', 'marca', 'modelo', 'foto',
            'paises', 'categoria', 'sub_categoria',
            'homologacion', 'certificados',
            'parametros_transmision', 'parametros_recepcion',
            'interfaces_alambricas', 'evaluaciones',
            'certificaciones_externas',
        ]
