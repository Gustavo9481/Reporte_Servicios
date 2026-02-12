from typing import List, Dict

from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session, joinedload
from starlette.responses import StreamingResponse

from core.pdf_generator import generate_report_pdf
from data import models, schemas
from data.database import get_db

router = APIRouter(
    prefix="/reportes",
    tags=["Reportes"]
)


# .. ............................................... endpoint -> /reportes/ ..󰌠
# Creación de nuevos reportes.
@router.post(
    "/",
    response_model=schemas.Reporte,
    status_code=status.HTTP_201_CREATED,
)
def create_reporte(reporte: schemas.Reporte, db: Session = Depends(get_db)):
    """Crea un nuevo reporte en la base de datos junto a los totales de
    Servicios, Repuestos y Total General.
    """
    # 1. calcular totales de Servicios, Repuestos y Total General.
    total_servicios = sum(s.presupuesto for s in reporte.servicios)
    total_repuestos = sum(r.presupuesto for r in reporte.repuestos)
    total_general = total_servicios + total_repuestos

    # 2. crear el objeto principal 'ReportesDB' a partir del modelo pydantic.
    # incluye totales de Servicios y Repuestos.
    reporte_data = reporte.dict(exclude={"servicios", "repuestos"})
    reporte_data.update(
        {
            "total_servicios": total_servicios,
            "total_repuestos": total_repuestos,
            "total_general": total_general,
        }
    )
    reporte_db = models.ReportesDB(**reporte_data)

    # 3. crear los objetos 'ServiciosDB' y 'RepuestosDB' y los agrega a la creación.
    for servicio_in in reporte.servicios:
        reporte_db.servicios.append(models.ServiciosDB(**servicio_in.dict()))

    for repuesto_in in reporte.repuestos:
        reporte_db.repuestos.append(models.RepuestosDB(**repuesto_in.dict()))

    # 4. agregar el reporte a la sesión de la base de datos y guardar.
    db.add(reporte_db)
    db.commit()

    # 5. refrescar el objeto para obtener los IDs generados por la base de datos.
    db.refresh(reporte_db)

    return reporte_db


# .. ............................................... endpoint -> /reportes/ ..󰌠
# lista de reportes existentes
@router.get("/", response_model=schemas.PaginatedReportsResponse)
def lista_reportes(skip: int = 0, limit: int = 15, db: Session = Depends(get_db)):
    """Lista de reportes existentes, ordenados por los más recientes primero, con paginación"""
    total_reportes = db.query(models.ReportesDB).count()
    reportes = (
        db.query(models.ReportesDB)
        .options(joinedload(models.ReportesDB.servicios))
        .options(joinedload(models.ReportesDB.repuestos))
        .order_by(models.ReportesDB.id_reporte.desc())
        .offset(skip)
        .limit(limit)
        .all()
    )
    return {"total_count": total_reportes, "reports": reportes}


# .. ................................... endpoint -> /reportes/{reporte_id} ..󰌠
# Filtro de búsqueda por id de orden.
@router.get("/{reporte_id}", response_model=schemas.Reporte)
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


# .. ....................... endpoint -> /reportes/cliente/{cedula_cliente} ..󰌠
# Filtro de búsqueda por cédula cliente.
@router.get(
    "/cliente/{cedula_cliente}",
    response_model=List[schemas.Reporte],
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


# .. ........................ endpoint -> /reportes/cliente/nombre/{nombre} ..󰌠
# Filtro de búsqueda por nombre de cliente.
@router.get(
    "/cliente/nombre/{nombre}",
    response_model=List[schemas.Reporte],
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
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Nombre de cliente no encontrado",
        )

    return reportes


# .. .................... endpoint -> /reportes/cliente/telefono/{telefono} ..󰌠
# Filtro de búsqueda por teléfono de cliente.
@router.get(
    "/cliente/telefono/{telefono}",
    response_model=List[schemas.Reporte],
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


# .. .................................. endpoint -> /reportes/placa/{placa} ..󰌠
# Filtro de búsqueda por placa de vehículo.
@router.get(
    "/placa/{placa}",
    response_model=List[schemas.Reporte],
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
            status_code=status.HTTP_404_NOT_FOUND,
            detail="No se encontraron reportes para esta placa",
        )

    return reportes


# .. ................................... endpoint -> /reportes/{reporte_id} ..󰌠
# Edición de un registro
@router.put("/{reporte_id}", response_model=schemas.Reporte)
def update_reporte(
    reporte_id: int, reporte_update: schemas.Reporte, db: Session = Depends(get_db)
):
    """Actuliza los datos de un reporte filtrado por id"""
    # filtrado del reporte a actualizar.
    reporte_db = (
        db.query(models.ReportesDB)
        .filter(models.ReportesDB.id_reporte == reporte_id)
        .first()
    )
    if reporte_db is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Reporte no encontrado"
        )

    # cálculo de totales de servicios y repuestos.
    total_servicios = sum(s.presupuesto for s in reporte_update.servicios)
    total_repuestos = sum(r.presupuesto for r in reporte_update.repuestos)

    # ctualización de los campos del reporte, incluyendo los totales.
    update_data = reporte_update.dict(
        exclude_unset=True, exclude={"servicios", "repuestos"}
    )
    update_data["total_servicios"] = total_servicios
    update_data["total_repuestos"] = total_repuestos
    update_data["total_general"] = total_servicios + total_repuestos
    for key, value in update_data.items():
        setattr(reporte_db, key, value)

    # actualización de servicios y repuestos (método simple: borrar y recrear).
    reporte_db.servicios = []
    reporte_db.repuestos = []
    for servicio_in in reporte_update.servicios:
        reporte_db.servicios.append(models.ServiciosDB(**servicio_in.dict()))
    for repuesto_in in reporte_update.repuestos:
        reporte_db.repuestos.append(models.RepuestosDB(**repuesto_in.dict()))

    # guardar cambios, refrescar y devolver el objeto actualizado.
    db.commit()
    db.refresh(reporte_db)

    return reporte_db


# .. ................................... endpoint -> /reportes/{reporte_id} ..󰌠
# Eliminar un registro
@router.delete("/{reporte_id}", status_code=status.HTTP_200_OK)
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


# .. ............................... endpoint -> /reportes/{reporte_id}/pdf ..󰌠
# Generación de reporte en formato pdf.
@router.get("/{reporte_id}/pdf")
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

    # Generar el PDF.
    pdf_buffer = generate_report_pdf(reporte)
    pdf_buffer.seek(0)  # Asegurarse de que el buffer esté al principio

    # Devolver el PDF como una respuesta de streaming
    filename = f"reporte_{reporte_id}_{reporte.placa}.pdf"
    return StreamingResponse(
        pdf_buffer,
        media_type="application/pdf",
        headers={"Content-Disposition": f"attachment; filename={filename}"},
    )
