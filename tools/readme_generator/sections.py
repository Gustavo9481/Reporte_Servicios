"""
Generadores de secciones para el README.

Este módulo contiene funciones para generar cada sección del README.md,
incluyendo el header con badges, descripción, features, tech stack, etc.
"""

from typing import Dict, List, Any
from tools.readme_generator.badges import BadgeGenerator


def generate_header(config: Dict[str, Any]) -> str:
    """
    Genera el header del README con título, badges y tabla de contenidos.
    
    Args:
        config: Diccionario con la configuración del proyecto
    
    Returns:
        String con el header completo en formato Markdown
    
    Validates:
        - Requirements 1.2, 1.4, 2.1, 2.4, 13.1, 13.2, 13.3, 13.4, 13.5
    """
    project = config.get("project", {})
    name = project.get("name", "Proyecto")
    version = project.get("version", "1.0.0")
    license_type = project.get("license", "MIT")
    python_version = project.get("python_version", "3.10")
    
    # Generar badges usando BadgeGenerator
    python_badge = BadgeGenerator.python_version(python_version)
    license_badge = BadgeGenerator.license(license_type)
    version_badge = BadgeGenerator.project_version(version)
    
    # Construir header
    header = f"""# {name}

{python_badge}
{license_badge}
{version_badge}

## Tabla de Contenidos

- [Descripción](#descripción)
- [Características](#características)
- [Stack Tecnológico](#stack-tecnológico)
- [Instalación](#instalación)
- [Uso](#uso)
  - [Para Desarrolladores](#para-desarrolladores)
  - [Para Usuarios Finales](#para-usuarios-finales)
- [Estructura del Proyecto](#estructura-del-proyecto)
- [Documentación de API](#documentación-de-api)
- [Testing](#testing)
- [Build para Windows](#build-para-windows)
- [Contribuir](#contribuir)
- [Licencia](#licencia)
- [Contacto](#contacto)
"""
    
    return header


def generate_description(config: Dict[str, Any]) -> str:
    """
    Genera la sección de descripción con descripción del proyecto y features.
    
    Args:
        config: Diccionario con la configuración del proyecto
    
    Returns:
        String con la descripción y características en formato Markdown
    
    Validates:
        - Requirements 2.2, 2.3
    """
    project = config.get("project", {})
    description = project.get("description", "")
    features = config.get("features", [])
    
    section = f"""## Descripción

{description}

## Características

"""
    
    # Agregar lista de características
    for feature in features:
        section += f"- {feature}\n"
    
    return section


def generate_tech_stack(config: Dict[str, Any]) -> str:
    """
    Genera la sección de stack tecnológico organizado por categorías.
    
    Args:
        config: Diccionario con la configuración del proyecto
    
    Returns:
        String con el tech stack organizado en formato Markdown
    
    Validates:
        - Requirements 3.1, 3.2, 3.5
    """
    tech_stack = config.get("tech_stack", {})
    backend = tech_stack.get("backend", [])
    frontend = tech_stack.get("frontend", [])
    database = tech_stack.get("database", [])
    build_tools = tech_stack.get("build_tools", [])
    
    section = """## Stack Tecnológico

### Backend

"""
    
    # Agregar tecnologías backend
    for tech in backend:
        section += f"- {tech}\n"
    
    section += "\n### Frontend\n\n"
    
    # Agregar tecnologías frontend
    for tech in frontend:
        section += f"- {tech}\n"
    
    section += "\n### Base de Datos\n\n"
    
    # Agregar tecnologías de base de datos
    for tech in database:
        section += f"- {tech}\n"
    
    section += "\n### Herramientas de Build\n\n"
    
    # Agregar herramientas de build
    for tech in build_tools:
        section += f"- {tech}\n"
    
    return section


def generate_installation(config: Dict[str, Any]) -> str:
    """
    Genera la sección de instalación con pasos detallados y alternativas.
    
    Args:
        config: Diccionario con la configuración del proyecto
    
    Returns:
        String con las instrucciones de instalación en formato Markdown
    
    Validates:
        - Requirements 4.1, 4.2, 4.3, 4.4, 4.5, 4.6, 4.7
    """
    project = config.get("project", {})
    python_version = project.get("python_version", "3.10")
    
    section = f"""## Instalación

### Prerrequisitos

- Python {python_version} o superior
- Git (para clonar el repositorio)

### Pasos de Instalación

1. **Clonar el repositorio**

```bash
# Clonar el proyecto desde el repositorio
git clone <URL_DEL_REPOSITORIO>
cd reporte-servicios
```

2. **Crear un entorno virtual**

```bash
# Crear entorno virtual con Python
python -m venv venv

# Activar el entorno virtual
# En Windows:
venv\\Scripts\\activate
# En Linux/Mac:
source venv/bin/activate
```

3. **Instalar dependencias**

Puedes instalar las dependencias usando **pip** o **uv** (más rápido):

**Opción A: Usando pip (tradicional)**

```bash
# Instalar todas las dependencias del proyecto
pip install -r requirements.txt
```

**Opción B: Usando uv (recomendado, más rápido)**

```bash
# Instalar uv si no lo tienes
pip install uv

# Instalar dependencias con uv
uv pip install -r requirements.txt
```

4. **Inicializar la base de datos**

```bash
# Crear la base de datos SQLite y las tablas necesarias
python init_db.py
```

¡Listo! El entorno de desarrollo está configurado y la aplicación está lista para ejecutarse.
"""
    
    return section


