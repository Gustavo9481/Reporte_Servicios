# MODULO: core/pdf_generator.py
""" Generador de PDFs para Reporte_Servicios.
Aplicación del módulo Reportlab.
El presente módulo genera un archivo .pdf con toda la información del reporte
para poder obtener la firma de aceptación y conformidad del cliente.
El archivo se genera con el número de placa por defecto.
"""

from io import BytesIO

from reportlab.lib import colors
from reportlab.lib.enums import TA_CENTER, TA_LEFT, TA_RIGHT
from reportlab.lib.pagesizes import letter
from reportlab.lib.styles import ParagraphStyle, getSampleStyleSheet
from reportlab.lib.units import inch
from reportlab.platypus import Paragraph, SimpleDocTemplate, Spacer, Table, TableStyle


def draw_footer(canvas, doc) -> None:
    """ Dibuja el pie de página en la parte inferior de cada página. """

    canvas.saveState()

    footer_style = ParagraphStyle(
        name="Footer",
        fontSize=8,
        alignment=TA_CENTER,
        textColor=colors.grey,
    )

    text = """
    Calle 5 Rafael Vegas, Conjunto Residencial Parque de Las Américas, Edif. San Martín<br/>
    Sector La Mata, Los Teques - Estado Miranda
    """

    p = Paragraph(text, footer_style)

    # Usa las dimensiones del documento para el posicionamiento.
    w, h = p.wrap(doc.width * 0.7, doc.bottomMargin)

    # Calcula la posición x para centrar el bloque de 70%.
    x = doc.leftMargin + (doc.width - (doc.width * 0.7)) / 2

    # Posiciona el texto en la parte inferior del margen.
    y = doc.bottomMargin - h - 20  # Ajuste fino para la posición vertical.

    p.drawOn(canvas, x, y)
    canvas.restoreState()


