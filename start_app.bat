@echo off
title AI Language Tutor
echo ================================================
echo          AI Language Tutor
echo ================================================
echo.

REM Ellenőrizzük, hogy létezik-e a Python
python --version >nul 2>&1
if errorlevel 1 (
    echo HIBA: Python nincs telepitve!
    echo Telepitsd a Python-t: https://www.python.org/downloads/
    pause
    exit /b 1
)

REM Frontend build ellenőrzése
if not exist "ai-language-tutor-frontend\dist\index.html" (
    echo Frontend buildelese szukseges...
    cd ai-language-tutor-frontend
    call npm install
    call npm run build
    cd ..
)

REM Alkalmazás indítása
echo Alkalmazas inditasa...
python launcher.py

pause
