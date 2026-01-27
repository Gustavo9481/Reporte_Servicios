# MODULO: data
# Modelos para base de datos
from datetime import date
from typing import List, Literal, Optional

from pydantic import BaseModel, Field
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


# .. ..................................................... Modelos Pydantic ..󰌠
# Validación de datos entrada y salida | solicitudes http.


class Servicio(BaseModel):
    """Tabla de SERVICIOS"""

    id_servicio: Optional[int] = Field(None, description="id autoincrementable")
    id_reporte: Optional[int] = Field(None, description="relación con REPORTES")
    item: int = Field(..., description="número identificador del servicio")
    descripcion: str = Field(..., description="descripción detallada del servicio")
    presupuesto: float = Field(..., description="Costo presupuestado del servicio")


class Repuesto(BaseModel):
    """Tabla de REPUESTOS"""

    id_repuesto: Optional[int] = Field(None, description="id autoincrementable")
    id_reporte: Optional[int] = Field(None, description="relación con REPORTES")
    cantidad: int = Field(..., description="cantidad de repuestos solicitados")
    descripcion: str = Field(..., description="descripción detallada del repuesto")
    presupuesto: float = Field(..., description="Costo presupuestado del repuesto")


class Reporte(BaseModel):
    """Tabla de REPORTES (principal)"""

    id_reporte: Optional[int] = Field(None, description="id autoincrementable")
    placa: str = Field(..., max_length=7, description="matrícula del vehículo")
    modelo: str = Field(..., description="modelo del vehículo")
    color: str = Field(..., description="color del vehículo")
    cedula_cliente: int = Field(..., description="número identificación del cliente")
    nombre_cliente: str = Field(..., description="nombre del cliente")
    telefono_cliente: int = Field(..., description="número teléfono del cliente")
    fecha: date = Field(
        default_factory=date.today, description="fecha creación del reporte"
    )
    status_reporte: Literal["activa", "anulada"] = Field(
        "activa", description="estado del reporte -> activa | anulada"
    )
    factura_reporte: Optional[str] = Field(
        None, description="número de factura (en caso de estar facturado)"
    )
    factura_monto: Optional[float] = Field(
        None, description="monto de la factura (en caso de estar facturado)"
    )

    # Sección CARROCERÍA.
    carroceria_golpe: bool = Field(
        False, description="Vehículo presenta golpes en carrocería?"
    )
    carroceria_suelto: bool = Field(
        False, description="Vehículo presenta algún suelto en carrocería?"
    )
    carroceria_rayas: bool = Field(
        False, description="Vehículo presenta alguna raya en carrocería?"
    )
    carroceria_desconchado: bool = Field(
        False, description="Vehículo presenta algún desconchado en carrocería?"
    )
    carroceria_vidrio_roto: bool = Field(
        False, description="Vehículo presenta algún vidrio roto?"
    )
    carroceria_falta_moldura: bool = Field(
        False, description="Vehículo presenta falta de moldura?"
    )
    carroceria_falta_faro: bool = Field(
        False, description="Vehículo presenta falta de faro?"
    )
    carroceria_falta_accesorio: bool = Field(
        False, description="Vehículo presenta falta de accesorio?"
    )
    carroceria_espejo_roto: bool = Field(
        False, description="Vehículo presenta algún espejo roto?"
    )
    carroceria_falta_centro_copas: bool = Field(
        False, description="Vehículo presenta falta de centro de copas?"
    )
    carroceria_otro: bool = Field(
        False, description="Vehículo presenta algún otro problema en carrocería?"
    )

    # Sección ACCESORIOS.
    accesorios_alfombra_delantera: bool = Field(
        False, description="Falta alguna alfombra delantera al vehículo?"
    )
    accesorios_alfombra_trasera: bool = Field(
        False, description="Falta alguna alfombra trasera al vehículo?"
    )
    accesorios_radio: bool = Field(
        False, description="Falla o falta la radio del vehículo?"
    )
    accesorios_radio_reproductor: bool = Field(
        False, description="Falla o falta el reproductor de la radio"
    )
    accesorios_antena_electrica: bool = Field(
        False, description="Falta la antena eléctrica del vehículo?"
    )
    accesorios_encendedor_cigarrillos: bool = Field(
        False, description="Falta el encendedor de cigarrillos del vehículo?"
    )
    accesorios_triangulo_seguridad: bool = Field(
        False, description="Falta el triángulo de seguridad del vehículo?"
    )
    accesorios_gato: bool = Field(False, description="Falta el gato del vehículo?")
    accesorios_caucho_repuesto: bool = Field(
        False, description="Falta el caucho de repuesto del vehículo?"
    )
    accesorios_otro: bool = Field(
        False, description="Falta algún otro accesorio del vehículo?"
    )

    # Sección SISTEMA ELECTRICO.
    sistem_electric_frenos_del: bool = Field(
        False, description="Fallan los frenos delanteros?"
    )
    sistem_electric_tablero: bool = Field(
        False, description="Falla el tablero del vehículo?"
    )
    sistem_electric_luz_cruce: bool = Field(
        False, description="Falla la luz de cruce del vehículo?"
    )
    sistem_electric_stop: bool = Field(
        False, description="Falla la luz de stop del vehículo?"
    )
    sistem_electric_vidrio_electrico: bool = Field(
        False, description="Falla la luz del vidrio eléctrico del vehículo?"
    )
    sistem_electric_aire_acondicionado: bool = Field(
        False, description="Falla el aire acondicionado del vehículo?"
    )
    sistem_electric_otro: bool = Field(
        False, description="Falla algún otro sistema eléctrico del vehículo?"
    )

    observaciones: Optional[str] = Field(
        None, description="Observaciones o detalles extra del checklist"
    )
    total_servicios: Optional[float] = Field(
        None, description="Suma total del presupuesto de servicios"
    )
    total_repuestos: Optional[float] = Field(
        None, description="Suma total del presupuesto de repuestos"
    )
    total_general: Optional[float] = Field(
        None, description="Suma total de servicios y repuestos"
    )
    servicios: List[Servicio] = Field(
        [], description="Lista de servicios asociados al reporte"
    )
    repuestos: List[Repuesto] = Field(
        [], description="Lista de repuestos asociados al reporte"
    )

    class Config:
        """Clase de configuración, ayuda a pydantic a tener claro como deben estar
        estructurados los datos de los modelos.
        """

        from_attributes = True
        json_schema_extra = {
            "example": {
                "fecha": "2025-12-27",
                "placa": "PLA11CA",
                "modelo": "Modelo Vehículo",
                "color": "color",
                "cedula_cliente": 1111111,
                "nombre_cliente": "Nombre Cliente o Empresa",
                "telefono_cliente": 1234567890,
                "status_reporte": "activa",
                "servicios": [{"item": 1, "descripcion": "Descripción del servicio"}],
                "repuestos": [
                    {"cantidad": 1, "descripcion": "Descripción del repuesto"}
                ],
            }
        }
