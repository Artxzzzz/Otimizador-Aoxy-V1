# -*- mode: python ; coding: utf-8 -*-
"""
Arquivo de especificação para PyInstaller - Otimizador Aoxy v1.0
Este arquivo configura como empacotar o app com todos os recursos.
"""

import os
import sys

# Definir o caminho base do projeto
basedir = os.path.dirname(os.path.abspath('build.spec'))
main_dir = os.path.join(basedir, 'meu_app', 'main')

# Definir arquivos de dados (recursos)
datas = [
    (os.path.join(main_dir, 'img'), 'main/img'),           # Ícone e imagens
    (os.path.join(main_dir, 'info'), 'main/info'),         # Arquivo sobre.txt
    (os.path.join(main_dir, 'fonts'), 'main/fonts'),       # Fontes TTF
]

a = Analysis(
    [os.path.join(main_dir, 'main.py')],
    pathex=[main_dir],
    binaries=[],
    datas=datas,
    hiddenimports=['tkinter', 'psutil', 'tktooltip'],
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludedimports=[],
    noarchive=False,
)

pyz = PYZ(a.pure, a.zipped_data, cipher=None)

exe = EXE(
    pyz,
    a.scripts,
    a.binaries,
    a.zipfiles,
    a.datas,
    [],
    name='Otimizador-Aoxy-v1',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    upx_exclude=[],
    runtime_tmpdir=None,
    console=False,  # Sem janela de console
    disable_windowed_traceback=False,
    icon=os.path.join(main_dir, 'img', 'icon.ico'),  # Ícone do EXE
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
)

coll = COLLECT(
    exe,
    a.binaries,
    a.zipfiles,
    a.datas,
    strip=False,
    upx=True,
    upx_exclude=[],
    name='dist',
)
