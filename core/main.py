# MODULO: core/main.py
# Archivo de lanzamiento de la app, almacén de endpoints.

from contextlib import asynccontextmanager
from pathlib import Path
from typing import Dict, List

from fastapi import Depends, FastAPI, HTTPException, status
from sqlalchemy.orm import Session, joinedload
from starlette.applications import AppType
from starlette.responses import (
    HTMLResponse,
    StreamingResponse,
)
from starlette.staticfiles import StaticFiles

from core.pdf_generator import generate_report_pdf
from data import models
from data.database import create_db_tables, get_db


@asynccontextmanager
async def lifespan(app: FastAPI):
    """
    Gestión del ciclo de vida de la aplicación.
    Se ejecuta al iniciar y cerrar el servidor.
    """
    create_db_tables()
    yield


app = FastAPI(
    title="Reporte de Servicios",
    description="Aplicación para generar reportes de servicios",
    version="1.0.0",
    lifespan=lifespan,
    contact={
        "name": "Gustavo Colmenares | GUScode",
        "email": "g_colmenares9481@proton.me",
    },
    license_info={
        "name": "MIT License",
        "url": "https://opensource.org/licenses/MIT",
    },
)

# Montado de la carpeta 'interface'
# todos sus archivos estarán disponibles bajo la ruta '/static/'
app.mount("/interface", StaticFiles(directory="interface"), name="interface")
app.mount("/static", StaticFiles(directory="interface"), name="static")


# .. ..................................................... endpoint -> root ..󰌠
# ENDPOINT: entrada a la app
@app.get("/", response_class=HTMLResponse, include_in_schema=False)  # oculta de /docs
async def serve_index_html():
    """Sirve el archivo HTML a la página de inicio"""
    html_file_path = Path("interface/index.html")
    if not html_file_path.is_file():
        raise HTTPException(status_code=404, detail="Archivo index no encontrado")
    return html_file_path.read_text()


# ENDPOINT: mensaje de conexión de la api.
@app.get("/api/status")
def get_api_status():
    """Test para raíz de la api, sirve un mensaje"""
    return {"API -> Reportes de taller | Bienvenido !!"}


# ENDPOINT: creación de nuevos reportes
@app.post(
    "/reportes/",
    response_model=models.Reporte,
    status_code=status.HTTP_201_CREATED,
    tags=["Reportes"],
)
def create_reporte(reporte: models.Reporte, db: Session = Depends(get_db)):
    """Crea un nuevo reporte en la base de datos"""
    # 1. calcular totales
    total_servicios = sum(s.presupuesto for s in reporte.servicios)
    total_repuestos = sum(r.presupuesto for r in reporte.repuestos)
    total_general = total_servicios + total_repuestos

    # 2. crear el objeto principal 'ReportesDB' a partir del modelo pydantic, incluyendo totales
    reporte_data = reporte.dict(exclude={"servicios", "repuestos"})
    reporte_data.update(
        {
            "total_servicios": total_servicios,
            "total_repuestos": total_repuestos,
            "total_general": total_general,
        }
    )
    reporte_db = models.ReportesDB(**reporte_data)

    # 3. crear los objetos 'ServiciosDB' y 'RepuestosDB' y los agrega a la creación
    for servicio_in in reporte.servicios:
        reporte_db.servicios.append(models.ServiciosDB(**servicio_in.dict()))

    for repuesto_in in reporte.repuestos:
        reporte_db.repuestos.append(models.RepuestosDB(**repuesto_in.dict()))

    # 4. agregar el reporte a la sesión de la base de datos y guardar
    db.add(reporte_db)
    db.commit()

    # 5. refrescar el objeto para obtener los IDs generados por la base de datos
    db.refresh(reporte_db)

    return reporte_db


# ENDPOINT: lista de reportes existentes
@app.get("/reportes/", response_model=List[models.Reporte], tags=["Reportes"])
def lista_reportes(db: Session = Depends(get_db)):
    """Lista de reportes existentes"""
    reportes = (
        db.query(models.ReportesDB)
        .options(joinedload(models.ReportesDB.servicios))
        .options(joinedload(models.ReportesDB.repuestos))
        .all()
    )
    return reportes


# ENDPOINT: filtro de búsqueda por id de orden
@app.get("/reportes/{reporte_id}", response_model=models.Reporte, tags=["Reportes"])
def leer_reporte(reporte_id: int, db: Session = Depends(get_db)):
    """Lee un reporte en específoco por id"""
    reporte = (
        db.query(models.ReportesDB)
        .options(joinedload(models.ReportesDB.servicios))
        .options(joinedload(models.ReportesDB.repuestos))
        .filter(models.ReportesDB.id_reporte == reporte_id)
        .first()
    )

    if reporte is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Reporte no encontrado"
        )
    return reporte


# ENDPOINT: filtro de búsqueda por cédula cliente.
@app.get(
    "/reportes/cliente/{cedula_cliente}",
    response_model=List[models.Reporte],
    tags=["Reportes"],
)
def find_cedula(cedula_cliente: int, db: Session = Depends(get_db)):
    """Lee un reporte en específico por cédula de cliente"""
    reportes = (
        db.query(models.ReportesDB)
        .options(joinedload(models.ReportesDB.servicios))
        .options(joinedload(models.ReportesDB.repuestos))
        .filter(models.ReportesDB.cedula_cliente == cedula_cliente)
        .all()
    )

    if not reportes:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Cliente no encontrado"
        )

    return reportes


