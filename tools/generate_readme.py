#!/usr/bin/env python3
"""
Script CLI para generar README.md profesional.

Este script proporciona una interfaz de línea de comandos para ejecutar
el generador de README, con opciones para controlar el comportamiento
de backup y modo interactivo.

Uso:
    python tools/generate_readme.py
    python tools/generate_readme.py --no-backup
    python tools/generate_readme.py --interactive
    python tools/generate_readme.py --log-level DEBUG
    python tools/generate_readme.py --log-to-file

Requisitos: 1.1
"""

import argparse
import sys
from pathlib import Path

# Añadir el directorio raíz al path para importar módulos
sys.path.insert(0, str(Path(__file__).parent.parent))

from tools.readme_generator.generator import ReadmeGenerator
from tools.readme_generator.logging_config import setup_logger


def parse_arguments():
    """
    Parsea los argumentos de línea de comandos.
    
    Returns:
        argparse.Namespace con los argumentos parseados
    """
    parser = argparse.ArgumentParser(
        description='Genera un README.md profesional para el proyecto Reporte de Servicios',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Ejemplos:
  %(prog)s                    Genera README.md con backup automático
  %(prog)s --no-backup        Genera README.md sin crear backup
  %(prog)s --interactive      Pregunta antes de sobrescribir README existente
  %(prog)s --log-level DEBUG  Muestra logs detallados de depuración
  %(prog)s --log-to-file      Guarda logs en archivo además de consola
        """
    )
    
    parser.add_argument(
        '--no-backup',
        action='store_true',
        help='Deshabilita la creación de backup del README existente'
    )
    
    parser.add_argument(
        '--interactive',
        action='store_true',
        help='Pregunta antes de sobrescribir un README existente'
    )
    
    parser.add_argument(
        '--output',
        type=Path,
        default=None,
        help='Ruta de salida personalizada para el README (por defecto: README.md en raíz del proyecto)'
    )
    
    parser.add_argument(
        '--log-level',
        type=str,
        choices=['DEBUG', 'INFO', 'WARNING', 'ERROR', 'CRITICAL'],
        default='INFO',
        help='Nivel de logging (por defecto: INFO)'
    )
    
    parser.add_argument(
        '--log-to-file',
        action='store_true',
        help='Guarda logs en archivo además de mostrarlos en consola'
    )
    
    parser.add_argument(
        '--log-file',
        type=Path,
        default=None,
        help='Ruta del archivo de log (por defecto: readme_generator_TIMESTAMP.log)'
    )
    
    return parser.parse_args()


def confirm_overwrite(readme_path: Path) -> bool:
    """
    Pregunta al usuario si desea sobrescribir el README existente.
    
    Args:
        readme_path: Ruta del README existente
    
    Returns:
        True si el usuario confirma, False en caso contrario
    """
    print(f"\n⚠ El archivo {readme_path} ya existe.")
    response = input("¿Desea sobrescribirlo? [s/N]: ").strip().lower()
    return response in ('s', 'si', 'sí', 'y', 'yes')


def main():
    """
    Función principal del script CLI.
    
    Ejecuta el generador de README con las opciones especificadas
    por el usuario, manejando errores y mostrando mensajes claros.
    """
    # Parsear argumentos
    args = parse_arguments()
    
    # Configurar logger
    logger = setup_logger(
        level=args.log_level,
        log_to_file=args.log_to_file,
        log_file_path=args.log_file
    )
    
    logger.info("Iniciando script de generación de README")
    logger.debug(f"Argumentos: {args}")
    
    # Determinar la ruta raíz del proyecto
    project_root = Path(__file__).parent.parent
    
    # Determinar la ruta de salida
    output_path = args.output if args.output else project_root / "README.md"
    
    print("=" * 60)
    print("Generador de README Profesional")
    print("=" * 60)
    print(f"\n📁 Proyecto: {project_root}")
    print(f"📄 Salida: {output_path}")
    
    if args.log_to_file:
        log_file = args.log_file if args.log_file else f"readme_generator_{Path().cwd().name}.log"
        print(f"📋 Logs: {log_file}")
    
    logger.info(f"Proyecto: {project_root}")
    logger.info(f"Salida: {output_path}")
    
    # Modo interactivo: preguntar antes de sobrescribir
    if args.interactive and output_path.exists():
        logger.debug("Modo interactivo activado, preguntando al usuario")
        if not confirm_overwrite(output_path):
            logger.info("Operación cancelada por el usuario")
            print("\n❌ Operación cancelada por el usuario.")
            sys.exit(0)
    
    # Determinar si crear backup
    create_backup = not args.no_backup
    
    if create_backup and output_path.exists():
        logger.info("Se creará backup del README existente")
        print(f"\n💾 Se creará backup del README existente")
    elif not create_backup and output_path.exists():
        logger.warning("No se creará backup (--no-backup activado)")
        print(f"\n⚠ No se creará backup (--no-backup activado)")
    
    print("\n🔄 Generando README...")
    
    try:
        # Crear el generador con el logger configurado
        logger.debug("Creando instancia de ReadmeGenerator")
        generator = ReadmeGenerator(project_root, logger=logger, log_level=args.log_level)
        
        # Generar y escribir el README
        logger.info("Iniciando generación y escritura del README")
        generator.write_to_file(output_path, backup=create_backup)
        
        print("\n" + "=" * 60)
        print("✅ README generado exitosamente")
        print("=" * 60)
        print(f"\n📄 Archivo: {output_path}")
        
        if create_backup and (output_path.with_suffix('.md.backup')).exists():
            print(f"💾 Backup: {output_path.with_suffix('.md.backup')}")
        
        print("\n💡 Revisa el archivo generado y ajusta según sea necesario.")
        
        logger.info("Proceso completado exitosamente")
        
    except FileNotFoundError as e:
        logger.error(f"Archivo no encontrado: {e}")
        print(f"\n❌ Error: Archivo no encontrado")
        print(f"   {e}")
        sys.exit(1)
    
    except PermissionError as e:
        logger.error(f"Permisos insuficientes: {e}")
        print(f"\n❌ Error: Permisos insuficientes")
        print(f"   {e}")
        print(f"\n💡 Intenta ejecutar el script con permisos adecuados.")
        sys.exit(1)
    
    except ValueError as e:
        logger.error(f"Configuración inválida: {e}")
        print(f"\n❌ Error: Configuración inválida")
        print(f"   {e}")
        print(f"\n💡 Verifica el archivo tools/readme_generator/config.json")
        sys.exit(1)
    
    except Exception as e:
        logger.critical(f"Error inesperado: {type(e).__name__} - {e}", exc_info=True)
        print(f"\n❌ Error inesperado: {type(e).__name__}")
        print(f"   {e}")
        print(f"\n💡 Si el problema persiste, revisa los logs o contacta al desarrollador.")
        sys.exit(1)


if __name__ == "__main__":
    main()
