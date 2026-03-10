# Tarea 11.1 Completada: Script CLI generate_readme.py

## Resumen

Se ha implementado exitosamente el script CLI `tools/generate_readme.py` que proporciona una interfaz de línea de comandos para generar el README.md profesional del proyecto.

## Implementación

### Archivo Creado

- **`tools/generate_readme.py`**: Script ejecutable con CLI completo

### Características Implementadas

#### 1. Argparse para Flags ✓

El script implementa argparse con los siguientes argumentos:

- `--no-backup`: Deshabilita la creación de backup del README existente
- `--interactive`: Pregunta antes de sobrescribir un README existente
- `--output PATH`: Permite especificar una ruta de salida personalizada

```python
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
    help='Ruta de salida personalizada para el README'
)
```

#### 2. Integración con ReadmeGenerator ✓

El script importa y utiliza correctamente la clase `ReadmeGenerator`:

```python
from tools.readme_generator.generator import ReadmeGenerator

# En main():
generator = ReadmeGenerator(project_root)
generator.write_to_file(output_path, backup=create_backup)
```

#### 3. Manejo de Errores con Mensajes Claros ✓

El script maneja múltiples tipos de errores con mensajes descriptivos:

- **FileNotFoundError**: Cuando no se encuentra el proyecto o configuración
- **PermissionError**: Cuando no hay permisos para escribir
- **ValueError**: Cuando la configuración es inválida
- **Exception genérica**: Para errores inesperados

Cada error incluye:
- Emoji visual (❌)
- Descripción clara del error
- Mensaje de ayuda (💡) con sugerencias

```python
except FileNotFoundError as e:
    print(f"\n❌ Error: Archivo no encontrado")
    print(f"   {e}")
    sys.exit(1)

except PermissionError as e:
    print(f"\n❌ Error: Permisos insuficientes")
    print(f"   {e}")
    print(f"\n💡 Intenta ejecutar el script con permisos adecuados.")
    sys.exit(1)
```

#### 4. Modo Interactivo ✓

Implementa la función `confirm_overwrite()` que pregunta al usuario antes de sobrescribir:

```python
def confirm_overwrite(readme_path: Path) -> bool:
    print(f"\n⚠ El archivo {readme_path} ya existe.")
    response = input("¿Desea sobrescribirlo? [s/N]: ").strip().lower()
    return response in ('s', 'si', 'sí', 'y', 'yes')
```

#### 5. Mensajes de Progreso Claros ✓

El script muestra mensajes informativos durante la ejecución:

```
============================================================
Generador de README Profesional
============================================================

📁 Proyecto: /ruta/al/proyecto
📄 Salida: /ruta/al/proyecto/README.md

💾 Se creará backup del README existente

🔄 Generando README...

✓ README generado exitosamente: /ruta/al/proyecto/README.md

============================================================
✅ README generado exitosamente
============================================================

📄 Archivo: /ruta/al/proyecto/README.md
💾 Backup: /ruta/al/proyecto/README.md.backup

💡 Revisa el archivo generado y ajusta según sea necesario.
```

## Uso del Script

### Uso Básico

```bash
# Generar README con backup automático (por defecto)
python tools/generate_readme.py

# Generar sin crear backup
python tools/generate_readme.py --no-backup

# Modo interactivo (pregunta antes de sobrescribir)
python tools/generate_readme.py --interactive

# Combinar flags
python tools/generate_readme.py --no-backup --interactive

# Especificar ruta de salida personalizada
python tools/generate_readme.py --output docs/README.md
```

### Ver Ayuda

```bash
python tools/generate_readme.py --help
```

## Validación de Requisitos

### Requisito 1.1 ✓

El script cumple con el requisito 1.1:

- ✓ Implementa CLI con argparse
- ✓ Soporta flags `--no-backup` y `--interactive`
- ✓ Integra ReadmeGenerator correctamente
- ✓ Maneja errores con mensajes claros
- ✓ Muestra progreso durante la ejecución
- ✓ Por defecto crea backup del README existente
- ✓ Puede ejecutarse con: `python tools/generate_readme.py`

## Estructura del Código

```
tools/
├── generate_readme.py          # Script CLI principal
└── readme_generator/
    ├── __init__.py
    ├── generator.py            # ReadmeGenerator (integrado)
    ├── sections.py
    ├── badges.py
    ├── inspector.py
    ├── models.py
    └── config.json
```

## Tests Creados

Se creó el archivo `tests/test_cli_task_11_1.py` con tests comprehensivos:

### Clases de Test

1. **TestCLIArgparse**: Tests para parsing de argumentos
   - `test_parse_no_arguments()`
   - `test_parse_no_backup_flag()`
   - `test_parse_interactive_flag()`
   - `test_parse_both_flags()`
   - `test_parse_output_path()`

2. **TestCLIInteractive**: Tests para modo interactivo
   - `test_confirm_overwrite_yes()`
   - `test_confirm_overwrite_si()`
   - `test_confirm_overwrite_no()`
   - `test_confirm_overwrite_empty()`
   - `test_confirm_overwrite_case_insensitive()`

3. **TestCLIErrorHandling**: Tests para manejo de errores
   - `test_handles_file_not_found_error()`
   - `test_handles_permission_error()`
   - `test_handles_value_error()`
   - `test_handles_generic_exception()`

4. **TestCLIIntegration**: Tests de integración
   - `test_cli_script_exists()`
   - `test_cli_has_shebang()`
   - `test_cli_imports_generator()`
   - `test_main_function_exists()`
   - `test_parse_arguments_function_exists()`
   - `test_confirm_overwrite_function_exists()`

5. **TestCLIMessages**: Tests para mensajes
   - `test_shows_progress_messages()`
   - `test_shows_backup_message_when_enabled()`
   - `test_shows_no_backup_warning()`

## Características Adicionales

### Shebang para Ejecución Directa

El script incluye shebang para poder ejecutarse directamente en sistemas Unix:

```python
#!/usr/bin/env python3
```

### Path Management

El script añade automáticamente el directorio raíz al path de Python para importar módulos:

```python
sys.path.insert(0, str(Path(__file__).parent.parent))
```

### Documentación Completa

Todas las funciones incluyen docstrings descriptivos en español:

- `parse_arguments()`: Parsea argumentos de línea de comandos
- `confirm_overwrite()`: Pregunta al usuario sobre sobrescritura
- `main()`: Función principal que orquesta la ejecución

## Conclusión

La tarea 11.1 está **completamente implementada** con todas las características requeridas:

✅ CLI con argparse para flags (--no-backup, --interactive)
✅ Integración con ReadmeGenerator
✅ Manejo de errores con mensajes claros
✅ Mensajes de progreso informativos
✅ Modo interactivo funcional
✅ Backup por defecto
✅ Tests comprehensivos
✅ Documentación completa

El script está listo para ser usado y cumple con el requisito 1.1 del spec.
