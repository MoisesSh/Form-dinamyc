"""
Vista API para la generación del Comprobante de Homologación en PDF.

La vista se limita a validar la entrada HTTP y delegar
toda la lógica de negocio al servicio pdf_services.
"""

import json
from datetime import datetime

from django.http import HttpResponse
from rest_framework import status
from rest_framework.generics import GenericAPIView

from core.serializers.pdf_serializers import ComprobanteHomologacionRequestSerializer
from core.services.pdf_services import (
    EquipoNoAprobadoError,
    generar_comprobante_pdf,
)


class ComprobanteHomologacionPDFView(GenericAPIView):
    serializer_class = ComprobanteHomologacionRequestSerializer

    def post(self, request, *args, **kwargs):
        # 1. Validar entrada
        serializer = self.get_serializer(data=request.data)
        if not serializer.is_valid():
            return self._error_response(
                'Datos de entrada inválidos.',
                serializer.errors,
            )

        equipo_ids = serializer.validated_data['equipo_ids']

        # 2. Delegar al servicio
        try:
            pdf_buffer = generar_comprobante_pdf(equipo_ids)
        except EquipoNoAprobadoError as e:
            return self._error_response(
                'Algunos equipos no fueron encontrados o no están homologados.',
                {'ids_invalidos': sorted(e.ids_invalidos)},
            )

        # 3. Devolver el PDF como respuesta HTTP
        response = HttpResponse(
            pdf_buffer.getvalue(),
            content_type='application/pdf',
        )
        timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
        response['Content-Disposition'] = (
            f'inline; filename="comprobante_homologacion_{timestamp}.pdf"'
        )
        return response

    def _error_response(self, mensaje, detalles=None):

        body = {'error': mensaje}
        if detalles:
            body['detalles'] = detalles
        return HttpResponse(
            json.dumps(body, ensure_ascii=False),
            content_type='application/json',
            status=status.HTTP_400_BAD_REQUEST,
        )
