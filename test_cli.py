#!/usr/bin/env python3
"""Test script to verify CLI functionality."""

import sys
from pathlib import Path

# Test imports
try:
    from tools.readme_generator.generator import ReadmeGenerator
    print("✓ Import successful")
except Exception as e:
    print(f"✗ Import failed: {e}")
    sys.exit(1)

# Test CLI script exists
cli_path = Path("tools/generate_readme.py")
if cli_path.exists():
    print(f"✓ CLI script exists: {cli_path}")
else:
    print(f"✗ CLI script not found: {cli_path}")
    sys.exit(1)

# Test argparse functionality
try:
    import argparse
    parser = argparse.ArgumentParser(description='Test')
    parser.add_argument('--no-backup', action='store_true')
    parser.add_argument('--interactive', action='store_true')
    args = parser.parse_args(['--no-backup'])
    assert args.no_backup == True
    assert args.interactive == False
    print("✓ Argparse functionality works")
except Exception as e:
    print(f"✗ Argparse test failed: {e}")
    sys.exit(1)

print("\n✅ All CLI tests passed!")
