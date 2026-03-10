#!/usr/bin/env python3
"""
Script simple para verificar que ReadmeGenerator funciona correctamente.
"""

import sys
from pathlib import Path

# Agregar el directorio raíz al path
sys.path.insert(0, str(Path(__file__).parent))

from tools.readme_generator.generator import ReadmeGenerator


def test_basic_functionality():
    """Test básico de funcionalidad."""
    print("=" * 60)
    print("TEST: Verificación básica de ReadmeGenerator")
    print("=" * 60)
    
    # Test 1: Inicialización
    print("\n1. Probando inicialización...")
    try:
        project_root = Path.cwd()
        generator = ReadmeGenerator(project_root)
        print("   ✓ ReadmeGenerator inicializado correctamente")
        print(f"   ✓ Configuración cargada: {len(generator.config)} claves")
    except Exception as e:
        print(f"   ✗ Error en inicialización: {e}")
        return False
    
    # Test 2: Generación de contenido
    print("\n2. Probando generación de contenido...")
    try:
        readme_content = generator.generate()
        print(f"   ✓ Contenido generado: {len(readme_content)} caracteres")
    except Exception as e:
        print(f"   ✗ Error en generación: {e}")
        return False
    
    # Test 3: Verificar secciones requeridas
    print("\n3. Verificando secciones requeridas...")
    required_sections = [
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
    
    missing_sections = []
    for section in required_sections:
        if section not in readme_content:
            missing_sections.append(section)
    
    if missing_sections:
        print(f"   ✗ Faltan {len(missing_sections)} secciones:")
        for section in missing_sections:
            print(f"      - {section}")
        return False
    else:
        print(f"   ✓ Todas las {len(required_sections)} secciones presentes")
    
    # Test 4: Verificar orden de secciones
    print("\n4. Verificando orden de secciones...")
    sections_to_check = [
        "## Tabla de Contenidos",
        "## Descripción",
        "## Stack Tecnológico",
        "## Instalación",
        "## Uso",
        "## Estructura del Proyecto",
        "## Documentación de API",
        "## Testing",
        "## Contribuir",
        "## Licencia"
    ]
    
    positions = [readme_content.find(section) for section in sections_to_check]
    
    if positions != sorted(positions):
        print("   ✗ Las secciones no están en el orden correcto")
        return False
    else:
        print("   ✓ Secciones en orden correcto")
    
    # Test 5: Verificar integración de generadores
    print("\n5. Verificando integración de generadores de secciones...")
    checks = [
        ("Badges", "![Python]"),
        ("Descripción", "Aplicación web"),
        ("Tech Stack", "FastAPI"),
        ("Instalación", "pip install"),
        ("Uso", "uvicorn"),
        ("API", "/api/"),
        ("Testing", "pytest"),
        ("Build", "PyInstaller"),
        ("Contribuir", "PEP8"),
        ("Licencia", "MIT"),
        ("Contacto", "Gustavo Colmenares")
    ]
    
    failed_checks = []
    for check_name, check_text in checks:
        if check_text not in readme_content:
            failed_checks.append(check_name)
    
    if failed_checks:
        print(f"   ✗ Faltan elementos de: {', '.join(failed_checks)}")
        return False
    else:
        print(f"   ✓ Todos los {len(checks)} elementos verificados")
    
    # Test 6: Escribir archivo de prueba
    print("\n6. Probando escritura de archivo...")
    try:
        test_output = Path("README_TEST.md")
        generator.write_to_file(test_output, backup=False)
        
        if test_output.exists():
            content = test_output.read_text(encoding='utf-8')
            if len(content) > 0:
                print(f"   ✓ Archivo escrito correctamente: {len(content)} caracteres")
                # Limpiar archivo de prueba
                test_output.unlink()
            else:
                print("   ✗ Archivo vacío")
                return False
        else:
            print("   ✗ Archivo no creado")
            return False
    except Exception as e:
        print(f"   ✗ Error al escribir archivo: {e}")
        return False
    
    print("\n" + "=" * 60)
    print("✓ TODOS LOS TESTS PASARON")
    print("=" * 60)
    return True


if __name__ == "__main__":
    success = test_basic_functionality()
    sys.exit(0 if success else 1)
