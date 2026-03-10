"""
Generador de badges para el README.

Este módulo proporciona utilidades para generar badges de shields.io
que muestran información visual sobre el proyecto (versión de Python,
licencia, versión del proyecto, etc.).
"""


class BadgeGenerator:
    """
    Generador de badges de shields.io.
    
    Esta clase proporciona métodos estáticos para generar badges
    en formato Markdown que utilizan el servicio shields.io.
    
    Formato de badge:
        ![Badge Name](https://img.shields.io/badge/label-value-color.svg)
    
    Ejemplos:
        - Python: ![Python](https://img.shields.io/badge/python-3.10+-blue.svg)
        - License: ![License](https://img.shields.io/badge/license-MIT-green.svg)
        - Version: ![Version](https://img.shields.io/badge/version-1.0.0-orange.svg)
    """
    
    @staticmethod
    def python_version(version: str) -> str:
        """
        Genera un badge para la versión de Python requerida.
        
        Args:
            version: Versión de Python en formato X.Y (ej: "3.10")
        
        Returns:
            Badge en formato Markdown con la versión de Python
        
        Examples:
            >>> BadgeGenerator.python_version("3.10")
            '![Python](https://img.shields.io/badge/python-3.10+-blue.svg)'
        """
        # Escapar caracteres especiales para URL (el + se mantiene como +)
        label = "python"
        value = f"{version}+"
        color = "blue"
        
        return f"![Python](https://img.shields.io/badge/{label}-{value}-{color}.svg)"
    
    @staticmethod
    def license(license_type: str) -> str:
        """
        Genera un badge para el tipo de licencia del proyecto.
        
        Args:
            license_type: Tipo de licencia (ej: "MIT", "Apache-2.0", "GPL-3.0")
        
        Returns:
            Badge en formato Markdown con la licencia
        
        Examples:
            >>> BadgeGenerator.license("MIT")
            '![License](https://img.shields.io/badge/license-MIT-green.svg)'
        """
        label = "license"
        # Reemplazar guiones en el tipo de licencia con %2D para URL encoding
        value = license_type.replace("-", "--")
        color = "green"
        
        return f"![License](https://img.shields.io/badge/{label}-{value}-{color}.svg)"
    
    @staticmethod
    def project_version(version: str) -> str:
        """
        Genera un badge para la versión del proyecto.
        
        Args:
            version: Versión del proyecto en formato semántico X.Y.Z (ej: "1.0.0")
        
        Returns:
            Badge en formato Markdown con la versión del proyecto
        
        Examples:
            >>> BadgeGenerator.project_version("1.0.0")
            '![Version](https://img.shields.io/badge/version-1.0.0-orange.svg)'
        """
        label = "version"
        value = version
        color = "orange"
        
        return f"![Version](https://img.shields.io/badge/{label}-{value}-{color}.svg)"
