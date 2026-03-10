"""
Tests para el script CLI generate_readme.py (Tarea 11.1).

Este módulo verifica que el script CLI funcione correctamente con
argparse, maneje errores apropiadamente, y muestre mensajes claros.

Requisitos: 1.1
"""

import pytest
import sys
import subprocess
from pathlib import Path
from unittest.mock import patch, MagicMock
from io import StringIO


# Importar el módulo CLI
sys.path.insert(0, str(Path(__file__).parent.parent))
from tools import generate_readme


class TestCLIArgparse:
    """Tests para el parsing de argumentos del CLI."""
    
    def test_parse_no_arguments(self):
        """Verifica que sin argumentos use valores por defecto."""
        with patch('sys.argv', ['generate_readme.py']):
            args = generate_readme.parse_arguments()
            assert args.no_backup == False
            assert args.interactive == False
            assert args.output is None
    
    def test_parse_no_backup_flag(self):
        """Verifica que --no-backup se parsee correctamente."""
        with patch('sys.argv', ['generate_readme.py', '--no-backup']):
            args = generate_readme.parse_arguments()
            assert args.no_backup == True
            assert args.interactive == False
    
    def test_parse_interactive_flag(self):
        """Verifica que --interactive se parsee correctamente."""
        with patch('sys.argv', ['generate_readme.py', '--interactive']):
            args = generate_readme.parse_arguments()
            assert args.no_backup == False
            assert args.interactive == True
    
    def test_parse_both_flags(self):
        """Verifica que ambos flags puedan usarse juntos."""
        with patch('sys.argv', ['generate_readme.py', '--no-backup', '--interactive']):
            args = generate_readme.parse_arguments()
            assert args.no_backup == True
            assert args.interactive == True
    
    def test_parse_output_path(self):
        """Verifica que --output se parsee correctamente."""
        with patch('sys.argv', ['generate_readme.py', '--output', 'custom/README.md']):
            args = generate_readme.parse_arguments()
            assert args.output == Path('custom/README.md')


class TestCLIInteractive:
    """Tests para el modo interactivo del CLI."""
    
    def test_confirm_overwrite_yes(self):
        """Verifica que 's' confirme sobrescritura."""
        with patch('builtins.input', return_value='s'):
            result = generate_readme.confirm_overwrite(Path('README.md'))
            assert result == True
    
    def test_confirm_overwrite_si(self):
        """Verifica que 'si' confirme sobrescritura."""
        with patch('builtins.input', return_value='si'):
            result = generate_readme.confirm_overwrite(Path('README.md'))
            assert result == True
    
    def test_confirm_overwrite_no(self):
        """Verifica que 'n' rechace sobrescritura."""
        with patch('builtins.input', return_value='n'):
            result = generate_readme.confirm_overwrite(Path('README.md'))
            assert result == False
    
    def test_confirm_overwrite_empty(self):
        """Verifica que entrada vacía rechace sobrescritura."""
        with patch('builtins.input', return_value=''):
            result = generate_readme.confirm_overwrite(Path('README.md'))
            assert result == False
    
    def test_confirm_overwrite_case_insensitive(self):
        """Verifica que la confirmación sea case-insensitive."""
        with patch('builtins.input', return_value='S'):
            result = generate_readme.confirm_overwrite(Path('README.md'))
            assert result == True
        
        with patch('builtins.input', return_value='SI'):
            result = generate_readme.confirm_overwrite(Path('README.md'))
            assert result == True


class TestCLIErrorHandling:
    """Tests para el manejo de errores del CLI."""
    
    def test_handles_file_not_found_error(self, tmp_path, capsys):
        """Verifica que maneje FileNotFoundError correctamente."""
        # Crear un directorio temporal que no existe
        nonexistent = tmp_path / "nonexistent"
        
        with patch('sys.argv', ['generate_readme.py']):
            with patch('tools.generate_readme.Path') as mock_path:
                mock_path.return_value.parent.parent = nonexistent
                
                with pytest.raises(SystemExit) as exc_info:
                    with patch('tools.generate_readme.ReadmeGenerator') as mock_gen:
                        mock_gen.side_effect = FileNotFoundError("Archivo no encontrado")
                        generate_readme.main()
                
                assert exc_info.value.code == 1
    
    def test_handles_permission_error(self, capsys):
        """Verifica que maneje PermissionError correctamente."""
        with patch('sys.argv', ['generate_readme.py']):
            with pytest.raises(SystemExit) as exc_info:
                with patch('tools.generate_readme.ReadmeGenerator') as mock_gen:
                    mock_instance = MagicMock()
                    mock_instance.write_to_file.side_effect = PermissionError("Sin permisos")
                    mock_gen.return_value = mock_instance
                    generate_readme.main()
            
            assert exc_info.value.code == 1
            captured = capsys.readouterr()
            assert "Permisos insuficientes" in captured.out
    
    def test_handles_value_error(self, capsys):
        """Verifica que maneje ValueError correctamente."""
        with patch('sys.argv', ['generate_readme.py']):
            with pytest.raises(SystemExit) as exc_info:
                with patch('tools.generate_readme.ReadmeGenerator') as mock_gen:
                    mock_gen.side_effect = ValueError("Configuración inválida")
                    generate_readme.main()
            
            assert exc_info.value.code == 1
            captured = capsys.readouterr()
            assert "Configuración inválida" in captured.out
    
    def test_handles_generic_exception(self, capsys):
        """Verifica que maneje excepciones genéricas."""
        with patch('sys.argv', ['generate_readme.py']):
            with pytest.raises(SystemExit) as exc_info:
                with patch('tools.generate_readme.ReadmeGenerator') as mock_gen:
                    mock_gen.side_effect = RuntimeError("Error inesperado")
                    generate_readme.main()
            
            assert exc_info.value.code == 1
            captured = capsys.readouterr()
            assert "Error inesperado" in captured.out


