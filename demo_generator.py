#!/usr/bin/env python3
"""
Script de demostración para ReadmeGenerator.

Este script demuestra el uso básico de la clase ReadmeGenerator
y genera un README de ejemplo.
"""

import sys
from pathlib import Path

# Asegurar que podemos importar desde tools
sys.path.insert(0, str(Path(__file__).parent))

try:
    from tools.readme_generator.generator import ReadmeGenerator
    
    print("=" * 70)
    print("DEMOSTRACIÓN: ReadmeGenerator")
    print("=" * 70)
    
    # 1. Crear instancia del generador
    print("\n1. Creando instancia de ReadmeGenerator...")
    project_root = Path.cwd()
    generator = ReadmeGenerator(project_root)
    print(f"   ✓ Generador creado para: {project_root}")
    print(f"   ✓ Configuración cargada con {len(generator.config)} claves")
    
    # 2. Generar contenido
    print("\n2. Generando contenido del README...")
    readme_content = generator.generate()
    print(f"   ✓ Contenido generado: {len(readme_content):,} caracteres")
    print(f"   ✓ Líneas generadas: {len(readme_content.splitlines()):,}")
    
    # 3. Mostrar primeras líneas
    print("\n3. Primeras líneas del README generado:")
    print("   " + "-" * 66)
    lines = readme_content.splitlines()[:15]
    for line in lines:
        print(f"   {line}")
    print("   " + "-" * 66)
    print(f"   ... ({len(readme_content.splitlines()) - 15} líneas más)")
    
    # 4. Verificar secciones
    print("\n4. Verificando secciones principales...")
    sections = [
        "# Reporte de Servicios",
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
    
    for section in sections:
        if section in readme_content:
            print(f"   ✓ {section}")
        else:
            print(f"   ✗ {section} (FALTA)")
    
    # 5. Generar archivo de demostración
    print("\n5. Generando archivo de demostración...")
    demo_path = Path("README_DEMO.md")
    generator.write_to_file(demo_path, backup=False)
    
    if demo_path.exists():
        size = demo_path.stat().st_size
        print(f"   ✓ Archivo creado: {demo_path}")
        print(f"   ✓ Tamaño: {size:,} bytes")
        
        # Limpiar archivo de demostración
        print("\n6. Limpiando archivo de demostración...")
        demo_path.unlink()
        print(f"   ✓ Archivo eliminado: {demo_path}")
    
    print("\n" + "=" * 70)
    print("✓ DEMOSTRACIÓN COMPLETADA EXITOSAMENTE")
    print("=" * 70)
    print("\nLa clase ReadmeGenerator está funcionando correctamente.")
    print("Para generar el README real, ejecuta:")
    print("  python tools/generate_readme.py")
    print()
    
except Exception as e:
    print(f"\n✗ ERROR: {e}")
    import traceback
    traceback.print_exc()
    sys.exit(1)
