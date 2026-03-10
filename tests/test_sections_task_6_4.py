"""
Tests para verificar la tarea 6.4: Implementar secciones finales.

Verifica que las funciones generate_contributing() y generate_license_contact()
generen el contenido correcto según los requisitos 11.1-11.5 y 12.1-12.5.
"""

import pytest
from datetime import datetime
from tools.readme_generator.sections import generate_contributing, generate_license_contact


@pytest.fixture
def sample_config():
    """Configuración de ejemplo para los tests."""
    return {
        "project": {
            "name": "Reporte de Servicios",
            "version": "1.0.0",
            "license": "MIT",
            "author": "Gustavo Colmenares | GUScode",
            "email": "g_colmenares9481@proton.me"
        }
    }


class TestGenerateContributing:
    """Tests para la función generate_contributing()."""
    
    def test_section_header_present(self, sample_config):
        """Verifica que el encabezado de la sección esté presente."""
        result = generate_contributing(sample_config)
        assert "## Contribuir" in result
    
    def test_pep8_mentioned(self, sample_config):
        """Requisito 11.1: Verifica que se mencione PEP8 para estilo de código."""
        result = generate_contributing(sample_config)
        assert "PEP8" in result or "pep8" in result.lower()
    
    def test_google_docstrings_mentioned(self, sample_config):
        """Requisito 11.2: Verifica que se mencione Google docstrings para documentación."""
        result = generate_contributing(sample_config)
        assert "Google docstrings" in result or "google" in result.lower()
    
    def test_contribution_process_explained(self, sample_config):
        """Requisito 11.3: Verifica que se explique el proceso de contribución."""
        result = generate_contributing(sample_config)
        # Debe mencionar pull requests o fork
        assert "pull request" in result.lower() or "fork" in result.lower()
    
    def test_encourages_running_tests(self, sample_config):
        """Requisito 11.5: Verifica que se anime a ejecutar tests antes de enviar cambios."""
        result = generate_contributing(sample_config)
        assert "pytest" in result or "tests" in result.lower()
    
    def test_content_in_spanish(self, sample_config):
        """Requisito 15.1: Verifica que el contenido esté en español."""
        result = generate_contributing(sample_config)
        spanish_keywords = ["Contribuir", "estilo", "código", "proceso"]
        for keyword in spanish_keywords:
            assert keyword in result


class TestGenerateLicenseContact:
    """Tests para la función generate_license_contact()."""
    
    def test_license_section_present(self, sample_config):
        """Verifica que el encabezado de Licencia esté presente."""
        result = generate_license_contact(sample_config)
        assert "## Licencia" in result
    
    def test_contact_section_present(self, sample_config):
        """Verifica que el encabezado de Contacto esté presente."""
        result = generate_license_contact(sample_config)
        assert "## Contacto" in result
    
    def test_mit_license_specified(self, sample_config):
        """Requisito 12.1: Verifica que se especifique la licencia MIT."""
        result = generate_license_contact(sample_config)
        assert "MIT" in result
    
    def test_license_link_included(self, sample_config):
        """Requisito 12.2: Verifica que se incluya un enlace a la licencia."""
        result = generate_license_contact(sample_config)
        assert "LICENSE" in result or "https://opensource.org/licenses/MIT" in result
    
    def test_author_name_included(self, sample_config):
        """Requisito 12.3: Verifica que se incluya el nombre del autor completo."""
        result = generate_license_contact(sample_config)
        assert "Gustavo Colmenares" in result
        assert "GUScode" in result
    
    def test_contact_email_included(self, sample_config):
        """Requisito 12.4: Verifica que se incluya el email de contacto."""
        result = generate_license_contact(sample_config)
        assert "g_colmenares9481@proton.me" in result
    
    def test_copyright_with_current_year(self, sample_config):
        """Requisito 12.5: Verifica que se incluya copyright con el año actual."""
        result = generate_license_contact(sample_config)
        current_year = datetime.now().year
        assert str(current_year) in result
        assert "©" in result or "copyright" in result.lower()
    
    def test_content_in_spanish(self, sample_config):
        """Requisito 15.1: Verifica que el contenido esté en español."""
        result = generate_license_contact(sample_config)
        spanish_keywords = ["Licencia", "Contacto", "Autor", "derechos reservados"]
        for keyword in spanish_keywords:
            assert keyword in result


class TestIntegration:
    """Tests de integración para ambas funciones."""
    
    def test_both_functions_return_non_empty_strings(self, sample_config):
        """Verifica que ambas funciones retornen strings no vacíos."""
        contributing = generate_contributing(sample_config)
        license_contact = generate_license_contact(sample_config)
        
        assert isinstance(contributing, str)
        assert isinstance(license_contact, str)
        assert len(contributing) > 0
        assert len(license_contact) > 0
    
    def test_markdown_format_valid(self, sample_config):
        """Verifica que el formato Markdown sea válido (headers, listas, etc.)."""
        contributing = generate_contributing(sample_config)
        license_contact = generate_license_contact(sample_config)
        
        # Verificar que tengan headers de nivel 2
        assert "## " in contributing
        assert "## " in license_contact
        
        # Verificar que tengan listas o bloques de código
        assert "-" in contributing or "```" in contributing
