#!/usr/bin/env python3
"""
Demostración de las funciones implementadas en la tarea 6.4.

Este script muestra el output de las funciones generate_contributing() 
y generate_license_contact() usando la configuración del proyecto.
"""

import json
from pathlib import Path
from tools.readme_generator.sections import generate_contributing, generate_license_contact


def main():
    # Cargar configuración del proyecto
    config_path = Path("tools/readme_generator/config.json")
    with open(config_path, 'r', encoding='utf-8') as f:
        config = json.load(f)
    
    print("=" * 80)
    print("DEMOSTRACIÓN: generate_contributing()")
    print("=" * 80)
    print()
    
    contributing = generate_contributing(config)
    print(contributing)
    
    print("\n" + "=" * 80)
    print("DEMOSTRACIÓN: generate_license_contact()")
    print("=" * 80)
    print()
    
    license_contact = generate_license_contact(config)
    print(license_contact)
    
    print("\n" + "=" * 80)
    print("✅ Ambas funciones ejecutadas exitosamente")
    print("=" * 80)


if __name__ == "__main__":
    main()
