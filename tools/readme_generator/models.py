"""
Modelos de datos para el generador de README.

Este módulo define las estructuras de datos utilizadas para representar
los metadatos del proyecto, endpoints de API y stack tecnológico.
"""

from pydantic import BaseModel, Field, field_validator
from typing import List
import re


class ProjectMetadata(BaseModel):
    """
    Metadatos principales del proyecto.
    
    Attributes:
        name: Nombre del proyecto
        version: Versión del proyecto en formato semántico (X.Y.Z)
        description: Descripción breve del proyecto
        author: Nombre del autor o autores
        email: Email de contacto del autor
        license: Tipo de licencia (MIT, Apache-2.0, GPL-3.0, etc.)
        python_version: Versión mínima de Python requerida
    """
    name: str = Field(..., min_length=1, max_length=200)
    version: str = Field(..., pattern=r'^\d+\.\d+\.\d+$')
    description: str = Field(..., min_length=10, max_length=1000)
    author: str = Field(..., min_length=1, max_length=200)
    email: str = Field(..., min_length=3, max_length=254)
    license: str = Field(..., min_length=1, max_length=50)
    python_version: str = Field(..., pattern=r'^\d+\.\d+$')
    
    @field_validator('email')
    @classmethod
    def validate_email(cls, v: str) -> str:
        """Valida que el email tenga un formato básico válido."""
        email_pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
        if not re.match(email_pattern, v):
            raise ValueError('El email debe tener un formato válido (ejemplo@dominio.com)')
        return v.lower()
    
    @field_validator('version')
    @classmethod
    def validate_version(cls, v: str) -> str:
        """Valida que la versión siga el formato semántico."""
        parts = v.split('.')
        if len(parts) != 3:
            raise ValueError('La versión debe tener formato X.Y.Z')
        if not all(part.isdigit() for part in parts):
            raise ValueError('Cada parte de la versión debe ser un número')
        return v
    
    @field_validator('python_version')
    @classmethod
    def validate_python_version(cls, v: str) -> str:
        """Valida que la versión de Python sea válida."""
        parts = v.split('.')
        if len(parts) != 2:
            raise ValueError('La versión de Python debe tener formato X.Y')
        if not all(part.isdigit() for part in parts):
            raise ValueError('Cada parte de la versión debe ser un número')
        major, minor = map(int, parts)
        if major < 3 or (major == 3 and minor < 8):
            raise ValueError('La versión de Python debe ser al menos 3.8')
        return v


class ApiEndpoint(BaseModel):
    """
    Información de un endpoint de API.
    
    Attributes:
        method: Método HTTP (GET, POST, PUT, DELETE, PATCH)
        path: Ruta del endpoint (debe comenzar con /)
        description: Descripción breve de la funcionalidad del endpoint
    """
    method: str = Field(..., pattern=r'^(GET|POST|PUT|DELETE|PATCH|OPTIONS|HEAD)$')
    path: str = Field(..., pattern=r'^/.*')
    description: str = Field(..., min_length=5, max_length=500)
    
    @field_validator('method')
    @classmethod
    def validate_method(cls, v: str) -> str:
        """Valida y normaliza el método HTTP a mayúsculas."""
        return v.upper()
    
    @field_validator('path')
    @classmethod
    def validate_path(cls, v: str) -> str:
        """Valida que el path comience con /."""
        if not v.startswith('/'):
            raise ValueError('El path debe comenzar con /')
        return v


class TechStack(BaseModel):
    """
    Stack tecnológico del proyecto.
    
    Attributes:
        backend: Lista de tecnologías backend
        frontend: Lista de tecnologías frontend
        database: Lista de tecnologías de base de datos
        build_tools: Lista de herramientas de build y empaquetado
    """
    backend: List[str] = Field(..., min_length=1)
    frontend: List[str] = Field(..., min_length=1)
    database: List[str] = Field(..., min_length=1)
    build_tools: List[str] = Field(..., min_length=1)
    
    @field_validator('backend', 'frontend', 'database', 'build_tools')
    @classmethod
    def validate_non_empty_strings(cls, v: List[str]) -> List[str]:
        """Valida que todos los elementos de la lista sean strings no vacíos."""
        if not all(isinstance(item, str) and item.strip() for item in v):
            raise ValueError('Todos los elementos deben ser strings no vacíos')
        return [item.strip() for item in v]
