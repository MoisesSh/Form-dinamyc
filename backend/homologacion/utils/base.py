
import os
from io import BytesIO

from reportlab.lib import colors
from reportlab.lib.enums import TA_CENTER, TA_LEFT, TA_RIGHT
from reportlab.lib.pagesizes import letter
from reportlab.lib.styles import ParagraphStyle, getSampleStyleSheet
from reportlab.lib.units import cm, mm
from reportlab.platypus import (
    BaseDocTemplate,
    Frame,
    Image,
    PageBreak,
    PageTemplate,
    Paragraph,
    Spacer,
    Table,
    TableStyle,
)

# Directorio donde están los archivos estáticos (imágenes)
_STATIC_DIR = os.path.join(
    os.path.dirname(os.path.dirname(os.path.abspath(__file__))),
    'static',
)

# Colores institucionales
AZUL_CONATEL = colors.HexColor('#1B3A5C')
AZUL_CLARO = colors.HexColor('#2C5F8A')
GRIS_LINEA = colors.HexColor('#B0B0B0')
GRIS_FONDO = colors.HexColor('#F5F5F5')


def _get_image_path(filename):
    #Obtiene la ruta absoluta de una imagen en static/.
    path = os.path.join(_STATIC_DIR, filename)
    if not os.path.isfile(path):
        raise FileNotFoundError(
            f"Imagen no encontrada: {path}. "
            f"Asegúrese de que el archivo '{filename}' esté en homologacion/static/"
        )
    return path


def get_custom_styles():
    #Devuelve un diccionario con los estilos personalizados para los PDFs.
    styles = getSampleStyleSheet()

    styles.add(ParagraphStyle(
        'PDFTitle',
        parent=styles['Title'],
        fontSize=16,
        leading=20,
        textColor=AZUL_CONATEL,
        alignment=TA_CENTER,
        spaceAfter=6 * mm,
        fontName='Helvetica-Bold',
    ))

    styles.add(ParagraphStyle(
        'PDFSubtitle',
        parent=styles['Normal'],
        fontSize=11,
        leading=14,
        textColor=AZUL_CLARO,
        alignment=TA_CENTER,
        spaceAfter=4 * mm,
        fontName='Helvetica',
    ))

    styles.add(ParagraphStyle(
        'PDFBody',
        parent=styles['Normal'],
        fontSize=10,
        leading=13,
        textColor=colors.black,
        alignment=TA_LEFT,
        fontName='Helvetica',
    ))

    styles.add(ParagraphStyle(
        'PDFBodyBold',
        parent=styles['Normal'],
        fontSize=10,
        leading=13,
        textColor=colors.black,
        alignment=TA_LEFT,
        fontName='Helvetica-Bold',
    ))

    styles.add(ParagraphStyle(
        'PDFTableHeader',
        parent=styles['Normal'],
        fontSize=9,
        leading=11,
        textColor=colors.white,
        alignment=TA_CENTER,
        fontName='Helvetica-Bold',
    ))

    styles.add(ParagraphStyle(
        'PDFTableCell',
        parent=styles['Normal'],
        fontSize=8,
        leading=10,
        textColor=colors.black,
        alignment=TA_CENTER,
        fontName='Helvetica',
    ))

    styles.add(ParagraphStyle(
        'PDFFooter',
        parent=styles['Normal'],
        fontSize=7,
        leading=9,
        textColor=colors.grey,
        alignment=TA_CENTER,
        fontName='Helvetica',
    ))

    return styles


