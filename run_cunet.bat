@echo off
title Cunet
color 0a

echo.
echo ========================================
echo    Cunet
echo ========================================
echo.

python --version >nul 2>&1
if errorlevel 1 (
    echo Error: Python is not installed.
    echo Please install Python from https://python.org
    pause
    exit /b 1
)

echo Checking for required libraries...
pip show colorama >nul 2>&1
if errorlevel 1 (
    echo Installing required libraries...
    pip install -r requirements.txt
    if errorlevel 1 (
        echo Failed to install required libraries.
        pause
        exit /b 1
    )
)

echo All requirements are installed.
echo Starting Cunet...
echo.

python Sunet.py

echo.
echo Thank you for using Sunet
pause
