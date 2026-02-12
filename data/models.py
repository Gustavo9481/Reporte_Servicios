# MODULO: data
# Modelos para base de datos

from datetime import date
from typing import List, Literal, Optional

from sqlalchemy import Boolean, Column, Date, Float, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from .database import Base

# .. ................................................... Modelos SQLAlchemy ..󰌠
# Definición de las estructuras de las tablas


class ServiciosDB(Base):
    """Tabla de Servicios"""

    __tablename__ = "servicios"
    id_servicio = Column(Integer, primary_key=True, index=True)
    id_reporte = Column(Integer, ForeignKey("reportes.id_reporte"))
    item = Column(Integer, nullable=False)
    descripcion = Column(String, nullable=False)
    presupuesto = Column(Float, nullable=False, default=0.0)
    reporte = relationship("ReportesDB", back_populates="servicios")


class RepuestosDB(Base):
    """Tabla de Repuestos"""

    __tablename__ = "repuestos"
    id_repuesto = Column(Integer, primary_key=True, index=True)
    id_reporte = Column(Integer, ForeignKey("reportes.id_reporte"))
    cantidad = Column(Integer, nullable=False)
    descripcion = Column(String, nullable=False)
    presupuesto = Column(Float, nullable=False, default=0.0)
    reporte = relationship("ReportesDB", back_populates="repuestos")


class ReportesDB(Base):
    """Tabla de Reportes (principal)"""

    __tablename__ = "reportes"
    id_reporte = Column(Integer, primary_key=True, index=True)
    placa = Column(String, index=True, nullable=False)
    modelo = Column(String, nullable=False)
    color = Column(String, nullable=False)
    cedula_cliente = Column(Integer, nullable=False)
    nombre_cliente = Column(String, nullable=False)
    telefono_cliente = Column(Integer, nullable=False)
    fecha = Column(Date, nullable=False, default=date.today)
    status_reporte = Column(String, default="activa", nullable=False)
    factura_reporte = Column(String, nullable=True)
    factura_monto = Column(Float, nullable=True)

    # Sección CARROCERÍA.
    carroceria_golpe = Column(Boolean, default=False, nullable=False)
    carroceria_suelto = Column(Boolean, default=False, nullable=False)
    carroceria_rayas = Column(Boolean, default=False, nullable=False)
    carroceria_desconchado = Column(Boolean, default=False, nullable=False)
    carroceria_vidrio_roto = Column(Boolean, default=False, nullable=False)
    carroceria_falta_moldura = Column(Boolean, default=False, nullable=False)
    carroceria_falta_faro = Column(Boolean, default=False, nullable=False)
    carroceria_falta_accesorio = Column(Boolean, default=False, nullable=False)
    carroceria_espejo_roto = Column(Boolean, default=False, nullable=False)
    carroceria_falta_centro_copas = Column(Boolean, default=False, nullable=False)
    carroceria_otro = Column(Boolean, default=False, nullable=True)

    # Sección ACCESORIOS.
    accesorios_alfombra_delantera = Column(Boolean, default=False, nullable=False)
    accesorios_alfombra_trasera = Column(Boolean, default=False, nullable=False)
    accesorios_radio = Column(Boolean, default=False, nullable=False)
    accesorios_radio_reproductor = Column(Boolean, default=False, nullable=False)
    accesorios_antena_electrica = Column(Boolean, default=False, nullable=False)
    accesorios_encendedor_cigarrillos = Column(Boolean, default=False, nullable=False)
    accesorios_triangulo_seguridad = Column(Boolean, default=False, nullable=False)
    accesorios_gato = Column(Boolean, default=False, nullable=False)
    accesorios_caucho_repuesto = Column(Boolean, default=False, nullable=False)
    accesorios_otro = Column(Boolean, default=False, nullable=True)

    # Sección SISTEMAS ELECTRICOS.
    sistem_electric_frenos_del = Column(Boolean, default=False, nullable=False)
    sistem_electric_tablero = Column(Boolean, default=False, nullable=False)
    sistem_electric_luz_cruce = Column(Boolean, default=False, nullable=False)
    sistem_electric_stop = Column(Boolean, default=False, nullable=False)
    sistem_electric_vidrio_electrico = Column(Boolean, default=False, nullable=False)
    sistem_electric_aire_acondicionado = Column(Boolean, default=False, nullable=False)
    sistem_electric_otro = Column(Boolean, default=False, nullable=True)

    observaciones = Column(String, nullable=True)
    total_servicios = Column(Float, nullable=True)
    total_repuestos = Column(Float, nullable=True)
    total_general = Column(Float, nullable=True)

    servicios = relationship(
        "ServiciosDB", back_populates="reporte", cascade="all, delete-orphan"
    )
    repuestos = relationship(
        "RepuestosDB", back_populates="reporte", cascade="all, delete-orphan"
    )


