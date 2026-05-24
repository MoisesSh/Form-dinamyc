

from rest_framework import serializers


class ComprobanteHomologacionRequestSerializer(serializers.Serializer):

    equipo_ids = serializers.ListField(
        child=serializers.IntegerField(min_value=1),
        min_length=1,
        help_text='Lista de IDs de equipos homologados para incluir en el comprobante.',
    )