class TestCLIIntegration:
    """Tests de integración para el CLI completo."""
    
    def test_cli_script_exists(self):
        """Verifica que el script CLI exista."""
        cli_path = Path("tools/generate_readme.py")
        assert cli_path.exists(), "El script CLI debe existir"
    
    def test_cli_has_shebang(self):
        """Verifica que el script tenga shebang."""
        cli_path = Path("tools/generate_readme.py")
        with open(cli_path, 'r') as f:
            first_line = f.readline()
            assert first_line.startswith('#!/usr/bin/env python3'), \
                "El script debe tener shebang de Python 3"
    
    def test_cli_imports_generator(self):
        """Verifica que el CLI pueda importar ReadmeGenerator."""
        try:
            from tools.readme_generator.generator import ReadmeGenerator
            assert ReadmeGenerator is not None
        except ImportError as e:
            pytest.fail(f"No se pudo importar ReadmeGenerator: {e}")
    
    def test_main_function_exists(self):
        """Verifica que la función main exista."""
        assert hasattr(generate_readme, 'main'), "Debe existir función main()"
        assert callable(generate_readme.main), "main() debe ser callable"
    
    def test_parse_arguments_function_exists(self):
        """Verifica que la función parse_arguments exista."""
        assert hasattr(generate_readme, 'parse_arguments'), \
            "Debe existir función parse_arguments()"
        assert callable(generate_readme.parse_arguments), \
            "parse_arguments() debe ser callable"
    
    def test_confirm_overwrite_function_exists(self):
        """Verifica que la función confirm_overwrite exista."""
        assert hasattr(generate_readme, 'confirm_overwrite'), \
            "Debe existir función confirm_overwrite()"
        assert callable(generate_readme.confirm_overwrite), \
            "confirm_overwrite() debe ser callable"


class TestCLIMessages:
    """Tests para los mensajes del CLI."""
    
    def test_shows_progress_messages(self, capsys):
        """Verifica que muestre mensajes de progreso."""
        with patch('sys.argv', ['generate_readme.py']):
            with patch('tools.generate_readme.ReadmeGenerator') as mock_gen:
                mock_instance = MagicMock()
                mock_gen.return_value = mock_instance
                
                try:
                    generate_readme.main()
                except SystemExit:
                    pass
                
                captured = capsys.readouterr()
                assert "Generador de README Profesional" in captured.out
                assert "Proyecto:" in captured.out
                assert "Salida:" in captured.out
    
    def test_shows_backup_message_when_enabled(self, tmp_path, capsys):
        """Verifica que muestre mensaje de backup cuando está habilitado."""
        readme_path = tmp_path / "README.md"
        readme_path.write_text("Old content")
        
        with patch('sys.argv', ['generate_readme.py']):
            with patch('tools.generate_readme.Path') as mock_path:
                mock_path.return_value.parent.parent = tmp_path
                mock_path.return_value.exists.return_value = True
                
                with patch('tools.generate_readme.ReadmeGenerator') as mock_gen:
                    mock_instance = MagicMock()
                    mock_gen.return_value = mock_instance
                    
                    try:
                        generate_readme.main()
                    except SystemExit:
                        pass
                    
                    captured = capsys.readouterr()
                    # El mensaje puede variar, pero debe mencionar backup
                    assert "backup" in captured.out.lower() or "Backup" in captured.out
    
    def test_shows_no_backup_warning(self, tmp_path, capsys):
        """Verifica que muestre advertencia cuando --no-backup está activo."""
        readme_path = tmp_path / "README.md"
        readme_path.write_text("Old content")
        
        with patch('sys.argv', ['generate_readme.py', '--no-backup']):
            with patch('tools.generate_readme.Path') as mock_path:
                mock_path.return_value.parent.parent = tmp_path
                mock_path.return_value.exists.return_value = True
                
                with patch('tools.generate_readme.ReadmeGenerator') as mock_gen:
                    mock_instance = MagicMock()
                    mock_gen.return_value = mock_instance
                    
                    try:
                        generate_readme.main()
                    except SystemExit:
                        pass
                    
                    captured = capsys.readouterr()
                    assert "no-backup" in captured.out.lower() or "No se creará backup" in captured.out


if __name__ == "__main__":
    pytest.main([__file__, "-v"])
