# Tech Stack: Reporte de Servicios

## Lenguajes de Programación

*   **Python 3.10+**: Lenguaje principal para el desarrollo de la API.
*   **JavaScript**: Para la interactividad del frontend.
*   **HTML5**: Estructura del frontend.
*   **CSS3**: Estilos del frontend.

## Frameworks y Librerías

*   **Backend (Python)**:
    *   **FastAPI**: Framework web de alto rendimiento para construir APIs.
    *   **SQLAlchemy**: ORM (Object-Relational Mapper) para interactuar con la base de datos.
        *   `declarative_base`, `sessionmaker`, `create_engine`
        *   Modelos definidos usando `Column`, `Integer`, `String`, `Boolean`, `Float`, `Date`, `ForeignKey`, `relationship`.
    *   **Pydantic**: Para la validación de datos y serialización, integrado con FastAPI.
        *   `BaseModel`, `Field`, `Optional`, `Literal`.
    *   **ReportLab**: Librería para la generación de documentos PDF.
        *   `SimpleDocTemplate`, `Paragraph`, `Table`, `TableStyle`, `ParagraphStyle`, `colors`, `enums`, `units`.
    *   **Uvicorn**: Servidor ASGI para ejecutar la aplicación FastAPI.

*   **Frontend (JavaScript/HTML/CSS)**:
    *   **JavaScript (Vanilla)**: Lógica de interacción con el usuario y llamadas a la API.
    *   **HTML5/CSS3**: Para la estructura y estilos de la interfaz web.

## Base de Datos

*   **SQLite**: Base de datos relacional ligera, utilizada como `dB.sqlite3` en el directorio `data/`.

## Herramientas de Desarrollo y Calidad

*   **Poetry/uv**: Gestión de dependencias y entornos virtuales (inferido de `uv.lock` y `pyproject.toml`).
*   **pytest**: Framework de testing para Python (mencionado en `pyproject.toml`).
*   **black**: Formateador de código Python (mencionado en `pyproject.toml`).
*   **isort**: Herramienta para ordenar imports de Python (mencionado en `pyproject.toml`).

## Convenciones de Código y Estilo

*   **PEP8**: Se seguirá el estándar de estilo de código para Python.
*   **Docstrings**: Funciones y clases deben documentarse utilizando docstrings estilo Google.
*   **Nomenclatura**: Variables en inglés, explicativas.
*   **Manejo de Errores**: Uso de excepciones personalizadas para errores específicos.
*   **Consistencia**: Mantener la consistencia con el código existente en todo el proyecto.
*   **FastAPI**: Uso de `HTTPException` para respuestas de error de la API.
*   **SQLAlchemy**: Uso de `SessionLocal`, `get_db` con `Depends` para la gestión de la sesión de base de datos.
*   **Pydantic**: Definición de modelos Pydantic para validación de entrada y salida de datos de la API.
