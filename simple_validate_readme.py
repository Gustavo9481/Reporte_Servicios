#!/usr/bin/env python3
"""Script simple de validación del README.md"""

from pathlib import Path
import re

def main():
    readme = Path('README.md')
    if not readme.exists():
        print("❌ README.md no encontrado")
        return False
    
    content = readme.read_text(encoding='utf-8')
    
    print("🔍 Validando README.md...\n")
    
    # Validar secciones requeridas
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
    
    print("📋 Validando secciones:")
    all_present = True
    for section in sections:
        if section in content:
            print(f"  ✅ {section}")
        else:
            print(f"  ❌ Falta: {section}")
            all_present = False
    
    # Validar badges
    print("\n🏷️  Validando badges:")
    badges = ["![Python]", "![License]", "![Version]"]
    for badge in badges:
        if badge in content:
            print(f"  ✅ {badge}")
        else:
            print(f"  ❌ Falta: {badge}")
    
    # Validar formato Markdown
    print("\n📝 Validando formato Markdown:")
    code_blocks = content.count('```')
    if code_blocks % 2 == 0:
        print(f"  ✅ Bloques de código correctos ({code_blocks // 2} bloques)")
    else:
        print(f"  ❌ Bloques de código mal cerrados")
    
    # Validar enlaces
    print("\n🔗 Validando enlaces:")
    doc_links = [
        "docs/INSTRUCCIONES_USUARIO.md",
        "docs/reference.md",
        "docs/testing.md"
    ]
    for link in doc_links:
        if link in content:
            exists = Path(link).exists()
            status = "✅" if exists else "⚠️ "
            print(f"  {status} {link} {'(existe)' if exists else '(no existe)'}")
    
    # Validar contenido en español
    print("\n🌐 Validando idioma:")
    spanish_words = ['descripción', 'instalación', 'características']
    spanish_count = sum(1 for word in spanish_words if word in content.lower())
    if spanish_count >= 2:
        print(f"  ✅ Contenido en español ({spanish_count}/{len(spanish_words)} palabras clave)")
    else:
        print(f"  ❌ Contenido no parece estar en español")
    
    print("\n" + "="*50)
    if all_present:
        print("✅ README.md VÁLIDO - Todas las secciones presentes")
        return True
    else:
        print("❌ README.md INCOMPLETO - Faltan secciones")
        return False

if __name__ == '__main__':
    success = main()
    exit(0 if success else 1)
