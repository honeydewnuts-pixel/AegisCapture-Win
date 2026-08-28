# -*- mode: python ; coding: utf-8 -*-
block_cipher = None
a = Analysis(
    ['main.py'],
    pathex=[],
    binaries=[],
    datas=[
        ('assets/mt5_color_match_guide.jpg', 'assets'),
        ('guides/mt5_color_match_guide.jpg', 'guides'),
        ('mq5/AEGIS_Executor.mq5', 'mq5'),
    ],
    hiddenimports=['mss', 'PIL', 'requests'],
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
    name='AEGIS_Capture',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    console=False,
    icon=None,
)