def generate_report_pdf(report_data):
    """ Genera un archivo PDF para un reporte específico incluyendo todos los
    campos del checklist.
    """

    buffer = BytesIO()
    doc = SimpleDocTemplate(
        buffer,
        pagesize=letter,
        rightMargin=36,
        leftMargin=36,
        topMargin=36,
        bottomMargin=50,
    )

    usable_width = letter[0] - doc.leftMargin - doc.rightMargin - 1

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
            name="Signature", parent=styles["Normal"], fontSize=5, alignment=TA_CENTER
        )
    )
    styles["h1"].alignment = TA_CENTER
    styles["h1"].fontSize = 7.5
    styles["h1"].fontName = "Helvetica-Bold"
    styles["h3"].alignment = TA_LEFT
    styles["h3"].fontSize = 7.5
    styles["h3"].fontName = "Helvetica-Bold"
    styles["h3"].textColor = colors.black
    styles["Normal"].fontSize = 7.5

    story = []

    # .. ............................................... Título
    # Título simple para el reporte.
    story.append(
        Paragraph(f"Reporte de Servicio -> #{report_data.id_reporte}", styles["h1"])
    )
    story.append(Spacer(1, 0.04 * inch))

    # .. .................................. Información General
    # Información o datos básicos del reporte.
    story.append(
        Paragraph("Información General", styles["h3"])
    )
    # Calculo de anchos proporcionales para el 100%.
    w1, w3 = 1.0 * inch, 0.8 * inch
    w_rest = (usable_width - w1 - w3) / 2
    info_col_widths = [w1, w_rest, w3, w_rest]
    info_data = [
        ["Fecha:", report_data.fecha.strftime("%d-%m-%Y"), "Placa:", report_data.placa],
        ["Nombre Cliente:", report_data.nombre_cliente, "Modelo:", report_data.modelo],
        [
            "Cédula Cliente:",
            str(report_data.cedula_cliente),
            "Color:",
            report_data.color,
        ],
        [
            "Teléfono:",
            str(report_data.telefono_cliente),
            "Estado:",
            report_data.status_reporte.capitalize(),
        ],
    ]
    info_table = Table(info_data, colWidths=info_col_widths, hAlign="LEFT")
    info_table.setStyle(
        TableStyle(
            [
                ("GRID", (0, 0), (-1, -1), 0.5, colors.grey),
                ("FONTNAME", (0, 0), (0, -1), "Helvetica-Bold"),
                ("FONTNAME", (2, 0), (2, -1), "Helvetica-Bold"),
                ("FONTSIZE", (0, 0), (-1, -1), 7.5),
                ("BOTTOMPADDING", (0, 0), (-1, -1), 1),
                ("TOPPADDING", (0, 0), (-1, -1), 1),
            ]
        )
    )
    story.append(info_table)
    story.append(Spacer(1, 0.04 * inch))


    # .. .................... función -> create_checklist_table
    # Crea tablas de checklist.
    def create_checklist_table(title, items):
        story.append(Paragraph(title, styles["h3"]))
        data = []
        temp_row = []
        for label, val in items:
            mark = "[x]" if val else "[ ]"
            cell_text = f"{mark} {label}"
            p = Paragraph(cell_text, styles["Checklist"])
            temp_row.append(p)
            if len(temp_row) == 2:
                data.append(temp_row)
                temp_row = []
        if temp_row:
            data.append(temp_row + [""])

        t = Table(data, colWidths=[usable_width / 2.0] * 2)
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

    # .. .............................. Secciones del CkeckList
    # Listados de opciones de selección, con su marca correspondiente.
    carroceria_items = [
        ("Golpe", report_data.carroceria_golpe),
        ("Suelto", report_data.carroceria_suelto),
        ("Rayas", report_data.carroceria_rayas),
        ("Desconchado", report_data.carroceria_desconchado),
        ("Vidrio Roto", report_data.carroceria_vidrio_roto),
        ("Falta Moldura", report_data.carroceria_falta_moldura),
        ("Falta Faro", report_data.carroceria_falta_faro),
        ("Falta Accesorio", report_data.carroceria_falta_accesorio),
        ("Espejo Roto", report_data.carroceria_espejo_roto),
        ("Centro Copas", report_data.carroceria_falta_centro_copas),
        ("Otro (Carroc.)", report_data.carroceria_otro),
    ]
    story.append(create_checklist_table("Carrocería", carroceria_items))

    accesorios_items = [
        ("Alfombra Del", report_data.accesorios_alfombra_delantera),
        ("Alfombra Tras", report_data.accesorios_alfombra_trasera),
        ("Radio", report_data.accesorios_radio),
        ("Reproductor", report_data.accesorios_radio_reproductor),
        ("Antena Eléc", report_data.accesorios_antena_electrica),
        ("Encendedor", report_data.accesorios_encendedor_cigarrillos),
        ("Triángulo Seg", report_data.accesorios_triangulo_seguridad),
        ("Gato", report_data.accesorios_gato),
        ("Caucho Rep", report_data.accesorios_caucho_repuesto),
        ("Otro (Acces.)", report_data.accesorios_otro),
    ]
    story.append(create_checklist_table("Accesorios", accesorios_items))

    electrico_items = [
        ("Frenos Del", report_data.sistem_electric_frenos_del),
        ("Tablero", report_data.sistem_electric_tablero),
        ("Luz Cruce", report_data.sistem_electric_luz_cruce),
        ("Luz Stop", report_data.sistem_electric_stop),
        ("Vidrio Eléc", report_data.sistem_electric_vidrio_electrico),
        ("Aire Acond", report_data.sistem_electric_aire_acondicionado),
        ("Otro (Elec.)", report_data.sistem_electric_otro),
    ]
    story.append(create_checklist_table("Sistemas Eléctricos", electrico_items))

    # .. ........................................ Observaciones
    # Cuadro de texto para observacionesadicionales a los checklist.
    if report_data.observaciones:
        story.append(Paragraph("Observaciones Adicionales", styles["h3"]))
        story.append(
            Paragraph(
                report_data.observaciones.replace("\n", "<br/>"), styles["Normal"]
            )
        )

    # .. ................................ Servicios & Repuestos
    # Listas de servicios y repuestos con sus cantidades y totales.
    def create_items_table(title, header, rows):
        story.append(Paragraph(title, styles["h3"]))
        data = [header] + rows
        # Repartir el ancho: Item/Cant (10%), Precio (20%), Descripción (70%)
        col_w = [usable_width * 0.1, usable_width * 0.7, usable_width * 0.2]
        t = Table(data, colWidths=col_w)
        t.setStyle(
            TableStyle(
                [
                    ("GRID", (0, 0), (-1, -1), 0.5, colors.grey),
                    ("ALIGN", (2, 0), (2, -1), "RIGHT"),
                    ("FONTNAME", (0, 0), (-1, 0), "Helvetica-Bold"),
                    ("FONTSIZE", (0, 0), (-1, -1), 7.5),
                    ("BOTTOMPADDING", (0, 0), (-1, -1), 1),
                    ("TOPPADDING", (0, 0), (-1, -1), 1),
                ]
            )
        )
        return t

    if report_data.servicios:
        rows = [
            [s.item, s.descripcion, f"{s.presupuesto:.2f}"]
            for s in report_data.servicios
        ]
        story.append(
            create_items_table(
                "Servicios Realizados", ["Item", "Descripción", "Presupuesto"], rows
            )
        )
        story.append(Spacer(1, 0.02 * inch))

    if report_data.repuestos:
        rows = [
            [r.cantidad, r.descripcion, f"{r.presupuesto:.2f}"]
            for r in report_data.repuestos
        ]
        story.append(
            create_items_table(
                "Repuestos Utilizados", ["Cant.", "Descripción", "Presupuesto"], rows
            )
        )
        story.append(Spacer(1, 0.02 * inch))

    # .. ..................... Totales -> Servicios & Repuestos
    # Tabla de totales para Servicio y Repuestos registrados.
    story.append(Spacer(1, 0.04 * inch))
    total_data = [
        ["Total Servicios:", f"{report_data.total_servicios or 0:.2f}"],
        ["Total Repuestos:", f"{report_data.total_repuestos or 0:.2f}"],
        ["Total General:", f"{report_data.total_general or 0:.2f}"],
    ]
    total_table = Table(total_data, colWidths=[usable_width - 1.2 * inch, 1.2 * inch])
    total_table.setStyle(
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
    story.append(total_table)

    # .. ........................................ Firma Cliente
    # Sección para firma de aprobación y aceptación por parte del cliente.
    story.append(Spacer(1, 0.3 * inch))
    firma_data = [
        ["", "________________________"],
        ["", Paragraph("Firma Cliente", styles["Signature"])],
    ]
    firma_table = Table(firma_data, colWidths=[usable_width - 2.5 * inch, 2.5 * inch])
    firma_table.setStyle(TableStyle([("ALIGN", (1, 0), (1, 1), "CENTER")]))
    story.append(firma_table)

    doc.build(story, onFirstPage=draw_footer, onLaterPages=draw_footer)
    buffer.seek(0)
    return buffer
