# Plan de Implementación: README Profesional

## Resumen

Este plan implementa un generador de README profesional para el proyecto "Reporte de Servicios". El generador creará un archivo README.md completo en español que incluye todas las secciones requeridas: descripción, instalación, uso, estructura del proyecto, documentación de API, testing, build para Windows, y guías de contribución.

El sistema se compone de 4 componentes principales: ReadmeGenerator (orquestador), SectionGenerators (generadores de contenido), BadgeGenerator (generador de badges), y ProjectInspector (inspector de proyecto). La implementación incluye 22 propiedades de corrección verificables mediante property-based testing con Hypothesis.

## Tareas

- [x] 1. Configurar estructura del proyecto y dependencias
  - Crear directorio `tools/readme_generator/` para el generador
  - Crear archivo `tools/readme_generator/__init__.py`
  - Crear archivo `tools/readme_generator/config.json` con metadatos del proyecto
  - Añadir dependencias necesarias: `hypothesis`, `markdown` (si no están en requirements.txt)
  - _Requisitos: 1.1_

- [x] 2. Implementar modelos de datos y configuración
  - [x] 2.1 Crear dataclasses para metadatos del proyecto
    - Implementar `ProjectMetadata`, `ApiEndpoint`, `TechStack` en `tools/readme_generator/models.py`
    - Incluir validación básica con Pydantic o dataclasses
    - _Requisitos: 2.1, 2.2, 2.3, 3.1, 3.2, 8.1_
  
  - [ ]* 2.2 Escribir property test para modelos de datos
    - **Propiedad: Validación de metadatos**
    - **Valida: Requisitos 2.1, 3.4**
    - Verificar que los modelos acepten datos válidos y rechacen inválidos

- [x] 3. Implementar BadgeGenerator
  - [x] 3.1 Crear clase BadgeGenerator en `tools/readme_generator/badges.py`
    - Implementar métodos estáticos: `python_version()`, `license()`, `project_version()`
    - Generar URLs de shields.io con formato correcto
    - _Requisitos: 2.4, 13.1, 13.2, 13.3, 13.4_
  
  - [ ]* 3.2 Escribir tests unitarios para BadgeGenerator
    - Verificar formato correcto de URLs de shields.io
    - Verificar badges específicos (Python 3.10+, MIT, versión 1.0.0)
    - _Requisitos: 13.1, 13.2, 13.3_
  
  - [ ]* 3.3 Escribir property test para badges
    - **Propiedad 5: Badges Requeridos Presentes**
    - **Valida: Requisitos 2.4, 13.1, 13.2, 13.3, 13.4, 13.5**

- [x] 4. Implementar ProjectInspector
  - [x] 4.1 Crear clase ProjectInspector en `tools/readme_generator/inspector.py`
    - Implementar `__init__(project_root: Path)`
    - Implementar `get_directory_tree(max_depth: int)` para generar árbol de directorios
    - Implementar `get_dependencies()` para parsear requirements.txt
    - Implementar `get_api_endpoints()` con lista predefinida de endpoints
    - _Requisitos: 7.1, 7.2, 7.3, 8.1_
  
  - [ ]* 4.2 Escribir tests unitarios para ProjectInspector
    - Test con proyecto de ejemplo (tmp_path)
    - Test manejo de archivos faltantes
    - Test truncamiento de árbol profundo
    - _Requisitos: 7.1, 7.5_
  
  - [ ]* 4.3 Escribir property test para estructura de directorios
    - **Propiedad 15: Estructura de Directorios con Descripciones**
    - **Valida: Requisitos 7.1, 7.2, 7.3**

- [x] 5. Checkpoint - Verificar componentes base
  - Asegurar que todos los tests pasen, preguntar al usuario si surgen dudas.

