"""Contenedor de endpoints para la api.

Aplicación de APIRouter para la modularización de las rutas.
"""

from typing import List, Dict

from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.responses import StreamingResponse
from sqlalchemy.orm import Session, joinedload

from core.pdf import generate_report_pdf
from data import models, schemas
from data.database import get_db

# Instancia de APIRouter.
router = APIRouter(
    prefix="/reportes",
    tags=["Reportes"]
)


@router.post(
    "/",
    response_model=schemas.Reporte,
    status_code=status.HTTP_201_CREATED,
)
def create_report(reporte: schemas.Reporte, db: Session = Depends(get_db)):
    """Crea un nuevo reporte en la base de datos.

    Calcula automáticamente los totales de servicios y repuestos.

    Args:
        reporte: Esquema de datos del reporte a crear.
        db: Sesión de base de datos.

    Returns:
        El objeto ReportesDB creado.
    """
    # Cálculo de totales de Servicios, Repuestos y Total General.
    total_servicios = sum(s.presupuesto for s in reporte.servicios)
    total_repuestos = sum(r.presupuesto for r in reporte.repuestos)
    total_general = total_servicios + total_repuestos

    # Creación del objeto principal 'ReportesDB' a partir del modelo pydantic.
    reporte_data = reporte.dict(exclude={"servicios", "repuestos"})
    reporte_data.update(
        {
            "total_servicios": total_servicios,
            "total_repuestos": total_repuestos,
            "total_general": total_general,
        }
    )
    reporte_db = models.ReportesDB(**reporte_data)

    # Creación de los objetos 'ServiciosDB' y 'RepuestosDB'.
    for servicio_in in reporte.servicios:
        reporte_db.servicios.append(models.ServiciosDB(**servicio_in.dict()))

    for repuesto_in in reporte.repuestos:
        reporte_db.repuestos.append(models.RepuestosDB(**repuesto_in.dict()))

    # Agregar el reporte a la base de datos y guardar los cambios.
    db.add(reporte_db)
    db.commit()

    # Refrescar el objeto para obtener los IDs generados por la base de datos.
    db.refresh(reporte_db)

    return reporte_db


@router.get("/", response_model=schemas.PaginatedReportsResponse)
def get_reports(skip: int = 0, limit: int = 15, db: Session = Depends(get_db)):
    """Obtiene una lista paginada de reportes.

    Args:
        skip: Cantidad de registros a saltar (offset).
        limit: Cantidad máxima de registros a retornar.
        db: Sesión de base de datos.

    Returns:
        Un diccionario con el total de reportes y la lista de reportes para la página actual.
    """
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


