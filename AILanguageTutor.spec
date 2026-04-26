# -*- mode: python ; coding: utf-8 -*-
"""
PyInstaller spec fájl az AI Language Tutor alkalmazáshoz.

Használat:
    pyinstaller AILanguageTutor.spec

FONTOS: Először futtasd a frontend build-et:
    cd ai-language-tutor-frontend && npm run build
"""

import os
from pathlib import Path

# Útvonalak
BASE_PATH = Path(SPECPATH)
BACKEND_PATH = BASE_PATH / 'backend'
FRONTEND_DIST = BASE_PATH / 'ai-language-tutor-frontend' / 'dist'

block_cipher = None

a = Analysis(
    ['launcher.py'],
    pathex=[str(BASE_PATH)],
    binaries=[],
    datas=[
        # Backend app mappa
        (str(BACKEND_PATH / 'app'), 'backend/app'),
        # Backend init.py
        (str(BACKEND_PATH / 'init.py'), 'backend'),
        # Frontend build
        (str(FRONTEND_DIST), 'ai-language-tutor-frontend/dist'),
    ],
    hiddenimports=[
        # Uvicorn
        'uvicorn',
        'uvicorn.logging',
        'uvicorn.loops',
        'uvicorn.loops.auto',
        'uvicorn.protocols',
        'uvicorn.protocols.http',
        'uvicorn.protocols.http.auto',
        'uvicorn.protocols.http.h11_impl',
        'uvicorn.protocols.http.httptools_impl',
        'uvicorn.protocols.websockets',
        'uvicorn.protocols.websockets.auto',
        'uvicorn.lifespan',
        'uvicorn.lifespan.on',
        'uvicorn.lifespan.off',
        # FastAPI
        'fastapi',
        'starlette',
        'pydantic',
        # SQLAlchemy
        'sqlalchemy',
        'sqlalchemy.sql.default_comparator',
        'sqlalchemy.ext.baked',
        # Egyéb
        'multipart',
        'email_validator',
        'h11',
        'httptools',
        'websockets',
        'watchfiles',
        'python_dotenv',
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
    [],
    exclude_binaries=True,
    name='AILanguageTutor',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    console=False,  # Nincs konzol ablak
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
    # icon='icon.ico',  # Ikon hozzáadása (ha van)
)

coll = COLLECT(
    exe,
    a.binaries,
    a.zipfiles,
    a.datas,
    strip=False,
    upx=True,
    upx_exclude=[],
    name='AILanguageTutor',
)
