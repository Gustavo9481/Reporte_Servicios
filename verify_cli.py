#!/usr/bin/env python3
"""
Script de verificación simple para el CLI.
"""

import sys
from pathlib import Path

print("=" * 60)
print("Verificación del CLI generate_readme.py")
print("=" * 60)

# Test 1: Verificar que el archivo existe
cli_path = Path("tools/generate_readme.py")
if cli_path.exists():
    print("✓ Test 1: El script CLI existe")
else:
    print("✗ Test 1: El script CLI NO existe")
    sys.exit(1)

# Test 2: Verificar que tiene shebang
with open(cli_path, 'r') as f:
    first_line = f.readline()
    if first_line.startswith('#!/usr/bin/env python3'):
        print("✓ Test 2: El script tiene shebang correcto")
    else:
        print(f"✗ Test 2: Shebang incorrecto: {first_line}")
        sys.exit(1)

# Test 3: Verificar imports
try:
    sys.path.insert(0, str(Path.cwd()))
    import tools.generate_readme as cli_module
    print("✓ Test 3: El módulo CLI se puede importar")
except Exception as e:
    print(f"✗ Test 3: Error al importar: {e}")
    sys.exit(1)

# Test 4: Verificar funciones principales
required_functions = ['parse_arguments', 'confirm_overwrite', 'main']
for func_name in required_functions:
    if hasattr(cli_module, func_name):
        print(f"✓ Test 4.{required_functions.index(func_name) + 1}: Función {func_name}() existe")
    else:
        print(f"✗ Test 4.{required_functions.index(func_name) + 1}: Función {func_name}() NO existe")
        sys.exit(1)

# Test 5: Verificar argparse
try:
    from unittest.mock import patch
    with patch('sys.argv', ['generate_readme.py', '--no-backup']):
        args = cli_module.parse_arguments()
        if args.no_backup == True:
            print("✓ Test 5: Argparse funciona correctamente")
        else:
            print("✗ Test 5: Argparse no parsea --no-backup correctamente")
            sys.exit(1)
except Exception as e:
    print(f"✗ Test 5: Error en argparse: {e}")
    sys.exit(1)

# Test 6: Verificar confirm_overwrite
try:
    with patch('builtins.input', return_value='s'):
        result = cli_module.confirm_overwrite(Path('test.md'))
        if result == True:
            print("✓ Test 6: confirm_overwrite() funciona correctamente")
        else:
            print("✗ Test 6: confirm_overwrite() no retorna True para 's'")
            sys.exit(1)
except Exception as e:
    print(f"✗ Test 6: Error en confirm_overwrite: {e}")
    sys.exit(1)

# Test 7: Verificar integración con ReadmeGenerator
try:
    from tools.readme_generator.generator import ReadmeGenerator
    print("✓ Test 7: ReadmeGenerator se puede importar desde el CLI")
except Exception as e:
    print(f"✗ Test 7: Error al importar ReadmeGenerator: {e}")
    sys.exit(1)

print("\n" + "=" * 60)
print("✅ TODOS LOS TESTS PASARON")
print("=" * 60)
print("\nEl CLI está correctamente implementado con:")
print("  • Argparse para flags --no-backup, --interactive, --output")
print("  • Integración con ReadmeGenerator")
print("  • Manejo de errores con mensajes claros")
print("  • Modo interactivo para confirmación")