@router.get("/{reporte_id}", response_model=schemas.Reporte)
def get_report_by_id(reporte_id: int, db: Session = Depends(get_db)):
    """Obtiene un reporte específico por su ID.

    Args:
        reporte_id: ID del reporte a buscar.
        db: Sesión de base de datos.

    Returns:
        El objeto ReportesDB encontrado.

    Raises:
        HTTPException: Si el reporte no existe.
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
    return reporte


@router.get(
    "/cliente/{cedula_cliente}",
    response_model=List[schemas.Reporte],
)
def get_reports_by_client_id(cedula_cliente: int, db: Session = Depends(get_db)):
    """Busca reportes por cédula del cliente.

    Args:
        cedula_cliente: Cédula del cliente.
        db: Sesión de base de datos.

    Returns:
        Lista de reportes encontrados.

    Raises:
        HTTPException: Si no se encuentran reportes para el cliente.
    """
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


@router.get(
    "/cliente/nombre/{nombre}",
    response_model=List[schemas.Reporte],
)
def get_reports_by_client_name(nombre: str, db: Session = Depends(get_db)):
    """Busca reportes por nombre del cliente (búsqueda parcial insensible a mayúsculas).

    Args:
        nombre: Nombre o fragmento del nombre del cliente.
        db: Sesión de base de datos.

    Returns:
        Lista de reportes encontrados.

    Raises:
        HTTPException: Si no se encuentran reportes.
    """
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


@router.get(
    "/cliente/telefono/{telefono}",
    response_model=List[schemas.Reporte],
)
def get_reports_by_client_phone(telefono: int, db: Session = Depends(get_db)):
    """Busca reportes por teléfono del cliente.

    Args:
        telefono: Número de teléfono del cliente.
        db: Sesión de base de datos.

    Returns:
        Lista de reportes encontrados.

    Raises:
        HTTPException: Si no se encuentran reportes.
    """
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


@router.get(
    "/placa/{placa}",
    response_model=List[schemas.Reporte],
)
def get_reports_by_plate(placa: str, db: Session = Depends(get_db)):
    """Busca reportes por placa del vehículo.

    Args:
        placa: Placa del vehículo.
        db: Sesión de base de datos.

    Returns:
        Lista de reportes encontrados.

    Raises:
        HTTPException: Si no se encuentran reportes.
    """
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


@router.put("/{reporte_id}", response_model=schemas.Reporte)
def update_report(
    reporte_id: int, reporte_update: schemas.Reporte, db: Session = Depends(get_db)
):
    """Actualiza los datos de un reporte existente.

    Args:
        reporte_id: ID del reporte a actualizar.
        reporte_update: Esquema con los nuevos datos del reporte.
        db: Sesión de base de datos.

    Returns:
        El objeto ReportesDB actualizado.

    Raises:
        HTTPException: Si el reporte no existe.
    """
    # Filtrado del reporte a actualizar.
    reporte_db = (
        db.query(models.ReportesDB)
        .filter(models.ReportesDB.id_reporte == reporte_id)
        .first()
    )
    if reporte_db is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Reporte no encontrado"
        )

    # Cálculo de totales de servicios y repuestos.
    total_servicios = sum(s.presupuesto for s in reporte_update.servicios)
    total_repuestos = sum(r.presupuesto for r in reporte_update.repuestos)

    # Actualización de los campos del reporte, incluyendo los totales.
    update_data = reporte_update.dict(
        exclude_unset=True, exclude={"servicios", "repuestos"}
    )
    update_data["total_servicios"] = total_servicios
    update_data["total_repuestos"] = total_repuestos
    update_data["total_general"] = total_servicios + total_repuestos
    for key, value in update_data.items():
        setattr(reporte_db, key, value)

    # Actualización de servicios y repuestos (método simple: borrar y recrear).
    reporte_db.servicios = []
    reporte_db.repuestos = []
    for servicio_in in reporte_update.servicios:
        reporte_db.servicios.append(models.ServiciosDB(**servicio_in.dict()))
    for repuesto_in in reporte_update.repuestos:
        reporte_db.repuestos.append(models.RepuestosDB(**repuesto_in.dict()))

    # Guardar cambios, refrescar y devolver el objeto actualizado.
    db.commit()
    db.refresh(reporte_db)

    return reporte_db


@router.delete("/clean", status_code=status.HTTP_200_OK)
def delete_old_reports(db: Session = Depends(get_db)):
    """Elimina los 10 reportes más antiguos de la base de datos.

    Args:
        db: Sesión de base de datos.

    Returns:
        Un mensaje con la cantidad de registros eliminados.
    """
    # Buscar los 10 IDs más bajos (ascendente).
    reportes = (
        db.query(models.ReportesDB)
        .order_by(models.ReportesDB.id_reporte.asc())
        .limit(10)
        .all()
    )

    if not reportes:
        return {"message": "No hay reportes para eliminar."}

    count = len(reportes)
    for r in reportes:
        db.delete(r)

    try:
        db.commit()
    except Exception as e:
        db.rollback()
        raise HTTPException(status_code=500, detail=f"Error al confirmar eliminación: {str(e)}")

    return {"message": f"Se han eliminado {count} reportes antiguos correctamente."}


@router.delete("/{reporte_id}", status_code=status.HTTP_200_OK)
def delete_report(reporte_id: int, db: Session = Depends(get_db)) -> Dict[str, str]:
    """Elimina un reporte por su ID.

    Args:
        reporte_id: ID del reporte a eliminar.
        db: Sesión de base de datos.

    Returns:
        Mensaje de confirmación.

    Raises:
        HTTPException: Si el reporte no existe.
    """
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


@router.get("/{reporte_id}/pdf")
async def get_report_pdf(reporte_id: int, db: Session = Depends(get_db)):
    """Genera y descarga el PDF de un reporte específico.

    Args:
        reporte_id: ID del reporte.
        db: Sesión de base de datos.

    Returns:
        StreamingResponse con el archivo PDF.

    Raises:
        HTTPException: Si el reporte no existe.
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
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Reporte no encontrado"
        )

    # Generar PDF.
    pdf_buffer = generate_report_pdf(reporte)
    # Asegurarse de que el buffer esté al principio.
    pdf_buffer.seek(0)

    # Devolver el PDF como una respuesta de streaming.
    filename = f"reporte_{reporte_id}_{reporte.placa}.pdf"
    return StreamingResponse(
        pdf_buffer,
        media_type="application/pdf",
        headers={"Content-Disposition": f"attachment; filename={filename}"},
    )
