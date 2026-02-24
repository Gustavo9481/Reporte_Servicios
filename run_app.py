"""Script de arranque para el ejecutable de Reporte_Servicios."""

import uvicorn
import webbrowser
import threading
import time
import os
import sys

# Asegurar que el directorio raíz esté en el path para encontrar 'core' y otros módulos
sys.path.append(os.path.abspath(os.path.dirname(__file__)))

def open_browser():
    """Espera un par de segundos y abre el navegador."""
    time.sleep(1.5)
    webbrowser.open("http://127.0.0.1:8000")

if __name__ == "__main__":
    # Iniciar el hilo para abrir el navegador
    threading.Thread(target=open_browser, daemon=True).start()
    
    # Iniciar el servidor FastAPI mediante Uvicorn
    # Importamos app aquí para asegurar que el path esté configurado
    from core.main import app
    
    print("Iniciando servidor en http://127.0.0.1:8000")
    print("Por favor, no cierres esta ventana mientras uses la aplicación.")
    
    uvicorn.run(app, host="127.0.0.1", port=8000, log_level="info")
