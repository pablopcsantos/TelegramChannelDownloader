# -*- mode: python ; coding: utf-8 -*-
import os

block_cipher = None

a = Analysis(
    ['main.py'],
    pathex=[],
    binaries=[],
    # 1. Adicionamos os ícones na lista 'datas' para que sejam empacotados dentro do .exe
    datas=[
        ('main.qml', '.'),
        ('icon.ico', '.'),
        ('icon.png', '.')
    ],
    hiddenimports=['PySide6.QtQuick', 'PySide6.QtQml', 'PySide6.QtQuickControls2'],
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    # 2. Excluímos bibliotecas pesadas e módulos do Qt que o seu app não utiliza
    excludes=[
        'PySide6.QtWebEngine', 
        'PySide6.QtWebEngineCore', 
        'PySide6.QtWebEngineQuick',
        'PySide6.Qt3D',
        'PySide6.QtCharts',
        'PySide6.QtDataVisualization',
        'PySide6.QtMultimedia',
        'PySide6.QtMultimediaWidgets',
        'PySide6.QtSql',
        'PySide6.QtTest',
        'PySide6.QtXml',
        'PySide6.QtVirtualKeyboard',
        'matplotlib',
        'numpy',
        'pandas',
        'scipy',
        'tkinter',
        'PyQt5',
        'PyQt6'
    ],
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
    name='TelegramChannelDownloader',
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
    icon='icon.ico' if os.path.exists('icon.ico') else None,
)