def generate_usage(config: Dict[str, Any]) -> str:
    """
    Genera la sección de uso para desarrolladores.
    
    Args:
        config: Diccionario con la configuración del proyecto
    
    Returns:
        String con las instrucciones de uso en formato Markdown
    
    Validates:
        - Requirements 5.1, 5.2, 5.3, 5.4, 5.5
    """
    section = """## Uso

### Para Desarrolladores

1. **Iniciar el servidor de desarrollo**

```bash
# Ejecutar el servidor con uvicorn
uvicorn main:app --reload

# El servidor se iniciará en http://127.0.0.1:8000
```

2. **Acceder a la aplicación**

- **Interfaz web**: Abre tu navegador y visita [http://127.0.0.1:8000](http://127.0.0.1:8000)
- **Documentación interactiva de la API**: Visita [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)

3. **Detener el servidor**

```bash
# Presiona Ctrl+C en la terminal para detener el servidor
```

**Nota**: El flag `--reload` hace que el servidor se reinicie automáticamente cuando detecta cambios en el código, ideal para desarrollo.
"""
    
    return section


def generate_end_user_guide(config: Dict[str, Any]) -> str:
    """
    Genera la guía simplificada para usuarios finales.
    
    Args:
        config: Diccionario con la configuración del proyecto
    
    Returns:
        String con la guía para usuarios finales en formato Markdown
    
    Validates:
        - Requirements 6.1, 6.2, 6.3, 6.4
    """
    docs_links = config.get("docs_links", {})
    user_guide = docs_links.get("user_guide", "docs/INSTRUCCIONES_USUARIO.md")
    
    section = f"""### Para Usuarios Finales

Si eres un usuario final y solo quieres usar la aplicación sin instalar Python ni dependencias:

1. **Descargar el ejecutable**

   - Descarga el archivo `Reporte_Servicios.exe` desde la sección de releases
   - No necesitas instalar Python ni ninguna dependencia

2. **Ejecutar la aplicación**

   - Simplemente haz doble clic en `Reporte_Servicios.exe`
   - La aplicación se abrirá automáticamente en tu navegador predeterminado

3. **Guía de usuario detallada**

   Para instrucciones completas sobre cómo usar la aplicación, consulta la [Guía de Usuario]({user_guide}).

**Nota**: El ejecutable incluye todo lo necesario para funcionar, incluyendo la interfaz web y la base de datos SQLite.
"""
    
    return section


def generate_project_structure(config: Dict[str, Any]) -> str:
    """
    Genera la sección de estructura del proyecto con árbol y descripciones.
    
    Args:
        config: Diccionario con la configuración del proyecto
    
    Returns:
        String con la estructura del proyecto en formato Markdown
    
    Validates:
        - Requirements 7.1, 7.2, 7.3, 7.4, 7.5
    """
    from pathlib import Path
    from tools.readme_generator.inspector import ProjectInspector
    
    # Obtener la ruta raíz del proyecto (asumiendo que estamos en tools/readme_generator/)
    project_root = Path.cwd()
    
    # Crear inspector y obtener árbol de directorios
    inspector = ProjectInspector(project_root)
    directory_tree = inspector.get_directory_tree(max_depth=2)
    
    section = f"""## Estructura del Proyecto

```
{directory_tree}
```

### Descripción de Directorios Principales

- **api/**: Contiene los endpoints de la API REST, incluyendo rutas, modelos de datos y lógica de negocio
- **core/**: Módulos centrales de la aplicación, como configuración, utilidades y servicios compartidos
- **data/**: Gestión de la base de datos SQLite, modelos de SQLAlchemy y scripts de inicialización
- **interface/**: Interfaz web del usuario, incluyendo HTML, CSS, JavaScript y Web Components
- **docs/**: Documentación del proyecto, guías de usuario y referencias técnicas
- **tests/**: Suite de pruebas unitarias y de integración con pytest

### Archivos Clave

- **main.py**: Punto de entrada principal de la aplicación FastAPI
- **run_app.py**: Script para ejecutar la aplicación en modo producción
- **init_db.py**: Script para inicializar la base de datos SQLite con las tablas necesarias
- **requirements.txt**: Lista de dependencias del proyecto
- **windows_build.spec**: Especificación para PyInstaller para crear el ejecutable de Windows

La arquitectura separa claramente el backend (API REST con FastAPI) del frontend (interfaz web con JavaScript vanilla), facilitando el mantenimiento y la escalabilidad del proyecto.
"""
    
    return section


