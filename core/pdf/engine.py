"""Motor de generación del PDF.

Contiene la clase ServiceReportPDF que orquesta la creación del documento.
"""

from io import BytesIO
from typing import Any, List, Tuple

from reportlab.lib import colors
from reportlab.lib.pagesizes import letter
from reportlab.lib.units import inch
from reportlab.platypus import Paragraph, SimpleDocTemplate, Spacer, Table, TableStyle
from reportlab.platypus.flowables import Flowable

from core.pdf.styles import draw_footer_callback, get_report_styles


class ServiceReportPDF:
    """Clase encargada de la generación del reporte en PDF.

    Organiza la construcción del documento siguiendo el orden visual:
    Header -> Info General -> Checklists -> Servicios/Repuestos -> Totales -> Footer.
    """

    def __init__(self, report_data: Any):
        """Inicializa el generador con los datos del reporte.

        Args:
            report_data: Objeto modelo con los datos del reporte.
        """
        self.report_data = report_data
        self.buffer = BytesIO()
        self.doc = SimpleDocTemplate(
            self.buffer,
            pagesize=letter,
            rightMargin=36,
            leftMargin=36,
            topMargin=36,
            bottomMargin=50,
        )
        self.usable_width = letter[0] - self.doc.leftMargin - self.doc.rightMargin - 1
        self.styles = get_report_styles()
        self.story: List[Flowable] = []

    def generate(self) -> BytesIO:
        """Construye y genera el PDF.

        Returns:
            BytesIO con el contenido del PDF.
        """
        self._build_header()
        self._build_general_info()
        self._build_checklists()
        self._build_observations()
        self._build_services_and_parts()
        self._build_totals()
        self._build_signatures()

        # Build del documento con callback para el footer en cada página
        self.doc.build(
            self.story,
            onFirstPage=draw_footer_callback,
            onLaterPages=draw_footer_callback,
        )
        self.buffer.seek(0)
        return self.buffer

    # --- Secciones del Documento (En orden visual) ---

    def _build_header(self):
        """Construye el encabezado con info de la empresa e ID del reporte."""
        company_text = (
            "<b><font size='9'>Auto Servicios Integrales</font></b><br/>"
            "<b><font size='9'>Los Cerritos L.J. C.A.</font></b><br/>"
            "R.I.F. J-30497327-6<br/>"
            "Tlf. : 0212-3236867 | 0414-1259502"
        )
        
        # Estilo para la info de la empresa (alineado a la izquierda, más pequeño)
        from reportlab.lib.styles import ParagraphStyle
        from reportlab.lib.enums import TA_LEFT, TA_RIGHT
        
        company_style = ParagraphStyle(
            name="CompanyInfo",
            parent=self.styles["Normal"],
            fontSize=7,
            leading=8,
            alignment=TA_LEFT
        )
        
        report_id_style = ParagraphStyle(
            name="ReportID",
            parent=self.styles["h1"],
            alignment=TA_RIGHT
        )

        left_content = Paragraph(company_text, company_style)
        right_content = Paragraph(f"Reporte de Servicio -> #{self.report_data.id_reporte}", report_id_style)

        data = [[left_content, right_content]]
        # 60% para empresa, 40% para reporte id
        col_widths = [self.usable_width * 0.6, self.usable_width * 0.4]
        
        table = Table(data, colWidths=col_widths)
        table.setStyle(TableStyle([
            ('VALIGN', (0, 0), (-1, -1), 'TOP'),
            ('LEFTPADDING', (0, 0), (-1, -1), 0),
            ('RIGHTPADDING', (0, 0), (-1, -1), 0),
            ('BOTTOMPADDING', (0, 0), (-1, -1), 2),
        ]))
        
        self.story.append(table)
        self.story.append(Spacer(1, 0.02 * inch))

    def _build_general_info(self):
        """Construye la sección de información general del cliente y vehículo."""
        self.story.append(Spacer(1, 0.05 * inch))
        self.story.append(Paragraph("Información General", self.styles["h3"]))

        # Calculo de anchos proporcionales
        w1, w3 = 1.0 * inch, 0.8 * inch
        w_rest = (self.usable_width - w1 - w3) / 2
        col_widths = [w1, w_rest, w3, w_rest]

        data = [
            [
                "Fecha:",
                self.report_data.fecha.strftime("%d-%m-%Y"),
                "Placa:",
                self.report_data.placa,
            ],
            [
                "Nombre Cliente:",
                self.report_data.nombre_cliente,
                "Modelo:",
                self.report_data.modelo,
            ],
            [
                "Cédula Cliente:",
                str(self.report_data.cedula_cliente),
                "Color:",
                self.report_data.color,
            ],
            [
                "Teléfono:",
                str(self.report_data.telefono_cliente),
                "Estado:",
                self.report_data.status_reporte.capitalize(),
            ],
        ]

        table = Table(data, colWidths=col_widths, hAlign="CENTER")
        table.setStyle(
            TableStyle(
                [
                    ("GRID", (0, 0), (-1, -1), 0.5, colors.grey),
                    ("FONTNAME", (0, 0), (0, -1), "Helvetica-Bold"),
                    ("FONTNAME", (2, 0), (2, -1), "Helvetica-Bold"),
                    ("FONTSIZE", (0, 0), (-1, -1), 7.5),
                    ("BOTTOMPADDING", (0, 0), (-1, -1), 0.5),
                    ("TOPPADDING", (0, 0), (-1, -1), 0.5),
                    ("LEFTPADDING", (0, 0), (-1, -1), 2),
                    ("RIGHTPADDING", (0, 0), (-1, -1), 2),
                ]
            )
        )
        self.story.append(table)
        self.story.append(Spacer(1, 0.02 * inch))

    def _build_checklists(self):
        """Construye las secciones de checklist (Carrocería, Accesorios, Eléctrico)."""
        # Carrocería
        carroceria_items = [
            ("Golpe", self.report_data.carroceria_golpe),
            ("Suelto", self.report_data.carroceria_suelto),
            ("Rayas", self.report_data.carroceria_rayas),
            ("Desconchado", self.report_data.carroceria_desconchado),
            ("Vidrio Roto", self.report_data.carroceria_vidrio_roto),
            ("Falta Moldura", self.report_data.carroceria_falta_moldura),
            ("Falta Faro", self.report_data.carroceria_falta_faro),
            ("Falta Accesorio", self.report_data.carroceria_falta_accesorio),
            ("Espejo Roto", self.report_data.carroceria_espejo_roto),
            ("Centro Copas", self.report_data.carroceria_falta_centro_copas),
            ("Otro (Carroc.)", self.report_data.carroceria_otro),
        ]
        self.story.append(Paragraph("Carrocería", self.styles["h3"]))
        self.story.append(self._create_checklist_table(carroceria_items))

        # Accesorios
        accesorios_items = [
            ("Alfombra Del", self.report_data.accesorios_alfombra_delantera),
            ("Alfombra Tras", self.report_data.accesorios_alfombra_trasera),
            ("Radio", self.report_data.accesorios_radio),
            ("Reproductor", self.report_data.accesorios_radio_reproductor),
            ("Antena Eléc", self.report_data.accesorios_antena_electrica),
            ("Encendedor", self.report_data.accesorios_encendedor_cigarrillos),
            ("Triángulo Seg", self.report_data.accesorios_triangulo_seguridad),
            ("Gato", self.report_data.accesorios_gato),
            ("Caucho Rep", self.report_data.accesorios_caucho_repuesto),
            ("Otro (Acces.)", self.report_data.accesorios_otro),
        ]
        self.story.append(Paragraph("Accesorios", self.styles["h3"]))
        self.story.append(self._create_checklist_table(accesorios_items))

        # Sistemas Eléctricos
        electrico_items = [
            ("Frenos Del", self.report_data.sistem_electric_frenos_del),
            ("Tablero", self.report_data.sistem_electric_tablero),
            ("Luz Cruce", self.report_data.sistem_electric_luz_cruce),
            ("Luz Stop", self.report_data.sistem_electric_stop),
            ("Vidrio Eléc", self.report_data.sistem_electric_vidrio_electrico),
            ("Aire Acond", self.report_data.sistem_electric_aire_acondicionado),
            ("Otro (Elec.)", self.report_data.sistem_electric_otro),
        ]
        self.story.append(Paragraph("Sistemas Eléctricos", self.styles["h3"]))
        self.story.append(self._create_checklist_table(electrico_items))

    def _build_observations(self):
        """Agrega las observaciones adicionales si existen."""
        if self.report_data.observaciones:
            self.story.append(Paragraph("Observaciones Adicionales", self.styles["h3"]))
            text = self.report_data.observaciones.replace("\n", "<br/>")
            self.story.append(Paragraph(text, self.styles["Normal"]))

    def _build_services_and_parts(self):
        """Construye las tablas de servicios realizados y repuestos utilizados."""
        if self.report_data.servicios:
            rows = [
                [s.item, s.descripcion, f"{s.presupuesto:.2f}"]
                for s in self.report_data.servicios
            ]
            self.story.append(Paragraph("Servicios Realizados", self.styles["h3"]))
            self.story.append(
                self._create_items_table(
                    ["Item", "Descripción", "Presupuesto"], rows
                )
            )
            self.story.append(Spacer(1, 0.02 * inch))

        if self.report_data.repuestos:
            rows = [
                [r.cantidad, r.descripcion, f"{r.presupuesto:.2f}"]
                for r in self.report_data.repuestos
            ]
            self.story.append(Paragraph("Repuestos Utilizados", self.styles["h3"]))
            self.story.append(
                self._create_items_table(
                    ["Cant.", "Descripción", "Presupuesto"], rows
                )
            )
            self.story.append(Spacer(1, 0.02 * inch))

    def _build_totals(self):
        """Construye la tabla de totales."""
        self.story.append(Spacer(1, 0.02 * inch))
        self.story.append(Paragraph("Totales Generales", self.styles["h3"]))
        data = [
            ["Total Servicios:", f"{self.report_data.total_servicios or 0:.2f}"],
            ["Total Repuestos:", f"{self.report_data.total_repuestos or 0:.2f}"],
            ["Total General:", f"{self.report_data.total_general or 0:.2f}"],
        ]
        col_widths = [self.usable_width - 1.2 * inch, 1.2 * inch]
        table = Table(data, colWidths=col_widths)
        table.setStyle(
            TableStyle(
                [
                    ("ALIGN", (0, 0), (-1, -1), "RIGHT"),
                    ("GRID", (0, 0), (-1, -1), 0.5, colors.grey),
                    ("FONTSIZE", (0, 0), (-1, -1), 7.5),
                    ("BOTTOMPADDING", (0, 0), (-1, -1), 1),
                    ("TOPPADDING", (0, 0), (-1, -1), 1),
                ]
            )
        )
        self.story.append(table)

    def _build_signatures(self):
        """Construye la sección de firmas con la cláusula de conformidad."""
        self.story.append(Spacer(1, 0.2 * inch))
        clause_text = (
            "Al firmar el presente documento, el cliente declara estar conforme con la inspección "
            "del vehículo (checklist) y con los presupuestos de servicios y repuestos aquí detallados. "
            "La firma ratifica la veracidad de la información recolectada y autoriza la ejecución "
            "de los trabajos bajo los términos descritos."
        )
        self.story.append(Paragraph(clause_text, self.styles["Clause"]))
        
        self.story.append(Spacer(1, 0.5 * inch))
        data = [
            ["", "________________________"],
            ["", Paragraph("Firma Cliente", self.styles["Signature"])],
        ]
        col_widths = [self.usable_width - 2.5 * inch, 2.5 * inch]
        table = Table(data, colWidths=col_widths)
        table.setStyle(TableStyle([("ALIGN", (1, 0), (1, 1), "CENTER")]))
        self.story.append(table)

    # --- Helpers ---

    def _create_checklist_table(self, items: List[Tuple[str, bool]]) -> Table:
        """Crea una tabla con formato de checklist."""
        data = []
        temp_row = []
        for label, val in items:
            mark = "[x]" if val else "[ ]"
            cell_text = f"{mark} {label}"
            p = Paragraph(cell_text, self.styles["Checklist"])
            temp_row.append(p)
            if len(temp_row) == 2:
                data.append(temp_row)
                temp_row = []
        if temp_row:
            data.append(temp_row + [""])

        t = Table(data, colWidths=[self.usable_width / 2.0] * 2)
        t.setStyle(
            TableStyle(
                [
                    ("GRID", (0, 0), (-1, -1), 0.5, colors.grey),
                    ("VALIGN", (0, 0), (-1, -1), "MIDDLE"),
                    ("LEFTPADDING", (0, 0), (-1, -1), 5),
                    ("TOPPADDING", (0, 0), (-1, -1), 1),
                    ("BOTTOMPADDING", (0, 0), (-1, -1), 1),
                ]
            )
        )
        return t

    def _create_items_table(self, header: List[str], rows: List[List[str]]) -> Table:
        """Crea una tabla para listados de items (servicios/repuestos)."""
        data = [header] + rows
        col_w = [self.usable_width * 0.1, self.usable_width * 0.7, self.usable_width * 0.2]

        t = Table(data, colWidths=col_w)
        t.setStyle(
            TableStyle(
                [
                    ("GRID", (0, 0), (-1, -1), 0.5, colors.grey),
                    ("ALIGN", (2, 0), (2, -1), "RIGHT"),
                    ("FONTNAME", (0, 0), (-1, 0), "Helvetica-Bold"),
                    ("FONTSIZE", (0, 0), (-1, -1), 7.5),
                    ("BOTTOMPADDING", (0, 0), (-1, -1), 0.5),
                    ("TOPPADDING", (0, 0), (-1, -1), 0.5),
                    ("LEFTPADDING", (0, 0), (-1, -1), 2),
                    ("RIGHTPADDING", (0, 0), (-1, -1), 2),
                ]
            )
        )
        return t
