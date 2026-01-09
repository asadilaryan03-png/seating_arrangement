@echo off
REM Streamlit Installation Script

echo.
echo ====================================================
echo   Seating Arrangement System - Streamlit
echo   Installation Script
echo ====================================================
echo.

REM Check if Python is installed
python --version >nul 2>&1
if errorlevel 1 (
    echo ERROR: Python is not installed or not in PATH
    echo Please install Python 3.7+ from python.org
    pause
    exit /b 1
)

echo [1/4] Python found:
python --version
echo.

echo [2/4] Installing required packages...
pip install -r requirements.txt
if errorlevel 1 (
    echo ERROR: Failed to install packages
    pause
    exit /b 1
)
echo Package installation completed!
echo.

echo [3/4] Creating directories...
if not exist uploads (
    mkdir uploads
    echo Created 'uploads' directory
)
echo.

echo [4/4] Verification...
python -c "import streamlit; import pandas; import reportlab; import openpyxl; print('All packages verified successfully!')"
if errorlevel 1 (
    echo ERROR: Some packages could not be imported
    pause
    exit /b 1
)
echo.

echo ====================================================
echo   Installation Completed Successfully!
echo ====================================================
echo.
echo To start the Streamlit app, run:
echo   streamlit run streamlit_app.py
echo.
echo Or simply run:
echo   run_streamlit.bat
echo.
pause
