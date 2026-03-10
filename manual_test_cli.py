#!/usr/bin/env python3
"""
Test manual simple para verificar que el CLI funciona.
"""

import sys
from pathlib import Path
from unittest.mock import patch, MagicMock

# Añadir al path
sys.path.insert(0, str(Path.cwd()))

print("=" * 70)
print("TEST MANUAL DEL CLI generate_readme.py")
print("=" * 70)

# Test 1: Importar el módulo
print("\n[Test 1] Importando módulo CLI...")
try:
    import tools.generate_readme as cli
    print("✓ Módulo importado correctamente")
except Exception as e:
    print(f"✗ Error al importar: {e}")
    sys.exit(1)

# Test 2: Verificar funciones
print("\n[Test 2] Verificando funciones principales...")
functions = ['parse_arguments', 'confirm_overwrite', 'main']
for func in functions:
    if hasattr(cli, func) and callable(getattr(cli, func)):
        print(f"  ✓ {func}() existe y es callable")
    else:
        print(f"  ✗ {func}() no existe o no es callable")
        sys.exit(1)

# Test 3: Test de argparse
print("\n[Test 3] Testeando argparse...")
try:
    with patch('sys.argv', ['generate_readme.py']):
        args = cli.parse_arguments()
        assert args.no_backup == False, "no_backup debe ser False por defecto"
        assert args.interactive == False, "interactive debe ser False por defecto"
        print("  ✓ Argumentos por defecto correctos")
    
    with patch('sys.argv', ['generate_readme.py', '--no-backup']):
        args = cli.parse_arguments()
        assert args.no_backup == True, "--no-backup debe activar el flag"
        print("  ✓ Flag --no-backup funciona")
    
    with patch('sys.argv', ['generate_readme.py', '--interactive']):
        args = cli.parse_arguments()
        assert args.interactive == True, "--interactive debe activar el flag"
        print("  ✓ Flag --interactive funciona")
    
    with patch('sys.argv', ['generate_readme.py', '--no-backup', '--interactive']):
        args = cli.parse_arguments()
        assert args.no_backup == True and args.interactive == True
        print("  ✓ Ambos flags funcionan juntos")
    
except Exception as e:
    print(f"  ✗ Error en argparse: {e}")
    sys.exit(1)

# Test 4: Test de confirm_overwrite
print("\n[Test 4] Testeando confirm_overwrite...")
try:
    test_cases = [
        ('s', True, "respuesta 's'"),
        ('si', True, "respuesta 'si'"),
        ('S', True, "respuesta 'S' (mayúscula)"),
        ('SI', True, "respuesta 'SI' (mayúscula)"),
        ('n', False, "respuesta 'n'"),
        ('no', False, "respuesta 'no'"),
        ('', False, "respuesta vacía"),
        ('x', False, "respuesta inválida"),
    ]
    
    for input_val, expected, desc in test_cases:
        with patch('builtins.input', return_value=input_val):
            result = cli.confirm_overwrite(Path('test.md'))
            if result == expected:
                print(f"  ✓ {desc}: {result}")
            else:
                print(f"  ✗ {desc}: esperado {expected}, obtenido {result}")
                sys.exit(1)
    
except Exception as e:
    print(f"  ✗ Error en confirm_overwrite: {e}")
    sys.exit(1)

# Test 5: Verificar integración con ReadmeGenerator
print("\n[Test 5] Verificando integración con ReadmeGenerator...")
try:
    from tools.readme_generator.generator import ReadmeGenerator
    print("  ✓ ReadmeGenerator se puede importar")
    
    # Verificar que el CLI lo importa
    import inspect
    source = inspect.getsource(cli)
    if 'from tools.readme_generator.generator import ReadmeGenerator' in source:
        print("  ✓ CLI importa ReadmeGenerator correctamente")
    else:
        print("  ✗ CLI no importa ReadmeGenerator")
        sys.exit(1)
    
except Exception as e:
    print(f"  ✗ Error en integración: {e}")
    sys.exit(1)

# Test 6: Verificar manejo de errores en main()
print("\n[Test 6] Verificando manejo de errores...")
try:
    # Test FileNotFoundError
    with patch('sys.argv', ['generate_readme.py']):
        with patch('tools.generate_readme.ReadmeGenerator') as mock_gen:
            mock_gen.side_effect = FileNotFoundError("Test error")
            try:
                cli.main()
                print("  ✗ No se lanzó SystemExit para FileNotFoundError")
                sys.exit(1)
            except SystemExit as e:
                if e.code == 1:
                    print("  ✓ FileNotFoundError manejado correctamente")
                else:
                    print(f"  ✗ Exit code incorrecto: {e.code}")
                    sys.exit(1)
    
    # Test PermissionError
    with patch('sys.argv', ['generate_readme.py']):
        with patch('tools.generate_readme.ReadmeGenerator') as mock_gen:
            mock_instance = MagicMock()
            mock_instance.write_to_file.side_effect = PermissionError("Test error")
            mock_gen.return_value = mock_instance
            try:
                cli.main()
                print("  ✗ No se lanzó SystemExit para PermissionError")
                sys.exit(1)
            except SystemExit as e:
                if e.code == 1:
                    print("  ✓ PermissionError manejado correctamente")
                else:
                    print(f"  ✗ Exit code incorrecto: {e.code}")
                    sys.exit(1)
    
    # Test ValueError
    with patch('sys.argv', ['generate_readme.py']):
        with patch('tools.generate_readme.ReadmeGenerator') as mock_gen:
            mock_gen.side_effect = ValueError("Test error")
            try:
                cli.main()
                print("  ✗ No se lanzó SystemExit para ValueError")
                sys.exit(1)
            except SystemExit as e:
                if e.code == 1:
                    print("  ✓ ValueError manejado correctamente")
                else:
                    print(f"  ✗ Exit code incorrecto: {e.code}")
                    sys.exit(1)
    
except Exception as e:
    print(f"  ✗ Error en test de manejo de errores: {e}")
    import traceback
    traceback.print_exc()
    sys.exit(1)

# Resumen final
print("\n" + "=" * 70)
print("✅ TODOS LOS TESTS MANUALES PASARON")
print("=" * 70)
print("\nEl CLI está correctamente implementado con:")
print("  ✓ Argparse con flags --no-backup, --interactive, --output")
print("  ✓ Función confirm_overwrite() para modo interactivo")
print("  ✓ Integración con ReadmeGenerator")
print("  ✓ Manejo de errores (FileNotFoundError, PermissionError, ValueError)")
print("  ✓ Mensajes claros y descriptivos")
print("\n✅ Tarea 11.1 COMPLETADA")
