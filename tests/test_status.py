from fastapi import status

def test_api_status(client):
    """Verifica que el endpoint de estado de la API responda correctamente."""
    response = client.get("/api/status")
    assert response.status_code == status.HTTP_200_OK
    assert response.json() == {"status": "API -> Reportes de taller | Bienvenido !!"}

def test_serve_index_html(client):
    """Verifica que la raíz de la aplicación sirva el archivo index.html o un 404 si no existe."""
    response = client.get("/")
    # Si el archivo existe, debería ser 200. Si no, 404 según la lógica en core/main.py
    if response.status_code == status.HTTP_200_OK:
        assert "<html" in response.text.lower()
    else:
        assert response.status_code == status.HTTP_404_NOT_FOUND
        assert response.json()["detail"] == "Archivo index no encontrado"