def generate_api_docs(config: Dict[str, Any]) -> str:
    """
    Genera la sección de documentación de API con endpoints y ejemplos.
    
    Args:
        config: Diccionario con la configuración del proyecto
    
    Returns:
        String con la documentación de API en formato Markdown
    
    Validates:
        - Requirements 8.1, 8.2, 8.3, 8.4, 8.5
    """
    api_endpoints = config.get("api_endpoints", [])
    
    section = """## Documentación de API

La API REST proporciona endpoints para gestionar reportes de servicios. Todos los endpoints están bajo el prefijo `/api/`.

### Endpoints Principales

"""
    
    # Listar todos los endpoints
    for endpoint in api_endpoints:
        method = endpoint.get("method", "GET")
        path = endpoint.get("path", "")
        description = endpoint.get("description", "")
        section += f"- **{method}** `{path}` - {description}\n"
    
    section += """
### Ejemplo de Request/Response

**Crear un nuevo reporte**

```bash
# Request
POST /api/reportes
Content-Type: application/json

{
  "placa": "ABC123",
  "cliente": "Juan Pérez",
  "telefono": "555-1234",
  "vehiculo": "Toyota Corolla 2020",
  "servicios": "Cambio de aceite, revisión de frenos",
  "observaciones": "Cliente solicita revisión completa"
}

# Response (201 Created)
{
  "id": 1,
  "placa": "ABC123",
  "cliente": "Juan Pérez",
  "telefono": "555-1234",
  "vehiculo": "Toyota Corolla 2020",
  "servicios": "Cambio de aceite, revisión de frenos",
  "observaciones": "Cliente solicita revisión completa",
  "fecha_creacion": "2024-01-15T10:30:00",
  "fecha_actualizacion": "2024-01-15T10:30:00"
}
```

### Documentación Interactiva

FastAPI proporciona documentación interactiva automática donde puedes probar todos los endpoints:

- **Swagger UI**: [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)
- **ReDoc**: [http://127.0.0.1:8000/redoc](http://127.0.0.1:8000/redoc)

Para más detalles sobre los esquemas de datos y validaciones, consulta la [Documentación de Referencia](docs/reference.md).
"""
    
    return section


def generate_testing(config: Dict[str, Any]) -> str:
    """
    Genera la sección de testing con comandos pytest.
    
    Args:
        config: Diccionario con la configuración del proyecto
    
    Returns:
        String con las instrucciones de testing en formato Markdown
    
    Validates:
        - Requirements 9.1, 9.2, 9.3, 9.4, 9.5
    """
    docs_links = config.get("docs_links", {})
    testing_doc = docs_links.get("testing", "docs/testing.md")
    
    section = f"""## Testing

El proyecto utiliza **pytest** y **pytest-asyncio** para las pruebas unitarias y de integración.

### Ejecutar Todas las Pruebas

```bash
# Ejecutar todos los tests
pytest

# Ejecutar con output detallado
pytest -v

# Ejecutar con cobertura de código
pytest --cov=. --cov-report=html
```

### Ejecutar Pruebas Específicas

```bash
# Ejecutar tests de un archivo específico
pytest tests/test_api.py

# Ejecutar un test específico
pytest tests/test_api.py::test_create_reporte

# Ejecutar tests que coincidan con un patrón
pytest -k "test_reporte"
```

### Ver Reporte de Cobertura

Después de ejecutar las pruebas con cobertura, puedes ver el reporte HTML:

```bash
# Abrir el reporte de cobertura en el navegador
# El archivo se encuentra en htmlcov/index.html
```

### Frameworks de Testing

- **pytest**: Framework principal de testing
- **pytest-asyncio**: Soporte para tests asíncronos con FastAPI

Para más información sobre la estrategia de testing, casos de prueba y mejores prácticas, consulta la [Documentación de Testing]({testing_doc}).
"""
    
    return section


