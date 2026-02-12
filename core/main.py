# MODULO: core/main.py
# Archivo de lanzamiento de la app, almacén de endpoints.

from contextlib import asynccontextmanager
from pathlib import Path

from fastapi import FastAPI, HTTPException
from starlette.responses import HTMLResponse
from starlette.staticfiles import StaticFiles

from api.routes import reports
from data.database import create_db_tables


# Verificación de que las tablas esten creadas al iniciar la app.
@asynccontextmanager
async def lifespan(app: FastAPI):
    """
    Gestión del ciclo de vida de la aplicación.
    Se ejecuta al iniciar y cerrar el servidor.
    """
    create_db_tables()
    yield


app = FastAPI(
    title="Reporte de Servicios",
    description="Aplicación para generar reportes de servicios",
    version="1.0.0",
    lifespan=lifespan,
    contact={
        "name": "Gustavo Colmenares | GUScode",
        "email": "g_colmenares9481@proton.me",
    },
    license_info={
        "name": "MIT License",
        "url": "https://opensource.org/licenses/MIT",
    },
)

# Montado de la carpeta 'interface' como estáticos en '/static/'.
app.mount("/static", StaticFiles(directory="interface"), name="static")

# Incluir routers
app.include_router(reports.router)


# .. ..................................................... endpoint -> root ..󰌠
# Entrada a la app
@app.get("/", response_class=HTMLResponse, include_in_schema=False)  # oculta de /docs
async def serve_index_html():
    """Sirve el archivo HTML a la página de inicio"""
    html_file_path = Path("interface/index.html")
    if not html_file_path.is_file():
        raise HTTPException(status_code=404, detail="Archivo index no encontrado")
    return html_file_path.read_text()


# .. .............................................. endpoint -> /api/status ..󰌠
# Mensaje de conexión de la api.
@app.get("/api/status")
def get_api_status():
    """Test para raíz de la api, sirve un mensaje"""
    return {"API -> Reportes de taller | Bienvenido !!"}
