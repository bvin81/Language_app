"""
AI Language Tutor - Alkalmazás indító
Elindítja a backend szervert és megnyitja a böngészőt.
"""
import subprocess
import sys
import os
import time
import webbrowser
from pathlib import Path

# Windows-specifikus flag
if sys.platform == "win32":
    CREATE_NO_WINDOW = 0x08000000
else:
    CREATE_NO_WINDOW = 0


def get_base_path():
    """Visszaadja az alkalmazás gyökérkönyvtárát (exe vagy script módban)."""
    if getattr(sys, 'frozen', False):
        # PyInstaller exe módban
        return Path(sys.executable).parent
    else:
        # Normál Python script módban
        return Path(__file__).parent


def init_database():
    """Adatbázis inicializálása, ha még nem létezik."""
    base_path = get_base_path()
    db_path = base_path / "backend" / "language_tutor.db"

    if not db_path.exists():
        print("Adatbazis inicializalasa...")
        original_dir = os.getcwd()
        os.chdir(base_path / "backend")
        subprocess.run([sys.executable, "init.py"], check=True)
        os.chdir(original_dir)
        print("Adatbazis letrehozva!")


def start_backend():
    """Backend szerver indítása."""
    base_path = get_base_path()
    backend_path = base_path / "backend"

    print("Backend szerver inditasa...")

    # Uvicorn indítása
    process = subprocess.Popen(
        [
            sys.executable, "-m", "uvicorn",
            "app.main:app",
            "--host", "127.0.0.1",
            "--port", "8000"
        ],
        cwd=backend_path,
        stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT,
        creationflags=CREATE_NO_WINDOW
    )

    return process


def wait_for_server(url="http://127.0.0.1:8000", timeout=30):
    """Várakozás a szerver elindulására."""
    import urllib.request
    import urllib.error

    print("Varakozas a szerver indulasara...")
    start_time = time.time()

    while time.time() - start_time < timeout:
        try:
            urllib.request.urlopen(url + "/docs", timeout=1)
            return True
        except (urllib.error.URLError, urllib.error.HTTPError):
            time.sleep(0.5)

    return False


def open_browser():
    """Böngésző megnyitása az alkalmazással."""
    url = "http://127.0.0.1:8000"
    print(f"Bongeszo megnyitasa: {url}")
    webbrowser.open(url)


def main():
    print("=" * 50)
    print("    AI Language Tutor")
    print("=" * 50)
    print()

    backend_process = None

    try:
        # Adatbázis inicializálása
        init_database()

        # Backend indítása
        backend_process = start_backend()

        # Várakozás a szerverre
        if wait_for_server():
            print("Szerver elindult!")
            print()
            print("Az alkalmazas elerheto: http://127.0.0.1:8000")
            print("API dokumentacio: http://127.0.0.1:8000/docs")
            print()
            print("A leallitashoz nyomd meg a Ctrl+C billentyukombinaciot")
            print("vagy zard be ezt az ablakot.")
            print()

            # Böngésző megnyitása
            open_browser()

            # Várakozás a felhasználóra
            backend_process.wait()
        else:
            print("HIBA: A szerver nem indult el idoben!")
            sys.exit(1)

    except KeyboardInterrupt:
        print("\nAlkalmazas leallitasa...")
    finally:
        if backend_process:
            backend_process.terminate()
            backend_process.wait()
        print("Leallitva.")


if __name__ == "__main__":
    main()
