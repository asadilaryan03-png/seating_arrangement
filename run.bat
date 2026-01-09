@echo off
REM Run Script for Seating Arrangement System

echo.
echo ====================================================
echo   Seating Arrangement System - Running
echo   VVPIET Solapur
echo ====================================================
echo.

REM Check if Python is installed
python --version >nul 2>&1
if errorlevel 1 (
    echo ERROR: Python is not installed
    echo Please run install.bat first
    pause
    exit /b 1
)

echo Starting the application...
echo.
echo The application will open at:
echo   http://localhost:5000
echo.
echo Press Ctrl+C to stop the server
echo.

python app.py

pause
