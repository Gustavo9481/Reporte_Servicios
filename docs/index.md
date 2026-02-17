# Reporte Servicios

Bienvenido a la documentación del proyecto **Reporte Servicios**.

Este proyecto es una API de gestión para un taller mecánico, permitiendo la creación, consulta y descarga en PDF de reportes de servicio detallados.

## Características

- Gestión de reportes de servicio (CRUD).
- Generación automática de PDFs con ReportLab.
- Base de datos SQLite gestionada con SQLAlchemy.
- Validación de datos con Pydantic.

## Estructura del Proyecto

- `api/`: Endpoints de la API FastAPI.
- `core/`: Lógica central del negocio (generación de PDF, etc.).
- `data/`: Modelos de base de datos y esquemas.
- `interface/`: (Si aplica) Interfaz de usuario.

## Instalación

1. Clona el repositorio.
2. Crea un entorno virtual: `python -m venv .venv`
3. Activa el entorno: `source .venv/bin/activate`
4. Instala las dependencias: `pip install -r requirements.txt` (si existe) o instala manualmente las necesarias.

## Ejecución

Para iniciar el servidor de desarrollo:

```bash
uvicorn main:app --reload --port 8000
```
