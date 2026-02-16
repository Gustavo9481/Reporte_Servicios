"""Paquete para la generación de reportes en PDF.

Este paquete organiza la lógica de generación, estilos y configuración
para los reportes de servicio en formato PDF.
"""

from io import BytesIO
from typing import Any

from core.pdf.engine import ServiceReportPDF


def generate_report_pdf(report_data: Any) -> BytesIO:
    """Función de conveniencia para generar un reporte PDF.

    Crea una instancia de ServiceReportPDF y ejecuta el proceso de generación.

    Args:
        report_data: Objeto con los datos del reporte.

    Returns:
        BytesIO con el contenido del PDF generado.
    """
    report_pdf = ServiceReportPDF(report_data)
    return report_pdf.generate()