- [x] 6. Implementar generadores de secciones individuales
  - [x] 6.1 Crear módulo `tools/readme_generator/sections.py`
    - Implementar `generate_header()` con título, badges y tabla de contenidos
    - Implementar `generate_description()` con descripción y features
    - Implementar `generate_tech_stack()` organizado por categorías
    - _Requisitos: 1.2, 1.4, 2.1, 2.2, 2.3, 2.4, 3.1, 3.2, 3.5_
  
  - [x] 6.2 Implementar secciones de instalación y uso
    - Implementar `generate_installation()` con pasos detallados y alternativas (pip/uv)
    - Implementar `generate_usage()` para desarrolladores
    - Implementar `generate_end_user_guide()` para usuarios finales
    - _Requisitos: 4.1, 4.2, 4.3, 4.4, 4.5, 4.6, 4.7, 5.1, 5.2, 5.3, 5.4, 5.5, 6.1, 6.2, 6.3, 6.4_
  
  - [x] 6.3 Implementar secciones de documentación técnica
    - Implementar `generate_project_structure()` con árbol y descripciones
    - Implementar `generate_api_docs()` con endpoints y ejemplos
    - Implementar `generate_testing()` con comandos pytest
    - Implementar `generate_build_instructions()` para PyInstaller
    - _Requisitos: 7.1, 7.2, 7.3, 7.4, 8.1, 8.2, 8.3, 8.4, 8.5, 9.1, 9.2, 9.3, 9.4, 10.1, 10.2, 10.3, 10.4, 10.5_
  
  - [x] 6.4 Implementar secciones finales
    - Implementar `generate_contributing()` con guías de estilo y proceso
    - Implementar `generate_license_contact()` con licencia, autor y contacto
    - _Requisitos: 11.1, 11.2, 11.3, 11.5, 12.1, 12.2, 12.3, 12.4, 12.5_
  
  - [ ]* 6.5 Escribir tests unitarios para secciones
    - Test contenido específico de cada sección
    - Test formato Markdown de cada sección
    - Test casos edge (sin logo, sin releases, sin coverage)
    - _Requisitos: 1.3, 2.5, 6.5, 9.5, 11.4, 14.4_
  
  - [ ]* 6.6 Escribir property tests para secciones
    - **Propiedad 6: Descripción con Longitud Apropiada**
    - **Valida: Requisitos 2.2**
    - **Propiedad 7: Features Clave Documentadas**
    - **Valida: Requisitos 2.3**
    - **Propiedad 9: Tech Stack Completo y Organizado**
    - **Valida: Requisitos 3.1, 3.2, 3.5**
    - **Propiedad 10: Instrucciones de Instalación con Alternativas**
    - **Valida: Requisitos 4.1, 4.6**
    - **Propiedad 12: Endpoints de API Documentados**
    - **Valida: Requisitos 8.1, 8.2**

- [x] 7. Implementar ReadmeGenerator (orquestador principal)
  - [x] 7.1 Crear clase ReadmeGenerator en `tools/readme_generator/generator.py`
    - Implementar `__init__(project_root: Path)` que carga configuración
    - Implementar `generate()` que orquesta todas las secciones
    - Implementar `write_to_file(output_path: Path, backup: bool)` con manejo de backups
    - Integrar todos los generadores de secciones en orden correcto
    - _Requisitos: 1.1, 1.2, 1.5_
  
  - [x] 7.2 Implementar validación de Markdown
    - Añadir validación de Markdown generado usando librería `markdown`
    - Lanzar `MarkdownValidationError` si el formato es inválido
    - _Requisitos: 1.3_
  
  - [x] 7.3 Implementar manejo de errores
    - Manejo de `FileNotFoundError` para proyecto no encontrado
    - Manejo de `PermissionError` para escritura
    - Advertencias para archivos de documentación faltantes
    - Sistema de backup para README existente
    - _Requisitos: 1.1_
  
  - [ ]* 7.4 Escribir tests unitarios para ReadmeGenerator
    - Test creación de README en directorio raíz
    - Test título específico "Reporte de Servicios"
    - Test manejo de logo faltante
    - Test backup de README existente
    - Test error en proyecto inexistente
    - _Requisitos: 1.1, 2.1_
  
  - [ ]* 7.5 Escribir property tests para ReadmeGenerator
    - **Propiedad 1: Estructura de Secciones Completa y Ordenada**
    - **Valida: Requisitos 1.2, 6.1**
    - **Propiedad 2: Formato Markdown Válido**
    - **Valida: Requisitos 1.3, 7.5**
    - **Propiedad 3: Consistencia de Niveles de Encabezado**
    - **Valida: Requisitos 1.5**
    - **Propiedad 4: Tabla de Contenidos con Enlaces Válidos**
    - **Valida: Requisitos 1.4**

- [x] 8. Checkpoint - Verificar generación completa
  - Asegurar que todos los tests pasen, preguntar al usuario si surgen dudas.

