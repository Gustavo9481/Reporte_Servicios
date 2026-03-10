"""Script para generar README manualmente."""

import json
from pathlib import Path
from datetime import datetime

# Cargar configuración
config_path = Path("tools/readme_generator/config.json")
with open(config_path, 'r', encoding='utf-8') as f:
    config = json.load(f)

# Importar funciones de generación
import sys
sys.path.insert(0, str(Path.cwd()))

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

# Generar todas las secciones
sections = []

print("Generando secciones del README...")

sections.append(generate_header(config))
print("✓ Header generado")

sections.append(generate_description(config))
print("✓ Descripción generada")

sections.append(generate_tech_stack(config))
print("✓ Stack tecnológico generado")

sections.append(generate_installation(config))
print("✓ Instalación generada")

sections.append(generate_usage(config))
print("✓ Uso generado")

sections.append(generate_end_user_guide(config))
print("✓ Guía de usuario final generada")

sections.append(generate_project_structure(config))
print("✓ Estructura del proyecto generada")

sections.append(generate_api_docs(config))
print("✓ Documentación de API generada")

sections.append(generate_testing(config))
print("✓ Testing generado")

sections.append(generate_build_instructions(config))
print("✓ Instrucciones de build generadas")

sections.append(generate_contributing(config))
print("✓ Contribuir generado")

sections.append(generate_license_contact(config))
print("✓ Licencia y contacto generados")

# Unir todas las secciones
readme_content = "\n\n".join(sections)

# Crear backup si existe README.md
readme_path = Path("README.md")
if readme_path.exists():
    backup_path = Path("README.md.backup")
    import shutil
    shutil.copy2(readme_path, backup_path)
    print(f"✓ Backup creado: {backup_path}")

# Escribir el README
with open(readme_path, 'w', encoding='utf-8') as f:
    f.write(readme_content)

print(f"\n✅ README generado exitosamente: {readme_path}")
print(f"   Tamaño: {len(readme_content)} caracteres")
