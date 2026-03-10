"""
Tests para verificar la implementación de la tarea 7.1: ReadmeGenerator.

Este archivo contiene tests básicos para verificar que la clase ReadmeGenerator
funciona correctamente según los requisitos de la tarea 7.1.
"""

import pytest
from pathlib import Path
import json
import tempfile
import shutil

from tools.readme_generator.generator import ReadmeGenerator


def test_readme_generator_init_loads_config():
    """Verifica que __init__ carga la configuración correctamente."""
    # Usar el directorio actual del proyecto
    project_root = Path.cwd()
    
    generator = ReadmeGenerator(project_root)
    
    # Verificar que se cargó la configuración
    assert generator.config is not None
    assert "project" in generator.config
    assert "features" in generator.config
    assert "tech_stack" in generator.config


def test_readme_generator_init_raises_on_nonexistent_project():
    """Verifica que __init__ lanza FileNotFoundError si el proyecto no existe."""
    nonexistent_path = Path("/nonexistent/project/path")
    
    with pytest.raises(FileNotFoundError) as exc_info:
        ReadmeGenerator(nonexistent_path)
    
    assert "no existe" in str(exc_info.value).lower()


def test_readme_generator_generate_returns_string():
    """Verifica que generate() retorna un string con contenido."""
    project_root = Path.cwd()
    generator = ReadmeGenerator(project_root)
    
    readme_content = generator.generate()
    
    # Verificar que retorna un string no vacío
    assert isinstance(readme_content, str)
    assert len(readme_content) > 0


def test_readme_generator_generate_contains_all_sections():
    """Verifica que generate() incluye todas las secciones requeridas."""
    project_root = Path.cwd()
    generator = ReadmeGenerator(project_root)
    
    readme_content = generator.generate()
    
    # Verificar que contiene las secciones principales
    required_sections = [
        "# Reporte de Servicios",  # Título
        "## Tabla de Contenidos",
        "## Descripción",
        "## Características",
        "## Stack Tecnológico",
        "## Instalación",
        "## Uso",
        "## Estructura del Proyecto",
        "## Documentación de API",
        "## Testing",
        "## Build para Windows",
        "## Contribuir",
        "## Licencia",
        "## Contacto"
    ]
    
    for section in required_sections:
        assert section in readme_content, f"Falta la sección: {section}"


def test_readme_generator_generate_sections_in_correct_order():
    """Verifica que las secciones están en el orden correcto."""
    project_root = Path.cwd()
    generator = ReadmeGenerator(project_root)
    
    readme_content = generator.generate()
    
    # Verificar el orden de las secciones
    sections = [
        "## Tabla de Contenidos",
        "## Descripción",
        "## Características",
        "## Stack Tecnológico",
        "## Instalación",
        "## Uso",
        "## Estructura del Proyecto",
        "## Documentación de API",
        "## Testing",
        "## Build para Windows",
        "## Contribuir",
        "## Licencia"
    ]
    
    positions = [readme_content.find(section) for section in sections]
    
    # Todas las secciones deben estar presentes
    assert all(pos != -1 for pos in positions), "Faltan algunas secciones"
    
    # Las posiciones deben estar en orden ascendente
    assert positions == sorted(positions), "Las secciones no están en el orden correcto"


def test_readme_generator_write_to_file_creates_file(tmp_path):
    """Verifica que write_to_file() crea el archivo README.md."""
    project_root = Path.cwd()
    generator = ReadmeGenerator(project_root)
    
    output_path = tmp_path / "README.md"
    
    generator.write_to_file(output_path, backup=False)
    
    # Verificar que el archivo fue creado
    assert output_path.exists()
    
    # Verificar que tiene contenido
    content = output_path.read_text(encoding='utf-8')
    assert len(content) > 0
    assert "# Reporte de Servicios" in content


def test_readme_generator_write_to_file_creates_backup(tmp_path):
    """Verifica que write_to_file() crea un backup si el archivo existe."""
    project_root = Path.cwd()
    generator = ReadmeGenerator(project_root)
    
    output_path = tmp_path / "README.md"
    backup_path = tmp_path / "README.md.backup"
    
    # Crear un README existente
    output_path.write_text("Old content", encoding='utf-8')
    
    # Generar nuevo README con backup
    generator.write_to_file(output_path, backup=True)
    
    # Verificar que se creó el backup
    assert backup_path.exists()
    assert backup_path.read_text(encoding='utf-8') == "Old content"
    
    # Verificar que el nuevo README es diferente
    new_content = output_path.read_text(encoding='utf-8')
    assert new_content != "Old content"
    assert "# Reporte de Servicios" in new_content


def test_readme_generator_write_to_file_no_backup_when_disabled(tmp_path):
    """Verifica que write_to_file() no crea backup si backup=False."""
    project_root = Path.cwd()
    generator = ReadmeGenerator(project_root)
    
    output_path = tmp_path / "README.md"
    backup_path = tmp_path / "README.md.backup"
    
    # Crear un README existente
    output_path.write_text("Old content", encoding='utf-8')
    
    # Generar nuevo README sin backup
    generator.write_to_file(output_path, backup=False)
    
    # Verificar que NO se creó el backup
    assert not backup_path.exists()
    
    # Verificar que el nuevo README fue creado
    assert output_path.exists()
    new_content = output_path.read_text(encoding='utf-8')
    assert "# Reporte de Servicios" in new_content


def test_readme_generator_integrates_all_section_generators():
    """Verifica que generate() integra todos los generadores de secciones."""
    project_root = Path.cwd()
    generator = ReadmeGenerator(project_root)
    
    readme_content = generator.generate()
    
    # Verificar elementos de cada generador de sección
    
    # generate_header: badges
    assert "![Python]" in readme_content
    assert "![License]" in readme_content
    assert "![Version]" in readme_content
    
    # generate_description: descripción del proyecto
    assert "Aplicación web de gestión de reportes" in readme_content
    
    # generate_tech_stack: tecnologías
    assert "FastAPI" in readme_content
    assert "SQLAlchemy" in readme_content
    
    # generate_installation: comandos de instalación
    assert "pip install" in readme_content or "uv pip install" in readme_content
    assert "venv" in readme_content
    
    # generate_usage: comandos de uso
    assert "uvicorn" in readme_content
    assert "127.0.0.1:8000" in readme_content
    
    # generate_api_docs: endpoints
    assert "/api/" in readme_content
    assert "POST" in readme_content or "GET" in readme_content
    
    # generate_testing: pytest
    assert "pytest" in readme_content
    
    # generate_build_instructions: PyInstaller
    assert "PyInstaller" in readme_content or "pyinstaller" in readme_content
    
    # generate_contributing: guías de contribución
    assert "PEP8" in readme_content or "pep8" in readme_content
    
    # generate_license_contact: licencia y contacto
    assert "MIT" in readme_content
    assert "Gustavo Colmenares" in readme_content


if __name__ == "__main__":
    pytest.main([__file__, "-v"])
