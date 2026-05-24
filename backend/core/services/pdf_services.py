
from datetime import datetime

from reportlab.lib.units import mm
from reportlab.platypus import Paragraph, Spacer, Table

from core.models.tecnico_models import Equipo
from homologacion.utils.base import (
    BasePDFTemplate,
    build_table_style,
    get_custom_styles,
)


class EquipoNoAprobadoError(Exception):

    def __init__(self, ids_invalidos):
        self.ids_invalidos = ids_invalidos
        super().__init__(
            f'Equipos no encontrados o no homologados: {sorted(ids_invalidos)}'
        )


def validar_equipos_homologados(equipo_ids):

    equipos = (
        Equipo.objects
        .filter(id__in=equipo_ids, aprobado=1)
        .select_related('homologacion', 'homologacion__estatus')
        .order_by('id')
    )

    ids_encontrados = set(equipos.values_list('id', flat=True))
    ids_solicitados = set(equipo_ids)
    ids_faltantes = ids_solicitados - ids_encontrados

    if ids_faltantes:
        raise EquipoNoAprobadoError(ids_faltantes)

    return equipos


def generar_comprobante_pdf(equipo_ids):
    equipos = validar_equipos_homologados(equipo_ids)
    story = _construir_contenido(equipos)

    template = BasePDFTemplate(title='Comprobante de Homologación')
    return template.build_pdf(story)


def _construir_contenido(equipos):

    styles = get_custom_styles()
    story = []

    #    Título
    story.append(Spacer(1, 8 * mm))
    story.append(Paragraph(
        'COMPROBANTE DE HOMOLOGACIÓN',
        styles['PDFTitle'],
    ))

    #    Fecha de emisión   
    fecha_actual = datetime.now().strftime('%d/%m/%Y — %H:%M')
    story.append(Paragraph(
        f'<b>Fecha de emisión:</b> {fecha_actual}',
        styles['PDFBody'],
    ))
    story.append(Spacer(1, 6 * mm))

    #    Texto introductorio
    from user.models.firmar_models import ConsejoDirectivo
    consejo = ConsejoDirectivo.objects.filter(is_active=True).first()

    if consejo:
        texto_intro = (
            f"Quien suscribe, {consejo.nombre_completo or ''}, titular de la cédula de identidad "
            f"N° V- {consejo.C_I or ''}, {consejo.cargo or ''} de la Comisión Nacional de Telecomunicaciones "
            f"(CONATEL), designado por el ciudadano Presidente de la República Bolivariana de Venezuela "
            f"mediante {consejo.decreto or ''}, en ejercicio de las atribuciones conferidas por el artículo 44 "
            f"de la Ley Orgánica de Telecomunicaciones y el artículo 3 de la Disposición Administrativa sobre "
            f"Categorías de Equipos de Telecomunicaciones Sujetos a Homologación y Certificación, publicada "
            f"en la Gaceta Oficial de la República Bolivariana de Venezuela N°{consejo.gaceta_nro or ''} de fecha {consejo.gaceta_fecha or ''}:"
        )
    else:
        texto_intro = (
            "A continuación se presenta el listado de equipos homologados "
            "seleccionados que han sido debidamente aprobados por la "
            "Comisión Nacional de Telecomunicaciones (CONATEL):"
        )

    story.append(Paragraph(
        texto_intro,
        styles['PDFBody'],
    ))
    story.append(Spacer(1, 6 * mm))

    #    Tabla de equipos   
    encabezados = [
        Paragraph('N°', styles['PDFTableHeader']),
        Paragraph('Código Equipo', styles['PDFTableHeader']),
        Paragraph('Marca', styles['PDFTableHeader']),
        Paragraph('Modelo', styles['PDFTableHeader']),
        Paragraph('Cód. Homologación', styles['PDFTableHeader']),
        Paragraph('Fecha Homologación', styles['PDFTableHeader']),
        Paragraph('Estado', styles['PDFTableHeader']),
    ]

    filas = [encabezados]
    for idx, equipo in enumerate(equipos, start=1):
        homologacion = getattr(equipo, 'homologacion', None)

        cod_homo = (
            homologacion.cod_homo
            if homologacion and homologacion.cod_homo
            else 'N/D'
        )

        if homologacion and homologacion.fecha_emision:
            fecha_homo = homologacion.fecha_emision.strftime('%d/%m/%Y')
        else:
            fecha_homo = 'N/D'

        estatus_nombre = 'N/D'
        if homologacion and homologacion.estatus:
            estatus_nombre = homologacion.estatus.nombre or 'N/D'

        fila = [
            Paragraph(str(idx), styles['PDFTableCell']),
            Paragraph(equipo.cod_equipo or 'N/D', styles['PDFTableCell']),
            Paragraph(equipo.marca or 'N/D', styles['PDFTableCell']),
            Paragraph(equipo.modelo or 'N/D', styles['PDFTableCell']),
            Paragraph(cod_homo, styles['PDFTableCell']),
            Paragraph(fecha_homo, styles['PDFTableCell']),
            Paragraph(estatus_nombre, styles['PDFTableCell']),
        ]
        filas.append(fila)

    # Anchos de columna proporcionales
    col_widths = [25, 75, 70, 80, 90, 80, 65]

    tabla = Table(filas, colWidths=col_widths, repeatRows=1)
    tabla.setStyle(build_table_style())
    story.append(tabla)

    story.append(Spacer(1, 10 * mm))

    # Nota al pie del contenido  
    story.append(Paragraph(
        '<i>Este documento es un comprobante de homologación generado '
        'automáticamente por el sistema. Para cualquier consulta, '
        'diríjase a la Comisión Nacional de Telecomunicaciones (CONATEL).</i>',
        styles['PDFFooter'],
    ))

    return story
