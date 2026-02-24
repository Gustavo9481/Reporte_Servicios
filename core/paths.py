"""Gestión de rutas del proyecto compatibles con PyInstaller."""

import sys
import os
from pathlib import Path

def get_resource_path(relative_path: str) -> Path:
    """Obtiene la ruta absoluta de un recurso, compatible con PyInstaller.
    
    PyInstaller extrae los archivos a una carpeta temporal y guarda esa ruta en sys._MEIPASS.
    
    Args:
        relative_path: Ruta relativa al directorio raíz del proyecto.
        
    Returns:
        Path: Ruta absoluta del recurso.
    """
    try:
        # PyInstaller crea una carpeta temporal y almacena la ruta en _MEIPASS
        base_path = Path(sys._MEIPASS)
    except Exception:
        # En desarrollo, usamos la carpeta actual
        base_path = Path(os.path.abspath("."))
    
    return base_path / relative_path

def get_app_data_path() -> Path:
    """Obtiene la ruta para almacenar datos persistentes del usuario.
    
    En Windows: %APPDATA%/Reporte_Servicios
    En Linux: ~/.local/share/Reporte_Servicios
    
    Returns:
        Path: Ruta al directorio de datos de la aplicación.
    """
    app_name = "Reporte_Servicios"
    
    if sys.platform == "win32":
        base_dir = Path(os.environ.get("APPDATA", os.path.expanduser("~")))
    else:
        base_dir = Path(os.path.expanduser("~/.local/share"))
        
    data_dir = base_dir / app_name
    
    # Asegurarse de que el directorio exista
    data_dir.mkdir(parents=True, exist_ok=True)
    
    return data_dir
