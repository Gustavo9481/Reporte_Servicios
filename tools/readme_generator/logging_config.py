"""
Configuración de logging para el generador de README.

Este módulo proporciona configuración estructurada de logging con niveles
DEBUG, INFO, WARNING, ERROR, CRITICAL para el sistema de generación de README.
"""

import logging
import sys
from pathlib import Path
from typing import Optional
from datetime import datetime


class ReadmeGeneratorLogger:
    """Configurador de logging para el generador de README."""
    
    # Formato estructurado con timestamps
    LOG_FORMAT = '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
    DATE_FORMAT = '%Y-%m-%d %H:%M:%S'
    
    def __init__(
        self,
        name: str = "readme_generator",
        level: int = logging.INFO,
        log_to_file: bool = False,
        log_file_path: Optional[Path] = None
    ):
        """
        Inicializa el configurador de logging.
        
        Args:
            name: Nombre del logger
            level: Nivel de logging (DEBUG, INFO, WARNING, ERROR, CRITICAL)
            log_to_file: Si True, también escribe logs a archivo
            log_file_path: Ruta del archivo de log (opcional)
        """
        self.logger = logging.getLogger(name)
        self.logger.setLevel(level)
        self.logger.handlers.clear()  # Limpiar handlers existentes
        
        # Handler para consola
        console_handler = logging.StreamHandler(sys.stdout)
        console_handler.setLevel(level)
        console_formatter = logging.Formatter(
            self.LOG_FORMAT,
            datefmt=self.DATE_FORMAT
        )
        console_handler.setFormatter(console_formatter)
        self.logger.addHandler(console_handler)
        
        # Handler para archivo (opcional)
        if log_to_file:
            if log_file_path is None:
                # Usar ruta por defecto
                log_file_path = Path(f"readme_generator_{datetime.now().strftime('%Y%m%d_%H%M%S')}.log")
            
            file_handler = logging.FileHandler(log_file_path, encoding='utf-8')
            file_handler.setLevel(level)
            file_formatter = logging.Formatter(
                self.LOG_FORMAT,
                datefmt=self.DATE_FORMAT
            )
            file_handler.setFormatter(file_formatter)
            self.logger.addHandler(file_handler)
    
    def get_logger(self) -> logging.Logger:
        """Retorna el logger configurado."""
        return self.logger


def setup_logger(
    level: str = "INFO",
    log_to_file: bool = False,
    log_file_path: Optional[Path] = None
) -> logging.Logger:
    """
    Función de conveniencia para configurar el logger.
    
    Args:
        level: Nivel de logging como string ("DEBUG", "INFO", "WARNING", "ERROR", "CRITICAL")
        log_to_file: Si True, también escribe logs a archivo
        log_file_path: Ruta del archivo de log (opcional)
    
    Returns:
        Logger configurado
    
    Example:
        >>> logger = setup_logger(level="DEBUG", log_to_file=True)
        >>> logger.info("Iniciando generación de README")
    """
    level_map = {
        "DEBUG": logging.DEBUG,
        "INFO": logging.INFO,
        "WARNING": logging.WARNING,
        "ERROR": logging.ERROR,
        "CRITICAL": logging.CRITICAL
    }
    
    numeric_level = level_map.get(level.upper(), logging.INFO)
    
    logger_config = ReadmeGeneratorLogger(
        level=numeric_level,
        log_to_file=log_to_file,
        log_file_path=log_file_path
    )
    
    return logger_config.get_logger()
