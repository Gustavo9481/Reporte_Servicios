from data.database import SessionLocal, create_db_tables
from data.models import ReportesDB, ServiciosDB, RepuestosDB
from datetime import date

def test_database():
    # 1. Crear las tablas (o asegurar que existen)
    print("Iniciando creación de tablas...")
    create_db_tables()
    
    # 2. Iniciar sesión de base de datos
    db = SessionLocal()
    
    try:
        print("Insertando registro de prueba completo...")
        # 3. Crear un reporte principal
        nuevo_reporte = ReportesDB(
            placa="ABC1234",
            modelo="Toyota Corolla",
            color="Gris",
            cedula_cliente=12345678,
            nombre_cliente="Juan Pérez",
            telefono_cliente=5551234,
            observaciones="Revisión de los 50,000 km",
            # Checklist de ejemplo
            carroceria_golpe=True,
            accesorios_radio=True,
            sistem_electric_aire_acondicionado=True
        )
        
        # 4. Agregar Servicios (Relacionados)
        servicios = [
            ServiciosDB(item=1, descripcion="Cambio de Aceite y Filtro", presupuesto=60.0),
            ServiciosDB(item=2, descripcion="Alineación y Balanceo", presupuesto=40.0)
        ]
        nuevo_reporte.servicios.extend(servicios)
        
        # 5. Agregar Repuestos (Relacionados)
        repuestos = [
            RepuestosDB(cantidad=4, descripcion="Aceite Sintético 10W30", presupuesto=45.0),
            RepuestosDB(cantidad=1, descripcion="Filtro de Aceite Original", presupuesto=15.0)
        ]
        nuevo_reporte.repuestos.extend(repuestos)
        
        # Totales calculados (simulados para el test)
        nuevo_reporte.total_servicios = 100.0
        nuevo_reporte.total_repuestos = 60.0
        nuevo_reporte.total_general = 160.0
        
        # Guardar en la base de datos
        db.add(nuevo_reporte)
        db.commit()
        db.refresh(nuevo_reporte)
        
        print(f"✅ Registro creado exitosamente con ID: {nuevo_reporte.id_reporte}")
        
        # 6. Consultar y mostrar los datos guardados
        print("\n" + "="*30)
        print("CONSULTA DE RESULTADOS")
        print("="*30)
        
        reporte = db.query(ReportesDB).filter(ReportesDB.placa == "ABC1234").first()
        
        print(f"Reporte #: {reporte.id_reporte}")
        print(f"Cliente:   {reporte.nombre_cliente}")
        print(f"Vehículo:  {reporte.modelo} [{reporte.placa}]")
        print(f"Estado:    {reporte.status_reporte}")
        
        print("\nServicios asociados:")
        for s in reporte.servicios:
            print(f"  - {s.descripcion} (${s.presupuesto})")
            
        print("\nRepuestos asociados:")
        for r in reporte.repuestos:
            print(f"  - {r.cantidad}x {r.descripcion} (${r.presupuesto})")
            
        print(f"\nTOTAL GENERAL: ${reporte.total_general}")
        print("="*30)

    except Exception as e:
        print(f"❌ Error durante la prueba: {e}")
        db.rollback()
    finally:
        db.close()

if __name__ == "__main__":
    test_database()
