import pytest
from fastapi import status
from datetime import date

def test_create_report(client):
    """Prueba la creación de un nuevo reporte con servicios y repuestos."""
    report_data = {
        "placa": "ABC1234",
        "modelo": "Toyota Corolla",
        "color": "Blanco",
        "cedula_cliente": 12345678,
        "nombre_cliente": "Gustavo Prueba",
        "telefono_cliente": 5550123,
        "fecha": str(date.today()),
        "status_reporte": "activa",
        "servicios": [
            {"item": 1, "descripcion": "Cambio de aceite", "presupuesto": 50.0}
        ],
        "repuestos": [
            {"cantidad": 1, "descripcion": "Filtro de aceite", "presupuesto": 15.0}
        ]
    }
    response = client.post("/reportes/", json=report_data)
    assert response.status_code == status.HTTP_201_CREATED
    data = response.json()
    assert data["placa"] == "ABC1234"
    assert len(data["servicios"]) == 1
    assert len(data["repuestos"]) == 1
    # Verificar cálculo de totales (50 + 15 = 65)
    assert data["total_general"] == 65.0

def test_get_reports(client):
    """Prueba la obtención de la lista de reportes."""
    # Primero creamos uno para asegurar que hay datos
    client.post("/reportes/", json={
        "placa": "LIST123", "modelo": "X", "color": "Y", 
        "cedula_cliente": 1, "nombre_cliente": "Z", "telefono_cliente": 2,
        "servicios": [], "repuestos": []
    })
    
    response = client.get("/reportes/")
    assert response.status_code == status.HTTP_200_OK
    data = response.json()
    assert "total_count" in data
    assert "reports" in data
    assert len(data["reports"]) >= 1

def test_get_report_by_id(client):
    """Prueba la obtención de un reporte por su ID."""
    create_resp = client.post("/reportes/", json={
        "placa": "IDTEST1", "modelo": "X", "color": "Y", 
        "cedula_cliente": 1, "nombre_cliente": "Z", "telefono_cliente": 2,
        "servicios": [], "repuestos": []
    })
    assert create_resp.status_code == status.HTTP_201_CREATED
    data = create_resp.json()
    assert "id_reporte" in data, f"id_reporte no encontrado en la respuesta: {data}"
    report_id = data["id_reporte"]
    
    response = client.get(f"/reportes/{report_id}")
    assert response.status_code == status.HTTP_200_OK
    assert response.json()["id_reporte"] == report_id

def test_get_report_not_found(client):
    """Prueba que un reporte inexistente devuelva 404."""
    response = client.get("/reportes/99999")
    assert response.status_code == status.HTTP_404_NOT_FOUND

def test_search_reports_by_plate(client):
    """Prueba la búsqueda de reportes por placa."""
    client.post("/reportes/", json={
        "placa": "SEARCH1", "modelo": "X", "color": "Y", 
        "cedula_cliente": 1, "nombre_cliente": "Z", "telefono_cliente": 2,
        "servicios": [], "repuestos": []
    })
    
    response = client.get("/reportes/placa/SEARCH1")
    assert response.status_code == status.HTTP_200_OK
    assert len(response.json()) >= 1
    assert response.json()[0]["placa"] == "SEARCH1"

def test_update_report(client):
    """Prueba la actualización de un reporte existente."""
    create_resp = client.post("/reportes/", json={
        "placa": "OLDPLC", "modelo": "X", "color": "Y", 
        "cedula_cliente": 1, "nombre_cliente": "Z", "telefono_cliente": 2,
        "servicios": [], "repuestos": []
    })
    assert create_resp.status_code == status.HTTP_201_CREATED
    data = create_resp.json()
    assert "id_reporte" in data, f"id_reporte no encontrado en la respuesta: {data}"
    report_id = data["id_reporte"]
    
    update_data = data
    update_data["placa"] = "NEWPLC"
    
    response = client.put(f"/reportes/{report_id}", json=update_data)
    assert response.status_code == status.HTTP_200_OK
    assert response.json()["placa"] == "NEWPLC"

def test_delete_report(client):
    """Prueba la eliminación de un reporte."""
    create_resp = client.post("/reportes/", json={
        "placa": "DELTEST", "modelo": "X", "color": "Y", 
        "cedula_cliente": 1, "nombre_cliente": "Z", "telefono_cliente": 2,
        "servicios": [], "repuestos": []
    })
    assert create_resp.status_code == status.HTTP_201_CREATED
    data = create_resp.json()
    assert "id_reporte" in data
    report_id = data["id_reporte"]
    
    response = client.delete(f"/reportes/{report_id}")
    assert response.status_code == status.HTTP_200_OK
    
    # Confirmar que ya no existe
    get_resp = client.get(f"/reportes/{report_id}")
    assert get_resp.status_code == status.HTTP_404_NOT_FOUND
