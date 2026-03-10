#!/usr/bin/env python3
"""
Script de validación del README.md generado
Valida contra los requisitos 1.2, 1.3, 1.4, 1.5, 15.1
"""

import re
from pathlib import Path
from typing import List, Tuple


class ReadmeValidator:
    """Validador del README.md generado"""
    
    def __init__(self, readme_path: Path):
        self.readme_path = readme_path
        self.content = readme_path.read_text(encoding='utf-8')
        self.lines = self.content.split('\n')
        self.errors: List[str] = []
        self.warnings: List[str] = []
        self.successes: List[str] = []
    
    def validate_all(self) -> Tuple[bool, dict]:
        """Ejecuta todas las validaciones"""
        print("🔍 Iniciando validación del README.md...\n")
        
        # Requisito 1.2: Estructura de secciones
        self.validate_section_structure()
        
        # Requisito 1.3: Formato Markdown correcto
        self.validate_markdown_format()
        
        # Requisito 1.4: Tabla de contenidos con enlaces
        self.validate_table_of_contents()
        
        # Requisito 1.5: Niveles de encabezado consistentes
        self.validate_heading_levels()
        
        # Requisito 15.1: Contenido en español
        self.validate_spanish_content()
        
        # Enlaces funcionales
        self.validate_links()
        
        # Generar reporte
        return self.generate_report()
    
    def validate_section_structure(self):
        """Valida que todas las secciones requeridas estén presentes y en orden"""
        print("📋 Validando estructura de secciones...")
        
        required_sections = [
            ("# Reporte de Servicios", "Título del proyecto"),
            ("![Python]", "Badge de Python"),
            ("![License]", "Badge de Licencia"),
            ("![Version]", "Badge de Versión"),
            ("## Tabla de Contenidos", "Tabla de contenidos"),
            ("## Descripción", "Descripción"),
            ("## Características", "Características"),
            ("## Stack Tecnológico", "Stack Tecnológico"),
            ("## Instalación", "Instalación"),
            ("## Uso", "Uso"),
            ("## Estructura del Proyecto", "Estructura del Proyecto"),
            ("## Documentación de API", "Documentación de API"),
            ("## Testing", "Testing"),
            ("## Build para Windows", "Build para Windows"),
            ("## Contribuir", "Contribuir"),
            ("## Licencia", "Licencia"),
            ("## Contacto", "Contacto"),
        ]
        
        positions = []
        for section, name in required_sections:
            pos = self.content.find(section)
            if pos == -1:
                self.errors.append(f"❌ Falta la sección: {name}")
            else:
                positions.append((pos, name))
                self.successes.append(f"✅ Sección presente: {name}")
        
        # Verificar orden
        if positions:
            sorted_positions = sorted(positions, key=lambda x: x[0])
            if positions != sorted_positions:
                self.errors.append("❌ Las secciones no están en el orden correcto")
            else:
                self.successes.append("✅ Todas las secciones están en el orden correcto")
    
    def validate_markdown_format(self):
        """Valida que el Markdown sea sintácticamente válido"""
        print("📝 Validando formato Markdown...")
        
        # Verificar elementos específicos de Markdown
        has_code_blocks = '```' in self.content
        has_lists = bool(re.search(r'^[-*+] ', self.content, re.MULTILINE))
        has_links = '[' in self.content and '](' in self.content
        has_headers = bool(re.search(r'^#{1,6} ', self.content, re.MULTILINE))
        
        # Verificar sintaxis básica de Markdown
        markdown_valid = True
        
        # Verificar que los bloques de código estén cerrados
        code_block_count = self.content.count('```')
        if code_block_count % 2 != 0:
            self.errors.append("❌ Bloques de código no están correctamente cerrados")
            markdown_valid = False
        
        # Verificar que los enlaces tengan formato correcto
        broken_links = re.findall(r'\[([^\]]*)\]\([^\)]*$', self.content, re.MULTILINE)
        if broken_links:
            self.errors.append(f"❌ Enlaces mal formados encontrados: {len(broken_links)}")
            markdown_valid = False
        
        if markdown_valid:
            self.successes.append("✅ El Markdown tiene sintaxis válida")
        
        if has_headers:
            self.successes.append("✅ Contiene encabezados")
        else:
            self.errors.append("❌ No se encontraron encabezados")
        
        if has_code_blocks:
            self.successes.append("✅ Contiene bloques de código")
        else:
            self.warnings.append("⚠️  No se encontraron bloques de código")
        
        if has_lists:
            self.successes.append("✅ Contiene listas")
        else:
            self.warnings.append("⚠️  No se encontraron listas")
        
        if has_links:
            self.successes.append("✅ Contiene enlaces")
        else:
            self.errors.append("❌ No se encontraron enlaces")
    
    def validate_table_of_contents(self):
        """Valida la tabla de contenidos y sus enlaces"""
        print("🔗 Validando tabla de contenidos...")
        
        # Buscar la sección de tabla de contenidos
        toc_start = self.content.find("## Tabla de Contenidos")
        if toc_start == -1:
            self.errors.append("❌ No se encontró la tabla de contenidos")
            return
        
        # Extraer enlaces de la tabla de contenidos
        toc_section = self.content[toc_start:toc_start + 1000]
        toc_links = re.findall(r'\[([^\]]+)\]\(#([^\)]+)\)', toc_section)
        
        if not toc_links:
            self.errors.append("❌ La tabla de contenidos no tiene enlaces")
            return
        
        self.successes.append(f"✅ Tabla de contenidos con {len(toc_links)} enlaces")
        
        # Verificar que cada enlace apunte a un encabezado existente
        for link_text, anchor in toc_links:
            # Buscar el encabezado correspondiente
            # Los anchors en Markdown se generan convirtiendo el texto a minúsculas
            # y reemplazando espacios con guiones
            expected_heading = f"## {link_text}"
            
            # Buscar variaciones del encabezado
            found = False
            for line in self.lines:
                if line.strip().startswith('##') and link_text.lower() in line.lower():
                    found = True
                    break
            
            if found:
                self.successes.append(f"✅ Enlace válido: {link_text}")
            else:
                self.warnings.append(f"⚠️  Enlace posiblemente roto: {link_text}")
    
    def validate_heading_levels(self):
        """Valida la consistencia de los niveles de encabezado"""
        print("📊 Validando niveles de encabezado...")
        
        h1_count = len([l for l in self.lines if l.startswith('# ') and not l.startswith('## ')])
        h2_count = len([l for l in self.lines if l.startswith('## ') and not l.startswith('### ')])
        h3_count = len([l for l in self.lines if l.startswith('### ') and not l.startswith('#### ')])
        h4_count = len([l for l in self.lines if l.startswith('#### ')])
        
        # Debe haber exactamente un H1 (el título)
        if h1_count == 1:
            self.successes.append("✅ Un único título H1")
        else:
            self.errors.append(f"❌ Se encontraron {h1_count} títulos H1 (debe ser 1)")
        
        # Debe haber múltiples H2 (secciones principales)
        if h2_count >= 10:
            self.successes.append(f"✅ {h2_count} secciones principales (H2)")
        else:
            self.warnings.append(f"⚠️  Solo {h2_count} secciones H2 (esperadas >= 10)")
        
        # Puede haber H3 (subsecciones)
        if h3_count > 0:
            self.successes.append(f"✅ {h3_count} subsecciones (H3)")
        
        # No debe haber H4 o superiores en secciones principales
        if h4_count == 0:
            self.successes.append("✅ No hay encabezados H4 o superiores")
        else:
            self.warnings.append(f"⚠️  Se encontraron {h4_count} encabezados H4")
    
    def validate_spanish_content(self):
        """Valida que el contenido esté en español"""
        print("🌐 Validando contenido en español...")
        
        # Palabras clave en español que deben estar presentes
        spanish_keywords = [
            'descripción', 'características', 'instalación', 'uso',
            'estructura', 'documentación', 'licencia', 'contacto',
            'para', 'con', 'del', 'los', 'las', 'proyecto'
        ]
        
        content_lower = self.content.lower()
        found_keywords = [kw for kw in spanish_keywords if kw in content_lower]
        
        if len(found_keywords) >= len(spanish_keywords) * 0.8:
            self.successes.append(f"✅ Contenido en español ({len(found_keywords)}/{len(spanish_keywords)} palabras clave)")
        else:
            self.errors.append(f"❌ Contenido no parece estar en español ({len(found_keywords)}/{len(spanish_keywords)} palabras clave)")
        
        # Verificar que términos técnicos estén en inglés
        technical_terms = ['API', 'endpoint', 'FastAPI', 'SQLite', 'pytest']
        found_technical = [term for term in technical_terms if term in self.content]
        
        if len(found_technical) >= 3:
            self.successes.append(f"✅ Términos técnicos en inglés presentes ({len(found_technical)})")
        else:
            self.warnings.append(f"⚠️  Pocos términos técnicos encontrados ({len(found_technical)})")
    
    def validate_links(self):
        """Valida que los enlaces a documentación existan"""
        print("🔗 Validando enlaces a documentación...")
        
        # Enlaces a archivos de documentación
        doc_links = [
            ('docs/INSTRUCCIONES_USUARIO.md', 'Guía de Usuario'),
            ('docs/reference.md', 'Documentación de Referencia'),
            ('docs/testing.md', 'Documentación de Testing'),
        ]
        
        for file_path, name in doc_links:
            if file_path in self.content:
                self.successes.append(f"✅ Enlace presente: {name}")
                
                # Verificar si el archivo existe
                if Path(file_path).exists():
                    self.successes.append(f"✅ Archivo existe: {file_path}")
                else:
                    self.warnings.append(f"⚠️  Archivo no existe: {file_path}")
            else:
                self.warnings.append(f"⚠️  Enlace no encontrado: {name}")
        
        # Enlaces a documentación interactiva
        interactive_links = ['/docs', '/redoc']
        for link in interactive_links:
            if link in self.content:
                self.successes.append(f"✅ Enlace a documentación interactiva: {link}")
    
    def generate_report(self) -> Tuple[bool, dict]:
        """Genera el reporte final de validación"""
        print("\n" + "="*70)
        print("📊 REPORTE DE VALIDACIÓN DEL README.md")
        print("="*70 + "\n")
        
        # Éxitos
        if self.successes:
            print("✅ VALIDACIONES EXITOSAS:")
            for success in self.successes:
                print(f"  {success}")
            print()
        
        # Advertencias
        if self.warnings:
            print("⚠️  ADVERTENCIAS:")
            for warning in self.warnings:
                print(f"  {warning}")
            print()
        
        # Errores
        if self.errors:
            print("❌ ERRORES:")
            for error in self.errors:
                print(f"  {error}")
            print()
        
        # Resumen
        total_checks = len(self.successes) + len(self.warnings) + len(self.errors)
        success_rate = (len(self.successes) / total_checks * 100) if total_checks > 0 else 0
        
        print("="*70)
        print(f"📈 RESUMEN:")
        print(f"  ✅ Éxitos: {len(self.successes)}")
        print(f"  ⚠️  Advertencias: {len(self.warnings)}")
        print(f"  ❌ Errores: {len(self.errors)}")
        print(f"  📊 Tasa de éxito: {success_rate:.1f}%")
        print("="*70 + "\n")
        
        is_valid = len(self.errors) == 0
        
        if is_valid:
            print("🎉 ¡README.md VÁLIDO! Cumple con todos los requisitos.")
        else:
            print("❌ README.md tiene errores que deben corregirse.")
        
        return is_valid, {
            'successes': self.successes,
            'warnings': self.warnings,
            'errors': self.errors,
            'success_rate': success_rate,
            'is_valid': is_valid
        }


def main():
    """Función principal"""
    readme_path = Path('README.md')
    
    if not readme_path.exists():
        print("❌ Error: No se encontró el archivo README.md")
        return 1
    
    validator = ReadmeValidator(readme_path)
    is_valid, report = validator.validate_all()
    
    return 0 if is_valid else 1


if __name__ == '__main__':
    exit(main())
