"""
Inspector de proyecto para extraer información del código.

Este módulo proporciona utilidades para inspeccionar el proyecto y extraer
información como la estructura de directorios, dependencias y endpoints de API.
"""

from pathlib import Path
from typing import Dict, List, Optional
import json
import logging


class ProjectInspector:
    """
    Inspector de proyecto que extrae información del código.
    
    Esta clase proporciona métodos para analizar el proyecto y extraer
    información útil para generar el README, como la estructura de
    directorios, dependencias y endpoints de API.
    
    Attributes:
        project_root: Ruta raíz del proyecto
        logger: Logger para registrar advertencias y errores
    """
    
    # Directorios que deben excluirse del árbol
    EXCLUDED_DIRS = {
        '.git', '__pycache__', '.venv', 'venv', 'env',
        'node_modules', '.pytest_cache', '.mypy_cache',
        '.tox', '.eggs', '*.egg-info', 'dist', 'build',
        '.idea', '.vscode', '.DS_Store'
    }
    
    def __init__(self, project_root: Path, logger: Optional[logging.Logger] = None):
        """
        Inicializa el inspector con la ruta raíz del proyecto.
        
        Args:
            project_root: Ruta al directorio raíz del proyecto
            logger: Logger opcional para registrar advertencias
        
        Raises:
            FileNotFoundError: Si la ruta del proyecto no existe
        """
        self.project_root = Path(project_root)
        self.logger = logger or logging.getLogger(__name__)
        
        if not self.project_root.exists():
            self.logger.critical(f"El directorio del proyecto no existe: {project_root}")
            raise FileNotFoundError(f"El directorio del proyecto no existe: {project_root}")
        if not self.project_root.is_dir():
            self.logger.critical(f"La ruta no es un directorio: {project_root}")
            raise NotADirectoryError(f"La ruta no es un directorio: {project_root}")
        
        self.logger.debug(f"ProjectInspector inicializado para: {project_root}")
    
    def get_directory_tree(self, max_depth: int = 2) -> str:
        """
        Genera un árbol visual de la estructura de directorios del proyecto.
        
        Este método crea una representación en texto del árbol de directorios,
        excluyendo directorios comunes como .git, __pycache__, .venv, etc.
        
        Args:
            max_depth: Profundidad máxima del árbol (por defecto 2)
        
        Returns:
            String con el árbol de directorios en formato visual
        
        Examples:
            >>> inspector = ProjectInspector(Path("/proyecto"))
            >>> print(inspector.get_directory_tree(max_depth=2))
            proyecto/
            ├── api/
            │   ├── routes.py
            │   └── models.py
            ├── core/
            │   └── config.py
            └── README.md
        """
        self.logger.debug(f"Generando árbol de directorios con profundidad máxima: {max_depth}")
        lines = []
        
        def _should_exclude(path: Path) -> bool:
            """Verifica si un directorio debe ser excluido."""
            return path.name in self.EXCLUDED_DIRS or path.name.startswith('.')
        
        def _build_tree(directory: Path, prefix: str = "", depth: int = 0):
            """Construye el árbol recursivamente."""
            if depth > max_depth:
                return
            
            try:
                # Obtener y ordenar los contenidos (directorios primero, luego archivos)
                contents = sorted(directory.iterdir(), key=lambda p: (not p.is_dir(), p.name))
                
                # Filtrar elementos excluidos
                contents = [p for p in contents if not _should_exclude(p)]
                
                for i, path in enumerate(contents):
                    is_last = i == len(contents) - 1
                    
                    # Símbolos del árbol
                    connector = "└── " if is_last else "├── "
                    extension = "    " if is_last else "│   "
                    
                    # Nombre con indicador de directorio
                    name = path.name + ("/" if path.is_dir() else "")
                    lines.append(f"{prefix}{connector}{name}")
                    
                    # Recursión para directorios
                    if path.is_dir() and depth < max_depth:
                        _build_tree(path, prefix + extension, depth + 1)
                        
            except PermissionError as e:
                # Ignorar directorios sin permisos de lectura
                self.logger.warning(f"Sin permisos para leer directorio: {directory}")
        
        # Comenzar con el nombre del directorio raíz
        lines.append(f"{self.project_root.name}/")
        _build_tree(self.project_root, "", 0)
        
        self.logger.debug(f"Árbol de directorios generado con {len(lines)} líneas")
        
        return "\n".join(lines)
    
    def get_dependencies(self) -> Dict[str, List[str]]:
        """
        Parsea requirements.txt y agrupa las dependencias por categorías.
        
        Este método lee el archivo requirements.txt y organiza las dependencias
        en categorías lógicas (web, database, testing, etc.) basándose en
        patrones conocidos de nombres de paquetes.
        
        Returns:
            Diccionario con categorías como claves y listas de dependencias como valores
        
        Examples:
            >>> inspector = ProjectInspector(Path("/proyecto"))
            >>> deps = inspector.get_dependencies()
            >>> print(deps)
            {
                'web': ['fastapi==0.104.1', 'uvicorn==0.24.0'],
                'database': ['sqlalchemy==2.0.23'],
                'testing': ['pytest==7.4.3'],
                'other': ['pydantic==2.5.0']
            }
        """
        requirements_file = self.project_root / "requirements.txt"
        
        self.logger.debug(f"Buscando archivo de dependencias: {requirements_file}")
        
        if not requirements_file.exists():
            self.logger.warning(f"Archivo requirements.txt no encontrado: {requirements_file}")
            return {
                'web': [],
                'database': [],
                'testing': [],
                'documentation': [],
                'build': [],
                'other': []
            }
        
        # Categorías de dependencias
        categories = {
            'web': [],
            'database': [],
            'testing': [],
            'documentation': [],
            'build': [],
            'other': []
        }
        
        # Patrones para categorizar dependencias
        web_keywords = {'fastapi', 'uvicorn', 'flask', 'django', 'starlette', 'httpx', 'requests', 'aiohttp'}
        db_keywords = {'sqlalchemy', 'sqlite', 'psycopg', 'pymongo', 'redis', 'alembic'}
        test_keywords = {'pytest', 'unittest', 'nose', 'coverage', 'hypothesis', 'mock'}
        doc_keywords = {'mkdocs', 'sphinx', 'pdoc', 'pydoc'}
        build_keywords = {'pyinstaller', 'setuptools', 'wheel', 'build', 'twine'}
        
        try:
            with open(requirements_file, 'r', encoding='utf-8') as f:
                for line in f:
                    line = line.strip()
                    
                    # Ignorar líneas vacías y comentarios
                    if not line or line.startswith('#'):
                        continue
                    
                    # Extraer el nombre del paquete (antes de ==, >=, etc.)
                    package_name = line.split('==')[0].split('>=')[0].split('<=')[0].split('~=')[0].strip().lower()
                    
                    # Categorizar basándose en el nombre del paquete
                    if any(keyword in package_name for keyword in web_keywords):
                        categories['web'].append(line)
                    elif any(keyword in package_name for keyword in db_keywords):
                        categories['database'].append(line)
                    elif any(keyword in package_name for keyword in test_keywords):
                        categories['testing'].append(line)
                    elif any(keyword in package_name for keyword in doc_keywords):
                        categories['documentation'].append(line)
                    elif any(keyword in package_name for keyword in build_keywords):
                        categories['build'].append(line)
                    else:
                        categories['other'].append(line)
            
            self.logger.info(f"Dependencias parseadas exitosamente: {sum(len(v) for v in categories.values())} paquetes")
                        
        except Exception as e:
            # Si hay error al leer el archivo, retornar categorías vacías
            self.logger.error(f"No se pudo parsear requirements.txt: {e}")
            print(f"Advertencia: No se pudo parsear requirements.txt: {e}")
        
        return categories
    
    def get_api_endpoints(self) -> List[Dict[str, str]]:
        """
        Obtiene la lista de endpoints de API desde config.json.
        
        Este método carga los endpoints predefinidos desde el archivo de
        configuración del generador de README.
        
        Returns:
            Lista de diccionarios con información de endpoints (method, path, description)
        
        Examples:
            >>> inspector = ProjectInspector(Path("/proyecto"))
            >>> endpoints = inspector.get_api_endpoints()
            >>> print(endpoints[0])
            {'method': 'GET', 'path': '/api/status', 'description': 'Verifica el estado de la API'}
        """
        config_file = self.project_root / "tools" / "readme_generator" / "config.json"
        
        self.logger.debug(f"Buscando archivo de configuración de API: {config_file}")
        
        if not config_file.exists():
            # Retornar lista vacía si no existe el archivo de configuración
            self.logger.warning(f"Archivo config.json no encontrado: {config_file}")
            return []
        
        try:
            with open(config_file, 'r', encoding='utf-8') as f:
                config = json.load(f)
                endpoints = config.get('api_endpoints', [])
                self.logger.info(f"Cargados {len(endpoints)} endpoints de API")
                return endpoints
        except Exception as e:
            self.logger.error(f"No se pudo cargar config.json: {e}")
            print(f"Advertencia: No se pudo cargar config.json: {e}")
            return []