- [ ] 9. Implementar características condicionales y localización
  - [x] 9.1 Añadir lógica condicional para elementos opcionales
    - Logo/screenshot condicional (Propiedad 8)
    - Comando de coverage condicional (Propiedad 19)
    - Link a releases condicional (Propiedad 20)
    - Guidelines de commit condicionales (Propiedad 21)
    - Link a MkDocs condicional (Propiedad 22)
    - _Requisitos: 2.5, 6.5, 9.5, 11.4, 14.4_
  
  - [x] 9.2 Implementar localización en español
    - Asegurar todo el contenido narrativo en español
    - Mantener términos técnicos en inglés (API, endpoint, etc.)
    - Añadir comentarios en español a bloques de código
    - Generar copyright con año actual
    - _Requisitos: 15.1, 15.2, 15.3, 15.4, 15.5, 12.5_
  
  - [ ]* 9.3 Escribir property tests para características condicionales
    - **Propiedad 8: Logo Condicional**
    - **Valida: Requisitos 2.5**
    - **Propiedad 11: Prerrequisitos Antes de Instalación**
    - **Valida: Requisitos 4.7**
    - **Propiedad 18: Copyright con Año Actual**
    - **Valida: Requisitos 12.5**
    - **Propiedad 19: Comando de Coverage Condicional**
    - **Valida: Requisitos 9.5**
    - **Propiedad 20: Link a Releases Condicional**
    - **Valida: Requisitos 6.5**
    - **Propiedad 21: Guidelines de Commit Condicionales**
    - **Valida: Requisitos 11.4**
    - **Propiedad 22: Link a MkDocs Condicional**
    - **Valida: Requisitos 14.4**
  
  - [ ]* 9.4 Escribir property tests para localización
    - **Propiedad 16: Contenido en Español con Términos Técnicos**
    - **Valida: Requisitos 15.1, 15.2, 15.3**
    - **Propiedad 17: Código con Explicaciones en Español**
    - **Valida: Requisitos 15.5**

- [ ] 10. Implementar enlaces a documentación adicional
  - [x] 10.1 Añadir sección de enlaces adicionales
    - Link a guía de usuario (docs/INSTRUCCIONES_USUARIO.md)
    - Link a referencia de API (docs/reference.md)
    - Link a documentación de testing (docs/testing.md)
    - Link a documentación interactiva (/docs)
    - Link a sitio MkDocs (condicional)
    - _Requisitos: 6.2, 8.4, 9.3, 14.1, 14.2, 14.3, 14.4, 14.5_
  
  - [x] 10.2 Implementar validación de enlaces
    - Verificar que archivos referenciados existan
    - Emitir advertencias para enlaces rotos
    - _Requisitos: 14.1, 14.2, 14.3_
  
  - [ ]* 10.3 Escribir property test para enlaces
    - **Propiedad 13: Ejemplo de Request/Response**
    - **Valida: Requisitos 8.3**
    - **Propiedad 14: Enlaces a Documentación Adicional**
    - **Valida: Requisitos 6.2, 8.4, 9.3, 14.1, 14.2, 14.3, 14.5**

- [x] 11. Crear script ejecutable y logging
  - [x] 11.1 Crear script CLI `tools/generate_readme.py`
    - Implementar CLI con argparse para flags (--no-backup, --interactive)
    - Integrar ReadmeGenerator
    - Manejar errores y mostrar mensajes claros
    - _Requisitos: 1.1_
  
  - [x] 11.2 Implementar sistema de logging
    - Configurar logging con niveles DEBUG, INFO, WARNING, ERROR, CRITICAL
    - Logging de progreso de generación
    - Logging de advertencias (archivos faltantes, enlaces rotos)
    - Logging de errores
    - _Requisitos: 1.1_
  
  - [ ]* 11.3 Escribir tests de integración
    - Test ejecución completa del script
    - Test flags de CLI
    - Test logging en diferentes niveles
    - _Requisitos: 1.1_

- [x] 12. Checkpoint final - Verificar implementación completa
  - Asegurar que todos los tests pasen, preguntar al usuario si surgen dudas.

- [x] 13. Generar README.md del proyecto
  - [x] 13.1 Ejecutar el generador en el proyecto real
    - Ejecutar `python tools/generate_readme.py`
    - Verificar que se genere README.md en la raíz
    - Revisar manualmente el contenido generado
    - _Requisitos: 1.1, 1.2_
  
  - [x] 13.2 Validar README generado contra requisitos
    - Verificar todas las secciones presentes
    - Verificar formato Markdown correcto
    - Verificar contenido en español
    - Verificar enlaces funcionales
    - _Requisitos: 1.2, 1.3, 1.4, 1.5, 15.1_

## Notas

- Las tareas marcadas con `*` son opcionales y pueden omitirse para un MVP más rápido
- Cada tarea referencia requisitos específicos para trazabilidad
- Los checkpoints aseguran validación incremental
- Los property tests validan propiedades universales de corrección
- Los unit tests validan ejemplos específicos y casos edge
- El generador debe ser ejecutable de forma independiente mediante CLI
- La configuración del proyecto se mantiene en `tools/readme_generator/config.json`
- El README generado debe cumplir con las 22 propiedades de corrección definidas en el diseño
