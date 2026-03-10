# Reporte de Servicios

![Python](https://img.shields.io/badge/python-3.10+-blue.svg)
![License](https://img.shields.io/badge/license-MIT-green.svg)
![Version](https://img.shields.io/badge/version-1.0.0-orange.svg)

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

## Descripción

Aplicación web de gestión de reportes para talleres mecánicos

## Características

- Gestión completa de reportes (CRUD)
- Generación automática de PDFs profesionales
- Interfaz web intuitiva con Web Components
- Base de datos SQLite integrada
- API REST documentada con FastAPI
- Empaquetado para Windows sin dependencias

## Stack Tecnológico

### Backend

- FastAPI
- SQLAlchemy
- Pydantic
- ReportLab
- Uvicorn

### Frontend

- JavaScript Vanilla
- Web Components
- CSS3

### Base de Datos

- SQLite

### Herramientas de Build

- PyInstaller
- pytest

## Instalación

### Prerrequisitos

- Python 3.10 o superior
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
venv\Scripts\activate
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

## Uso

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

### Para Usuarios Finales

Si eres un usuario final y solo quieres usar la aplicación sin instalar Python ni dependencias:

1. **Descargar el ejecutable**

   - Descarga el archivo `Reporte_Servicios.exe` desde la sección de releases
   - No necesitas instalar Python ni ninguna dependencia

2. **Ejecutar la aplicación**

   - Simplemente haz doble clic en `Reporte_Servicios.exe`
   - La aplicación se abrirá automáticamente en tu navegador predeterminado

3. **Guía de usuario detallada**

   Para instrucciones completas sobre cómo usar la aplicación, consulta la [Guía de Usuario](docs/INSTRUCCIONES_USUARIO.md).

**Nota**: El ejecutable incluye todo lo necesario para funcionar, incluyendo la interfaz web y la base de datos SQLite.

## Estructura del Proyecto

```
Reporte_Servicios/
├── .gemini_security/
├── .github/
├── .kiro/
├── .pytest_cache/
├── .venv/
├── .vscode/
├── api/
│   ├── __pycache__/
│   ├── __init__.py
│   ├── dependencies.py
│   ├── models.py
│   └── routes.py
├── conductor/
│   ├── __pycache__/
│   ├── __init__.py
│   ├── conductor.py
│   └── models.py
├── core/
│   ├── __pycache__/
│   ├── __init__.py
│   ├── config.py
│   └── database.py
├── data/
│   ├── __pycache__/
│   ├── __init__.py
│   ├── crud.py
│   ├── database.py
│   ├── models.py
│   └── schemas.py
├── docs/
│   ├── INSTRUCCIONES_USUARIO.md
│   ├── reference.md
│   └── testing.md
├── interface/
│   ├── components/
│   ├── css/
│   ├── js/
│   └── index.html
├── site/
│   ├── assets/
│   ├── INSTRUCCIONES_USUARIO/
│   ├── reference/
│   ├── testing/
│   ├── 404.html
│   ├── index.html
│   ├── search/
│   ├── sitemap.xml
│   └── sitemap.xml.gz
├── tests/
│   ├── __pycache__/
│   ├── __init__.py
│   ├── test_api.py
│   ├── test_cli_task_11_1.py
│   ├── test_crud.py
│   ├── test_database.py
│   ├── test_generator_task_7_1.py
│   ├── test_models.py
│   ├── test_pdf.py
│   └── test_sections_task_6_4.py
├── testsprite_tests/
├── tools/
│   ├── readme_generator/
│   └── generate_readme.py
├── .gitignore
├── demo_generator.py
├── demo_task_6_4.py
├── execute_generator.py
├── generate_readme_manual.py
├── GEMINI.md
├── init_db.py
├── manual_test_cli.py
├── mkdocs.yml
├── pyproject.toml
├── README.md
├── requirements.txt
├── run_app.py
├── run_manual_test.sh
├── run_readme_generator.py
├── run_verification.py
├── TASK_11_1_COMPLETE.md
├── TASK_11_1_VERIFICATION.md
├── TASK_11_2_COMPLETE.md
├── TASK_6_3_VERIFICATION.md
├── TASK_6_4_VERIFICATION.md
├── TASK_7_1_COMPLETE.md
├── TASK_7_1_VERIFICATION.md
├── test_cli.py
├── test_generator_simple.py
├── uv.lock
├── verify_cli.py
└── windows_build.spec
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

## Documentación de API

La API REST proporciona endpoints para gestionar reportes de servicios. Todos los endpoints están bajo el prefijo `/api/`.

### Endpoints Principales

- **GET** `/api/status` - Verifica el estado de la API
- **POST** `/api/reportes` - Crea un nuevo reporte
- **GET** `/api/reportes` - Lista todos los reportes con paginación
- **GET** `/api/reportes/{id}` - Obtiene un reporte específico por ID
- **GET** `/api/reportes/placa/{placa}` - Busca reportes por placa del vehículo
- **PUT** `/api/reportes/{id}` - Actualiza un reporte existente
- **DELETE** `/api/reportes/{id}` - Elimina un reporte
- **GET** `/api/reportes/{id}/pdf` - Genera y descarga el PDF del reporte

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

## Testing

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

Para más información sobre la estrategia de testing, casos de prueba y mejores prácticas, consulta la [Documentación de Testing](docs/testing.md).

## Build para Windows

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

## Contribuir

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

## Licencia

Este proyecto está licenciado bajo la **MIT License**.

Para más detalles, consulta el archivo [LICENSE](LICENSE) o visita [https://opensource.org/licenses/MIT](https://opensource.org/licenses/MIT).

## Contacto

**Autor**: Gustavo Colmenares | GUScode

**Email**: g_colmenares9481@proton.me

Si tienes preguntas, sugerencias o deseas reportar un problema, no dudes en contactarme por email o abrir un issue en el repositorio.

---

© 2025 Gustavo Colmenares | GUScode. Todos los derechos reservados.
