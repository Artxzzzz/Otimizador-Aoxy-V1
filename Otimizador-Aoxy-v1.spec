# -*- mode: python ; coding: utf-8 -*-


a = Analysis(
    ['meu_app\\main\\main.py'],
    pathex=[],
    binaries=[],
    datas=[('meu_app/main/img', 'main/img'), ('meu_app/main/info', 'main/info'), ('meu_app/main/fonts', 'main/fonts')],
    hiddenimports=[],
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=[],
    noarchive=False,
    optimize=0,
)
pyz = PYZ(a.pure)

exe = EXE(
    pyz,
    a.scripts,
    a.binaries,
    a.datas,
    [],
    name='Otimizador-Aoxy-v1',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    upx_exclude=[],
    runtime_tmpdir=None,
    console=False,
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
    icon=['meu_app\\main\\img\\icon.ico'],
)
