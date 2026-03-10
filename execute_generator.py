from pathlib import Path
from tools.readme_generator.generator import ReadmeGenerator

project_root = Path(".")
output_path = project_root / "README.md"

generator = ReadmeGenerator(project_root)
generator.write_to_file(output_path, backup=True)
print("README generado exitosamente")