# ENDPOINT: filtro de búsqueda por nombre de cliente.
@app.get(
    "/reportes/cliente/nombre/{nombre}",
    response_model=List[models.Reporte],
    tags=["Reportes"],
)
def find_nombre(nombre: str, db: Session = Depends(get_db)):
    """Lee reportes asociados a un nombre de cliente (coincidencia parcial)"""
    reportes = (
        db.query(models.ReportesDB)
        .options(joinedload(models.ReportesDB.servicios))
        .options(joinedload(models.ReportesDB.repuestos))
        .filter(models.ReportesDB.nombre_cliente.ilike(f"%{nombre}%"))
        .all()
    )

    if not reportes:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Nombre de cliente no encontrado"
        )

    return reportes


# ENDPOINT: filtro de búsqueda por teléfono de cliente.
@app.get(
    "/reportes/cliente/telefono/{telefono}",
    response_model=List[models.Reporte],
    tags=["Reportes"],
)
def find_telefono(telefono: int, db: Session = Depends(get_db)):
    """Lee reportes asociados a un número de teléfono específico"""
    reportes = (
        db.query(models.ReportesDB)
        .options(joinedload(models.ReportesDB.servicios))
        .options(joinedload(models.ReportesDB.repuestos))
        .filter(models.ReportesDB.telefono_cliente == telefono)
        .all()
    )

    if not reportes:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Teléfono no encontrado"
        )

    return reportes


# ENDPOINT: filtro de búsqueda por placa de vehículo.
@app.get(
    "/reportes/placa/{placa}",
    response_model=List[models.Reporte],
    tags=["Reportes"],
)
def find_placa(placa: str, db: Session = Depends(get_db)):
    """Lee reportes asociados a una placa de vehículo específica"""
    reportes = (
        db.query(models.ReportesDB)
        .options(joinedload(models.ReportesDB.servicios))
        .options(joinedload(models.ReportesDB.repuestos))
        .filter(models.ReportesDB.placa == placa)
        .all()
    )

    if not reportes:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="No se encontraron reportes para esta placa"
        )

    return reportes


# ENDPOINT: edición de un registro
@app.put("/reportes/{reporte_id}", response_model=models.Reporte, tags=["Reportes"])
def update_reporte(
    reporte_id: int, reporte_update: models.Reporte, db: Session = Depends(get_db)
):
    """Actuliza los datos de un reporte filtrado por id"""
    # 1. filtrar el reporte a actualizar
    reporte_db = (
        db.query(models.ReportesDB)
        .filter(models.ReportesDB.id_reporte == reporte_id)
        .first()
    )
    if reporte_db is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Reporte no encontrado"
        )

    # 2. calcular los nuevos totales
    total_servicios = sum(s.presupuesto for s in reporte_update.servicios)
    total_repuestos = sum(r.presupuesto for r in reporte_update.repuestos)

    # 3. actualizar los campos del reporte, incluyendo los totales
    update_data = reporte_update.dict(
        exclude_unset=True, exclude={"servicios", "repuestos"}
    )
    update_data["total_servicios"] = total_servicios
    update_data["total_repuestos"] = total_repuestos
    update_data["total_general"] = total_servicios + total_repuestos
    for key, value in update_data.items():
        setattr(reporte_db, key, value)

    # 4. actualizar servicios y repuestos (método simple: borrar y recrear)
    reporte_db.servicios = []
    reporte_db.repuestos = []
    for servicio_in in reporte_update.servicios:
        reporte_db.servicios.append(models.ServiciosDB(**servicio_in.dict()))
    for repuesto_in in reporte_update.repuestos:
        reporte_db.repuestos.append(models.RepuestosDB(**repuesto_in.dict()))

    # 5. guardar cambios, refrescar y devolver el objeto actualizado.
    db.commit()
    db.refresh(reporte_db)

    return reporte_db


# ENDPOINT: borrar un registro
@app.delete("/reportes/{reporte_id}", status_code=status.HTTP_200_OK, tags=["Reportes"])
def delete_reporte(reporte_id: int, db: Session = Depends(get_db)) -> Dict[str, str]:
    """Elimina un registro"""
    reporte_db = (
        db.query(models.ReportesDB)
        .filter(models.ReportesDB.id_reporte == reporte_id)
        .first()
    )

    if reporte_db is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Reporte no encontrado"
        )

    db.delete(reporte_db)
    db.commit()

    return {"message": f"Reporte con ID {reporte_id} eliminado exitosamente"}


# --- NUEVO ENDPOINT PARA GENERAR PDF ---
@app.get("/reportes/{reporte_id}/pdf", tags=["Reportes"])
async def get_reporte_pdf(reporte_id: int, db: Session = Depends(get_db)):
    """
    Genera y devuelve el PDF de un reporte específico.
    """
    reporte = (
        db.query(models.ReportesDB)
        .options(joinedload(models.ReportesDB.servicios))
        .options(joinedload(models.ReportesDB.repuestos))
        .filter(models.ReportesDB.id_reporte == reporte_id)
        .first()
    )

    if reporte is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Reporte no encontrado"
        )

    # Generar el PDF
    pdf_buffer = generate_report_pdf(reporte)
    pdf_buffer.seek(0)  # Asegurarse de que el buffer esté al principio

    # Devolver el PDF como una respuesta de streaming
    filename = f"reporte_{reporte_id}_{reporte.placa}.pdf"
    return StreamingResponse(
        pdf_buffer,
        media_type="application/pdf",
        headers={"Content-Disposition": f"attachment; filename={filename}"},
    )
