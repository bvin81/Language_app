"""
Build script - EXE készítése az AI Language Tutor alkalmazáshoz.

Használat:
    python build_exe.py

Előfeltételek:
    pip install pyinstaller
    npm install (a frontend mappában)
"""
import subprocess
import sys
import os
import shutil
from pathlib import Path


def run_command(command, cwd=None, shell=False):
    """Parancs futtatása és hiba esetén kilépés."""
    print(f">>> {command if isinstance(command, str) else ' '.join(command)}")
    result = subprocess.run(command, cwd=cwd, shell=shell)
    if result.returncode != 0:
        print(f"❌ Hiba történt!")
        sys.exit(1)


def main():
    base_path = Path(__file__).parent
    frontend_path = base_path / "ai-language-tutor-frontend"
    backend_path = base_path / "backend"
    dist_path = base_path / "dist"

    print("=" * 60)
    print("🔨 AI Language Tutor - EXE Build")
    print("=" * 60)
    print()

    # 1. Frontend build
    print("📦 1/4 - Frontend buildelése...")
    if not (frontend_path / "node_modules").exists():
        print("   npm install futtatása...")
        run_command("npm install", cwd=frontend_path, shell=True)

    run_command("npm run build", cwd=frontend_path, shell=True)
    print("✅ Frontend build kész!")
    print()

    # 2. PyInstaller ellenőrzése
    print("📦 2/4 - PyInstaller ellenőrzése...")
    try:
        import PyInstaller
        print(f"✅ PyInstaller verzió: {PyInstaller.__version__}")
    except ImportError:
        print("   PyInstaller telepítése...")
        run_command([sys.executable, "-m", "pip", "install", "pyinstaller"])
    print()

    # 3. EXE készítése
    print("📦 3/4 - EXE készítése PyInstaller-rel...")

    # Összegyűjtjük a szükséges adatokat
    datas = [
        (str(backend_path / "app"), "backend/app"),
        (str(frontend_path / "dist"), "ai-language-tutor-frontend/dist"),
    ]

    # Hidden imports (SQLAlchemy és egyéb modulok)
    hidden_imports = [
        "uvicorn.logging",
        "uvicorn.protocols.http",
        "uvicorn.protocols.http.auto",
        "uvicorn.protocols.websockets",
        "uvicorn.protocols.websockets.auto",
        "uvicorn.lifespan",
        "uvicorn.lifespan.on",
        "sqlalchemy.sql.default_comparator",
        "sqlalchemy.ext.baked",
    ]

    # PyInstaller parancs összeállítása
    pyinstaller_args = [
        sys.executable, "-m", "PyInstaller",
        "--name=AILanguageTutor",
        "--onedir",  # Egy mappába (gyorsabb indulás)
        "--windowed",  # Nincs konzol ablak
        "--icon=NONE",  # Ikon (lecserélhető)
        "--noconfirm",  # Felülírás megerősítés nélkül
    ]

    # Adatok hozzáadása
    for src, dest in datas:
        if Path(src).exists():
            pyinstaller_args.append(f"--add-data={src};{dest}")

    # Hidden imports hozzáadása
    for imp in hidden_imports:
        pyinstaller_args.append(f"--hidden-import={imp}")

    # Launcher script
    pyinstaller_args.append(str(base_path / "launcher.py"))

    run_command(pyinstaller_args, cwd=base_path)
    print("✅ EXE elkészült!")
    print()

    # 4. Kiegészítő fájlok másolása
    print("📦 4/4 - Kiegészítő fájlok másolása...")
    exe_dist_path = dist_path / "AILanguageTutor"

    # Backend mappa létrehozása és fájlok másolása
    backend_dest = exe_dist_path / "backend"
    backend_dest.mkdir(parents=True, exist_ok=True)

    # app mappa másolása
    if (backend_path / "app").exists():
        shutil.copytree(
            backend_path / "app",
            backend_dest / "app",
            dirs_exist_ok=True
        )

    # init.py másolása
    if (backend_path / "init.py").exists():
        shutil.copy(backend_path / "init.py", backend_dest / "init.py")

    # Frontend dist másolása
    frontend_dest = exe_dist_path / "ai-language-tutor-frontend" / "dist"
    if (frontend_path / "dist").exists():
        shutil.copytree(
            frontend_path / "dist",
            frontend_dest,
            dirs_exist_ok=True
        )

    print("✅ Fájlok másolva!")
    print()

    # Kész
    print("=" * 60)
    print("🎉 BUILD SIKERES!")
    print("=" * 60)
    print()
    print(f"📁 Az alkalmazás helye: {exe_dist_path}")
    print(f"🚀 Indítás: {exe_dist_path / 'AILanguageTutor.exe'}")
    print()
    print("💡 Tipp: A teljes mappát másold oda, ahol használni szeretnéd.")


if __name__ == "__main__":
    main()
