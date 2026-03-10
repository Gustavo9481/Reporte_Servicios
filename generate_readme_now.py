#!/usr/bin/env python3
"""Script temporal para generar el README."""

from pathlib import Path
from tools.readme_generator.generator import ReadmeGenerator

if __name__ == "__main__":
    project_root = Path.cwd()
    print(f"Generando README para: {project_root}")
    
    generator = ReadmeGenerator(project_root)
    generator.write_to_file(Path("README.md"), backup=True)
    
    print("✅ README.md generado exitosamente")
