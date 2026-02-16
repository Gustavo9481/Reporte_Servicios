"""Estilos y configuraciones visuales para el generador de PDF.

Define los estilos de párrafo, colores y la función para dibujar el pie de página.
"""

from typing import Any

from reportlab.lib import colors
from reportlab.lib.enums import TA_CENTER, TA_LEFT, TA_RIGHT
from reportlab.lib.styles import ParagraphStyle, getSampleStyleSheet, StyleSheet1
from reportlab.platypus import Paragraph, SimpleDocTemplate


def get_report_styles() -> StyleSheet1:
    """Configura y retorna los estilos utilizados en el reporte."""
    styles = getSampleStyleSheet()
    styles.add(ParagraphStyle(name="Left", alignment=TA_LEFT))
    styles.add(ParagraphStyle(name="Right", alignment=TA_RIGHT))
    styles.add(
        ParagraphStyle(
            name="Checklist", parent=styles["Normal"], fontSize=7.5, leading=8
        )
    )
    styles.add(
        ParagraphStyle(
            name="Signature",
            parent=styles["Normal"],
            fontSize=5,
            alignment=TA_CENTER,
        )
    )
    styles["h1"].alignment = TA_CENTER
    styles["h1"].fontSize = 7.5
    styles["h1"].fontName = "Helvetica-Bold"
    styles["h3"].alignment = TA_LEFT
    styles["h3"].fontSize = 7.5
    styles["h3"].fontName = "Helvetica-Bold"
    styles["h3"].textColor = colors.black
    styles["h3"].spaceBefore = 2
    styles["h3"].spaceAfter = 2
    styles["Normal"].fontSize = 7.5
    from reportlab.lib.enums import TA_JUSTIFY
    styles.add(
        ParagraphStyle(
            name="Clause",
            parent=styles["Normal"],
            fontSize=6.5,
            leading=8,
            alignment=TA_JUSTIFY,
            fontName="Helvetica-Oblique",
        )
    )
    return styles


def draw_footer_callback(canvas: Any, doc: SimpleDocTemplate) -> None:
    """Dibuja el pie de página en cada página del PDF.

    Args:
        canvas: El canvas de ReportLab.
        doc: El documento plantilla.
    """
    canvas.saveState()

    footer_style = ParagraphStyle(
        name="Footer",
        fontSize=8,
        alignment=TA_CENTER,
        textColor=colors.grey,
    )

    text = """
    Avenida Independencia El Llano de Miquilen, Municipio Bolivariano de Guaicaipuro Estado Miranda.
    """

    p = Paragraph(text, footer_style)

    # Usa las dimensiones del documento para el posicionamiento.
    w, h = p.wrap(doc.width * 0.7, doc.bottomMargin)

    # Calcula la posición x para centrar el bloque de 70%.
    x = doc.leftMargin + (doc.width - (doc.width * 0.7)) / 2

    # Posiciona el texto en la parte inferior del margen.
    y = doc.bottomMargin - h - 20

    p.drawOn(canvas, x, y)
    canvas.restoreState()
