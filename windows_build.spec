from PyInstaller.utils.hooks import collect_submodules, collect_data_files

# Recolectar automáticamente todos los módulos y datos de librerías críticas
hidden_uvicorn = collect_submodules('uvicorn')
hidden_fastapi = collect_submodules('fastapi')
hidden_starlette = collect_submodules('starlette')
hidden_pydantic = collect_submodules('pydantic')

added_files = [
    ('interface', 'interface'),
] + collect_data_files('uvicorn') + collect_data_files('fastapi')

a = Analysis(
    ['run_app.py'],
    pathex=['.'],
    binaries=[],
    datas=added_files,
    hiddenimports=hidden_uvicorn + hidden_fastapi + hidden_starlette + hidden_pydantic + [
        'email.mime.multipart',
        'email.mime.text',
    ],
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=[],
    win_no_prefer_redirects=False,
    win_private_assemblies=False,
    cipher=block_cipher,
    noarchive=False,
)

pyz = PYZ(a.pure, a.zipped_data, cipher=block_cipher)

exe = EXE(
    pyz,
    a.scripts,
    a.binaries,
    a.zipfiles,
    a.datas,
    [],
    name='Reporte_Servicios',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=False,
    upx_exclude=[],
    runtime_tmpdir=None,
    console=True,  # Cambiar a False si no quieres ver la consola negra
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
    # icon='interface/favicon.ico', # Puedes descomentar esto si tienes un icono .ico
)
