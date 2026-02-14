# MODULO: data/schemas.py
""" Schemas de datos. 
    Validación de entradas y salidas por medio de pydantic | solicitudes http.
"""

from datetime import date
from typing import List, Literal, Optional
from pydantic import BaseModel, Field


# .. ............................................................ SERVICIOS ..󰌠
class Servicio(BaseModel):
    """ Tabla de SERVICIOS. """

    id_servicio: Optional[int] = Field(None, description="id autoincrementable")
    id_reporte: Optional[int] = Field(None, description="relación con REPORTES")
    item: int = Field(..., description="número identificador del servicio")
    descripcion: str = Field(..., description="descripción detallada del servicio")
    presupuesto: float = Field(..., description="Costo presupuestado del servicio")


# .. ............................................................ REPUESTOS ..󰌠
class Repuesto(BaseModel):
    """ Tabla de REPUESTOS. """

    id_repuesto: Optional[int] = Field(None, description="id autoincrementable")
    id_reporte: Optional[int] = Field(None, description="relación con REPORTES")
    cantidad: int = Field(..., description="cantidad de repuestos solicitados")
    descripcion: str = Field(..., description="descripción detallada del repuesto")
    presupuesto: float = Field(..., description="Costo presupuestado del repuesto")


# .. ............................................................. REPORTES ..󰌠
class Reporte(BaseModel):
    """ Tabla de REPORTES (principal). """

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

    # .. ...................................... class -> config
    class Config:
        """ Clase de configuración, ayuda a pydantic a tener claro como deben
        estar estructurados los datos de los modelos.
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


# .. ............................................... PAGINACIÓN DE REPORTES ..󰌠
class PaginatedReportsResponse(BaseModel):
    """ Clase que otorga los valores necesarios para la paginación de los
    reportes en la opción 'Lista de Reportes'. """

    total_count: int
    reports: List[Reporte]
