"""
Generador principal de README.

Este módulo contiene la clase ReadmeGenerator que orquesta la generación
completa del archivo README.md, integrando todos los generadores de secciones.
"""

from pathlib import Path
from typing import Dict, Any, Optional
import json
import shutil
from datetime import datetime
import logging

from tools.readme_generator.sections import (
    generate_header,
    generate_description,
    generate_tech_stack,
    generate_installation,
    generate_usage,
    generate_end_user_guide,
    generate_project_structure,
    generate_api_docs,
    generate_testing,
    generate_build_instructions,
    generate_contributing,
    generate_license_contact
)
from tools.readme_generator.logging_config import setup_logger


class ReadmeGenerator:
    """
    Generador principal del archivo README.md.
    
    Esta clase orquesta la generación completa del README, cargando la
    configuración del proyecto y llamando a todos los generadores de
    secciones en el orden correcto.
    
    Attributes:
        project_root: Ruta raíz del proyecto
        config: Diccionario con la configuración del proyecto
    """
    
    def __init__(
        self,
        project_root: Path,
        logger: Optional[logging.Logger] = None,
        log_level: str = "INFO"
    ):
        """
        Inicializa el generador con la ruta raíz del proyecto.
        
        Este método carga la configuración desde config.json y valida
        que el proyecto exista.
        
        Args:
            project_root: Ruta al directorio raíz del proyecto
            logger: Logger personalizado (opcional)
            log_level: Nivel de logging ("DEBUG", "INFO", "WARNING", "ERROR", "CRITICAL")
        
        Raises:
            FileNotFoundError: Si la ruta del proyecto no existe
            FileNotFoundError: Si no se encuentra config.json
            ValueError: Si config.json tiene formato inválido
        
        Validates:
            - Requirements 1.1, 1.2, 1.5
        """
        self.project_root = Path(project_root)
        
        # Configurar logger
        if logger is None:
            self.logger = setup_logger(level=log_level)
        else:
            self.logger = logger
        
        self.logger.info(f"Inicializando ReadmeGenerator para proyecto: {project_root}")
        
        # Validar que el proyecto exista
        if not self.project_root.exists():
            self.logger.critical(f"El directorio del proyecto no existe: {project_root}")
            raise FileNotFoundError(
                f"El directorio del proyecto no existe: {project_root}"
            )
        
        if not self.project_root.is_dir():
            self.logger.critical(f"La ruta no es un directorio: {project_root}")
            raise NotADirectoryError(
                f"La ruta no es un directorio: {project_root}"
            )
        
        self.logger.debug(f"Directorio del proyecto validado: {self.project_root}")
        
        # Cargar configuración desde config.json
        self.config = self._load_config()
    
    def _load_config(self) -> Dict[str, Any]:
        """
        Carga la configuración desde config.json.
        
        Returns:
            Diccionario con la configuración del proyecto
        
        Raises:
            FileNotFoundError: Si no se encuentra config.json
            ValueError: Si config.json tiene formato JSON inválido
        """
        config_path = self.project_root / "tools" / "readme_generator" / "config.json"
        
        self.logger.debug(f"Buscando archivo de configuración: {config_path}")
        
        if not config_path.exists():
            self.logger.error(f"No se encontró el archivo de configuración: {config_path}")
            raise FileNotFoundError(
                f"No se encontró el archivo de configuración: {config_path}"
            )
        
        try:
            with open(config_path, 'r', encoding='utf-8') as f:
                config = json.load(f)
            self.logger.info("Configuración cargada exitosamente")
            self.logger.debug(f"Proyecto: {config.get('project', {}).get('name', 'N/A')}")
            return config
        except json.JSONDecodeError as e:
            self.logger.error(f"El archivo config.json tiene formato JSON inválido: {e}")
            raise ValueError(
                f"El archivo config.json tiene formato JSON inválido: {e}"
            )
        except Exception as e:
            self.logger.error(f"Error al cargar config.json: {e}")
            raise ValueError(
                f"Error al cargar config.json: {e}"
            )
    
    def generate(self) -> str:
        """
        Genera el contenido completo del README.
        
        Este método orquesta la generación de todas las secciones del README
        en el orden correcto, llamando a cada generador de sección y
        concatenando los resultados.
        
        Returns:
            String con el contenido completo del README en formato Markdown
        
        Validates:
            - Requirements 1.1, 1.2, 1.5
        
        Examples:
            >>> generator = ReadmeGenerator(Path("/proyecto"))
            >>> readme_content = generator.generate()
            >>> print(readme_content[:100])
            # Reporte de Servicios
            
            ![Python](https://img.shields.io/badge/python-3.10+-blue.svg)
            ...
        """
        self.logger.info("Iniciando generación del README")
        sections = []
        
        # 1. Header con título, badges y tabla de contenidos
        self.logger.debug("Generando sección: Header")
        sections.append(generate_header(self.config))
        
        # 2. Descripción y características
        self.logger.debug("Generando sección: Descripción")
        sections.append(generate_description(self.config))
        
        # 3. Stack tecnológico
        self.logger.debug("Generando sección: Stack Tecnológico")
        sections.append(generate_tech_stack(self.config))
        
        # 4. Instalación
        self.logger.debug("Generando sección: Instalación")
        sections.append(generate_installation(self.config))
        
        # 5. Uso (desarrolladores y usuarios finales)
        self.logger.debug("Generando sección: Uso")
        sections.append(generate_usage(self.config))
        self.logger.debug("Generando sección: Guía de Usuario Final")
        sections.append(generate_end_user_guide(self.config))
        
        # 6. Estructura del proyecto
        self.logger.debug("Generando sección: Estructura del Proyecto")
        sections.append(generate_project_structure(self.config))
        
        # 7. Documentación de API
        self.logger.debug("Generando sección: Documentación de API")
        sections.append(generate_api_docs(self.config))
        
        # 8. Testing
        self.logger.debug("Generando sección: Testing")
        sections.append(generate_testing(self.config))
        
        # 9. Build para Windows
        self.logger.debug("Generando sección: Build para Windows")
        sections.append(generate_build_instructions(self.config))
        
        # 10. Contribuir
        self.logger.debug("Generando sección: Contribuir")
        sections.append(generate_contributing(self.config))
        
        # 11. Licencia y contacto
        self.logger.debug("Generando sección: Licencia y Contacto")
        sections.append(generate_license_contact(self.config))
        
        # Unir todas las secciones con doble salto de línea
        readme_content = "\n\n".join(sections)
        
        self.logger.info(f"README generado exitosamente ({len(readme_content)} caracteres)")
        
        return readme_content
    
    def write_to_file(self, output_path: Path, backup: bool = True) -> None:
        """
        Escribe el README generado en el archivo especificado.
        
        Este método genera el contenido del README y lo escribe en el archivo
        especificado. Si el archivo ya existe y backup=True, crea un backup
        antes de sobrescribir.
        
        Args:
            output_path: Ruta donde se escribirá el README.md
            backup: Si True, crea un backup del README existente antes de sobrescribir
        
        Raises:
            PermissionError: Si no hay permisos para escribir en el directorio
            OSError: Si hay un error al escribir el archivo
        
        Examples:
            >>> generator = ReadmeGenerator(Path("/proyecto"))
            >>> generator.write_to_file(Path("/proyecto/README.md"), backup=True)
            # Crea README.md y README.md.backup si ya existía
        """
        output_path = Path(output_path)
        
        self.logger.info(f"Escribiendo README en: {output_path}")
        
        # Crear backup si el archivo existe y backup=True
        if output_path.exists() and backup:
            backup_path = output_path.with_suffix('.md.backup')
            try:
                shutil.copy2(output_path, backup_path)
                self.logger.info(f"Backup creado: {backup_path}")
                print(f"✓ Backup creado: {backup_path}")
            except Exception as e:
                self.logger.warning(f"No se pudo crear backup: {e}")
                print(f"⚠ Advertencia: No se pudo crear backup: {e}")
        
        # Generar contenido del README
        try:
            readme_content = self.generate()
        except Exception as e:
            self.logger.error(f"Error al generar el contenido del README: {e}")
            raise RuntimeError(f"Error al generar el contenido del README: {e}")
        
        # Escribir el archivo
        try:
            with open(output_path, 'w', encoding='utf-8') as f:
                f.write(readme_content)
            self.logger.info(f"README escrito exitosamente: {output_path}")
            print(f"✓ README generado exitosamente: {output_path}")
        except PermissionError:
            self.logger.error(f"No hay permisos para escribir en: {output_path}")
            raise PermissionError(
                f"No hay permisos para escribir en: {output_path}"
            )
        except Exception as e:
            self.logger.error(f"Error al escribir el archivo README: {e}")
            raise OSError(
                f"Error al escribir el archivo README: {e}"
            )
