from data.database import SessionLocal, create_db_tables
from data.models import ReportesDB, ServiciosDB, RepuestosDB
from datetime import date
from faker import Faker
import random

def create_fake_records():
    """
    Crea 10 registros falsos en la base de datos utilizando la librería Faker.
    """
    # 1. Inicializar Faker para generar datos en español
    fake = Faker('es_ES')

    # 2. Asegurar que las tablas de la base de datos existan
    print("Asegurando que las tablas de la base de datos existan...")
    create_db_tables()
    
    # 3. Iniciar sesión de base de datos
    db = SessionLocal()
    
    try:
        print("Iniciando la inserción de 10 registros de prueba...")
        for i in range(10):
            # --- Generación de datos para el Reporte ---
            report_data = {
                "placa": fake.bothify(text='???####', letters='ABCDEFGHIJKLMNOPQRSTUVWXYZ'),
                "modelo": random.choice(["Toyota Corolla", "Honda Civic", "Ford Fiesta", "Chevrolet Spark", "Hyundai Tucson"]),
                "color": fake.color_name(),
                "cedula_cliente": int(fake.unique.random_number(digits=8, fix_len=True)),
                "nombre_cliente": fake.name(),
                "telefono_cliente": int(fake.msisdn()[:10]),
                "observaciones": fake.sentence(nb_words=10),
                "status_reporte": random.choice(["activa", "anulada"]),
                # Checklist aleatorio
                "carroceria_golpe": random.choice([True, False]),
                "carroceria_rayas": random.choice([True, False]),
                "carroceria_suelto": random.choice([True, False]),
                "accesorios_radio": random.choice([True, False]),
                "accesorios_encendedor_cigarrillos": random.choice([True, False]),
                "accesorios_alfombra_delantera": random.choice([True, False]),
                "accesorios_alfombra_trasera": random.choice([True, False]),
                "sistem_electric_frenos_del": random.choice([True, False]),
                "sistem_electric_tablero": random.choice([True, False]),
                "sistem_electric_aire_acondicionado": random.choice([True, False]),
            }
            nuevo_reporte = ReportesDB(**report_data)

            # --- Generación de Servicios ---
            servicios_a_crear = []
            total_servicios = 0
            for item_num in range(1, random.randint(2, 5)):
                presupuesto = round(random.uniform(20.0, 150.0), 2)
                servicio = ServiciosDB(
                    item=item_num, 
                    descripcion=fake.bs(), 
                    presupuesto=presupuesto
                )
                servicios_a_crear.append(servicio)
                total_servicios += presupuesto
            
            nuevo_reporte.servicios.extend(servicios_a_crear)

            # --- Generación de Repuestos ---
            repuestos_a_crear = []
            total_repuestos = 0
            for _ in range(random.randint(1, 6)):
                presupuesto = round(random.uniform(5.0, 300.0), 2)
                repuesto = RepuestosDB(
                    cantidad=random.randint(1, 5),
                    descripcion=f"{fake.word().capitalize()} para {report_data['modelo']}",
                    presupuesto=presupuesto
                )
                repuestos_a_crear.append(repuesto)
                total_repuestos += presupuesto
            
            nuevo_reporte.repuestos.extend(repuestos_a_crear)

            # --- Asignación de Totales ---
            nuevo_reporte.total_servicios = total_servicios
            nuevo_reporte.total_repuestos = total_repuestos
            nuevo_reporte.total_general = total_servicios + total_repuestos
            
            # --- Guardado en DB ---
            db.add(nuevo_reporte)
            db.commit()
            db.refresh(nuevo_reporte)
            
            print(f"✅ Registro #{i+1} creado con ID: {nuevo_reporte.id_reporte} para Placa: {nuevo_reporte.placa}")

        print("\n" + "="*40)
        print("   🎉 ¡Proceso completado! 🎉")
        print("Se han insertado 10 registros en la base de datos.")
        print("="*40)

    except Exception as e:
        print(f"❌ Ocurrió un error durante la inserción: {e}")
        db.rollback()
    finally:
        db.close()
        print("Conexión a la base de datos cerrada.")

if __name__ == "__main__":
    create_fake_records()