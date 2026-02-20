# Pruebas (Testing)

Este proyecto utiliza `pytest` como framework principal de pruebas para asegurar la calidad y el correcto funcionamiento de la API.

## Estructura de Pruebas

Las pruebas se encuentran en el directorio `tests/` y están organizadas de la siguiente manera:

*   **`conftest.py`**: Configuración de fixtures globales, incluyendo el cliente de prueba de FastAPI (`TestClient`) y la base de datos SQLite en memoria para aislamiento.
*   **`test_status.py`**: Pruebas de integración para verificar los endpoints base de la API.
*   **`test_reports.py`**: Pruebas de integración completas para el ciclo de vida de los reportes (CRUD).

## Ejecución de Pruebas

Para ejecutar la suite de pruebas completa, utiliza el siguiente comando desde la raíz del proyecto:

```bash
uv run pytest
```

### Comandos Útiles

*   **Ejecutar pruebas en silencio (solo fallos)**:
    ```bash
    uv run pytest -q
    ```
*   **Ejecutar una prueba específica**:
    ```bash
    uv run pytest tests/test_reports.py
    ```
*   **Ver la cobertura (si está instalado pytest-cov)**:
    ```bash
    uv run pytest --cov=.
    ```

## Cobertura de Funcionalidades

Las pruebas cubren actualmente:

1.  **Estado de la API**: Verificación del endpoint `/api/status`.
2.  **Interfaz**: Verificación de la carga del archivo `index.html`.
3.  **CRUD de Reportes**:
    *   Creación de reportes con servicios y repuestos.
    *   Cálculo automático de totales.
    *   Listado y paginación de reportes.
    *   Búsqueda por ID y por Placa.
    *   Actualización de datos.
    *   Eliminación de registros.

## TestSprite

El proyecto está preparado para la integración con **TestSprite** para validaciones adicionales de calidad y consistencia con el PRD.
