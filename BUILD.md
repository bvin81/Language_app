---
project: BUILD
status: active
tags: [project]
created: 2026-04-01
---

# AI Language Tutor - Build és Futtatás

## Gyors indítás (fejlesztés)

### 1. Backend indítása
```bash
cd backend
pip install -r requirements.txt
python init.py                    # Adatbázis inicializálása (első alkalommal)
uvicorn app.main:app --reload     # Backend indítása
```

### 2. Frontend indítása
```bash
cd ai-language-tutor-frontend
npm install
npm run dev
```

---

## Egyszerű indítás (batch script)

Ha már minden telepítve van:
```bash
start_app.bat
```
Ez buildelni a frontendet (ha szükséges) és elindítja az alkalmazást.

---

## EXE készítése

### Előfeltételek
- Python 3.10+
- Node.js 18+
- pip install pyinstaller

### Build lépések

#### 1. Módszer: Automatikus build script
```bash
python build_exe.py
```

#### 2. Módszer: Manuális build

1. **Frontend buildelése:**
```bash
cd ai-language-tutor-frontend
npm install
npm run build
cd ..
```

2. **PyInstaller futtatása:**
```bash
pyinstaller AILanguageTutor.spec
```

3. **Eredmény:**
   - `dist/AILanguageTutor/` - Az alkalmazás mappája
   - `dist/AILanguageTutor/AILanguageTutor.exe` - Az indító EXE

---

## Az EXE használata

1. Másold a teljes `dist/AILanguageTutor` mappát oda, ahol használni szeretnéd
2. Indítsd el az `AILanguageTutor.exe` fájlt
3. A böngésző automatikusan megnyílik az alkalmazással
4. Leállítás: Ctrl+C a konzolban, vagy zárd be az ablakot

---

## Mappastruktúra build után

```
AILanguageTutor/
├── AILanguageTutor.exe          # Indító
├── backend/
│   ├── app/                     # Backend kód
│   ├── init.py                  # DB inicializáló
│   └── language_tutor.db        # Adatbázis (első indításkor jön létre)
├── ai-language-tutor-frontend/
│   └── dist/                    # Frontend build
└── [Python runtime fájlok]
```

---

## Hibaelhárítás

### "Python nincs telepítve"
- Telepítsd a Python-t: https://www.python.org/downloads/
- Pipáld be: "Add Python to PATH"

### "Module not found" hibák
```bash
pip install fastapi uvicorn sqlalchemy python-multipart
```

### "Frontend build not found"
```bash
cd ai-language-tutor-frontend
npm install
npm run build
```

### Az EXE nem indul
- Ellenőrizd, hogy a teljes mappa át lett-e másolva
- Futtasd parancssorból a hibák megtekintéséhez:
  ```bash
  cd AILanguageTutor
  AILanguageTutor.exe
  ```

---

## Fejlesztői megjegyzések

- A backend a `http://127.0.0.1:8000` címen fut
- Production módban a backend szolgálja ki a frontendet is
- Az adatbázis automatikusan létrejön az első indításkor
- API dokumentáció: `http://127.0.0.1:8000/docs`