def generate_build_instructions(config: Dict[str, Any]) -> str:
    """
    Genera la sección de instrucciones de build para PyInstaller.
    
    Args:
        config: Diccionario con la configuración del proyecto
    
    Returns:
        String con las instrucciones de build en formato Markdown
    
    Validates:
        - Requirements 10.1, 10.2, 10.3, 10.4, 10.5
    """
    section = """## Build para Windows

El proyecto puede empaquetarse como un ejecutable standalone para Windows usando **PyInstaller**.

### Prerrequisitos

```bash
# Instalar PyInstaller si no lo tienes
pip install pyinstaller
```

### Crear el Ejecutable

```bash
# Ejecutar PyInstaller con el archivo de especificación
pyinstaller windows_build.spec

# El ejecutable se creará en el directorio dist/
```

### Ubicación del Ejecutable

Después del build, encontrarás el ejecutable en:

```
dist/
└── Reporte_Servicios.exe
```

### Contenido del Build

El ejecutable incluye:

- Todas las dependencias de Python (FastAPI, SQLAlchemy, ReportLab, etc.)
- La carpeta `interface/` completa con la interfaz web
- La base de datos SQLite (si existe)
- Todos los recursos necesarios para ejecutar la aplicación

### Distribución

El archivo `Reporte_Servicios.exe` es completamente portable y puede distribuirse a usuarios finales sin necesidad de instalar Python ni dependencias adicionales.

**Nota**: El archivo de especificación `windows_build.spec` está configurado para incluir automáticamente todos los recursos necesarios. Si agregas nuevos archivos estáticos o dependencias, asegúrate de actualizar el spec file.
"""
    
    return section


def generate_contributing(config: Dict[str, Any]) -> str:
    """
    Genera la sección de guía de contribución con estilo y proceso.
    
    Args:
        config: Diccionario con la configuración del proyecto
    
    Returns:
        String con las guías de contribución en formato Markdown
    
    Validates:
        - Requirements 11.1, 11.2, 11.3, 11.5
    """
    section = """## Contribuir

¡Las contribuciones son bienvenidas! Si deseas colaborar con el proyecto, sigue estas guías:

### Estilo de Código

- **PEP8**: Sigue las convenciones de estilo de Python definidas en [PEP8](https://pep8.org/)
- **Documentación**: Utiliza [Google docstrings](https://google.github.io/styleguide/pyguide.html#38-comments-and-docstrings) para documentar funciones, clases y módulos
- **Type hints**: Usa anotaciones de tipo para mejorar la legibilidad y mantenibilidad del código

### Proceso de Contribución

1. **Fork el repositorio** y crea una rama para tu feature o bugfix
2. **Escribe código limpio** siguiendo las guías de estilo mencionadas
3. **Añade tests** para cualquier funcionalidad nueva o cambios significativos
4. **Ejecuta los tests** antes de hacer commit para asegurar que todo funciona correctamente:

```bash
# Ejecutar todos los tests
pytest

# Verificar cobertura
pytest --cov=. --cov-report=html
```

5. **Haz commit de tus cambios** con mensajes descriptivos
6. **Envía un pull request** describiendo los cambios realizados y su propósito

### Buenas Prácticas

- Mantén los commits atómicos y enfocados en un solo cambio
- Escribe mensajes de commit claros y descriptivos
- Actualiza la documentación si tus cambios afectan el uso de la API o funcionalidades
- Asegúrate de que el código pase todos los tests antes de enviar el pull request

¡Gracias por contribuir al proyecto!
"""
    
    return section


def generate_license_contact(config: Dict[str, Any]) -> str:
    """
    Genera la sección de licencia y contacto con información del autor.
    
    Args:
        config: Diccionario con la configuración del proyecto
    
    Returns:
        String con la información de licencia y contacto en formato Markdown
    
    Validates:
        - Requirements 12.1, 12.2, 12.3, 12.4, 12.5
    """
    from datetime import datetime
    
    project = config.get("project", {})
    license_type = project.get("license", "MIT")
    author = project.get("author", "Gustavo Colmenares | GUScode")
    email = project.get("email", "g_colmenares9481@proton.me")
    
    # Obtener el año actual para el copyright
    current_year = datetime.now().year
    
    section = f"""## Licencia

Este proyecto está licenciado bajo la **{license_type} License**.

Para más detalles, consulta el archivo [LICENSE](LICENSE) o visita [https://opensource.org/licenses/MIT](https://opensource.org/licenses/MIT).

## Contacto

**Autor**: {author}

**Email**: {email}

Si tienes preguntas, sugerencias o deseas reportar un problema, no dudes en contactarme por email o abrir un issue en el repositorio.

---

© {current_year} {author}. Todos los derechos reservados.
"""
    
    return section