class BasePDFTemplate:


    def __init__(
        self,
        title='Documento CONATEL',
        left_logo='banderin.jpeg',
        right_logo='bicentenario.jpeg',
        footer_text='CONATEL — Comisión Nacional de Telecomunicaciones',
        page_size=letter,
        margins=None,
    ):
        self.title = title
        self.left_logo_path = _get_image_path(left_logo)
        self.right_logo_path = _get_image_path(right_logo)
        self.footer_text = footer_text
        self.page_size = page_size

        default_margins = {'top': 4.0, 'bottom': 2.5, 'left': 2.0, 'right': 2.0}
        if margins:
            default_margins.update(margins)
        self.margins = default_margins

    def _header_footer(self, canvas, doc):
        #Dibuja encabezado y pie de página en cada página.
        canvas.saveState()
        page_width, page_height = self.page_size

        # Encabezado 
        header_y = page_height - 2.8 * cm

        # Logo izquierdo (banderin)
        try:
            logo_left_w = 7.5 * cm
            logo_left_h = 1.8 * cm
            canvas.drawImage(
                self.left_logo_path,
                self.margins['left'] * cm,
                header_y,
                width=logo_left_w,
                height=logo_left_h,
                preserveAspectRatio=True,
                mask='auto',
            )
        except Exception:
            # Si la imagen falla, escribir texto alternativo
            canvas.setFont('Helvetica-Bold', 8)
            canvas.drawString(self.margins['left'] * cm, header_y + 0.5 * cm, 'CONATEL')

        # Logo derecho (bicentenario)
        try:
            logo_right_w = 2.5 * cm
            logo_right_h = 2.2 * cm
            canvas.drawImage(
                self.right_logo_path,
                page_width - self.margins['right'] * cm - logo_right_w,
                header_y - 0.2 * cm,
                width=logo_right_w,
                height=logo_right_h,
                preserveAspectRatio=True,
                mask='auto',
            )
        except Exception:
            pass

        # Línea separadora del encabezado
        line_y = header_y - 0.3 * cm
        canvas.setStrokeColor(AZUL_CONATEL)
        canvas.setLineWidth(1.5)
        canvas.line(
            self.margins['left'] * cm,
            line_y,
            page_width - self.margins['right'] * cm,
            line_y,
        )

        # Pie de página 
        footer_y = 1.5 * cm

        # Línea separadora del pie
        canvas.setStrokeColor(GRIS_LINEA)
        canvas.setLineWidth(0.5)
        canvas.line(
            self.margins['left'] * cm,
            footer_y + 0.3 * cm,
            page_width - self.margins['right'] * cm,
            footer_y + 0.3 * cm,
        )

        # Texto institucional (izquierda)
        canvas.setFont('Helvetica', 7)
        canvas.setFillColor(colors.grey)
        canvas.drawString(self.margins['left'] * cm, footer_y, self.footer_text)

        # Numeración de página (derecha)
        page_num_text = f'Página {doc.page}'
        canvas.drawRightString(
            page_width - self.margins['right'] * cm,
            footer_y,
            page_num_text,
        )

        canvas.restoreState()

    def build_pdf(self, story):

        buffer = BytesIO()
        page_width, page_height = self.page_size

        doc = BaseDocTemplate(
            buffer,
            pagesize=self.page_size,
            title=self.title,
            author='CONATEL',
            subject=self.title,
        )

        # Frame principal del contenido (respeta márgenes y espacio de header/footer)
        frame = Frame(
            x1=self.margins['left'] * cm,
            y1=self.margins['bottom'] * cm,
            width=page_width - (self.margins['left'] + self.margins['right']) * cm,
            height=page_height - (self.margins['top'] + self.margins['bottom']) * cm,
            id='main_frame',
        )

        template = PageTemplate(
            id='base',
            frames=[frame],
            onPage=self._header_footer,
        )
        doc.addPageTemplates([template])

        doc.build(story)
        buffer.seek(0)
        return buffer


def build_table_style():

    return TableStyle([
        # Encabezado
        ('BACKGROUND', (0, 0), (-1, 0), AZUL_CONATEL),
        ('TEXTCOLOR', (0, 0), (-1, 0), colors.white),
        ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
        ('FONTSIZE', (0, 0), (-1, 0), 9),
        ('ALIGN', (0, 0), (-1, 0), 'CENTER'),
        ('VALIGN', (0, 0), (-1, 0), 'MIDDLE'),
        ('BOTTOMPADDING', (0, 0), (-1, 0), 8),
        ('TOPPADDING', (0, 0), (-1, 0), 8),

        # Celdas de datos
        ('FONTNAME', (0, 1), (-1, -1), 'Helvetica'),
        ('FONTSIZE', (0, 1), (-1, -1), 8),
        ('ALIGN', (0, 1), (-1, -1), 'CENTER'),
        ('VALIGN', (0, 1), (-1, -1), 'MIDDLE'),
        ('BOTTOMPADDING', (0, 1), (-1, -1), 6),
        ('TOPPADDING', (0, 1), (-1, -1), 6),

        # Filas alternas
        ('ROWBACKGROUNDS', (0, 1), (-1, -1), [colors.white, GRIS_FONDO]),

        # Bordes
        ('GRID', (0, 0), (-1, -1), 0.5, GRIS_LINEA),
        ('LINEBELOW', (0, 0), (-1, 0), 1.5, AZUL_CONATEL),
    ])
