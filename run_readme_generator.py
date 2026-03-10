#!/usr/bin/env python3
"""Script temporal para ejecutar el generador de README."""

from pathlib import Path
from tools.readme_generator.generator import ReadmeGenerator
from tools.readme_generator.logging_config import setup_logger

# Configurar logger
logger = setup_logger(level='INFO', log_to_file=False)

# Determinar la ruta raíz del proyecto
project_root = Path(__file__).parent

# Ruta de salida
output_path = project_root / "README.md"

print("=" * 60)
print("Generador de README Profesional")
print("=" * 60)
print(f"\n📁 Proyecto: {project_root}")
print(f"📄 Salida: {output_path}")

print("\n🔄 Generando README...")

try:
    # Crear el generador
    generator = ReadmeGenerator(project_root, logger=logger, log_level='INFO')
    
    # Generar y escribir el README
    generator.write_to_file(output_path, backup=True)
    
    print("\n" + "=" * 60)
    print("✅ README generado exitosamente")
    print("=" * 60)
    print(f"\n📄 Archivo: {output_path}")
    
    backup_path = output_path.with_suffix('.md.backup')
    if backup_path.exists():
        print(f"💾 Backup: {backup_path}")
    
    print("\n💡 Revisa el archivo generado y ajusta según sea necesario.")
    
except Exception as e:
    print(f"\n❌ Error: {type(e).__name__}")
    print(f"   {e}")
    import traceback
    traceback.print_exc()
