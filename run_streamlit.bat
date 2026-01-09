@echo off
REM Run Streamlit Application

echo.
echo ====================================================
echo   Seating Arrangement System - Streamlit Edition
echo   Starting Application
echo ====================================================
echo.

REM Check if Python is installed
python --version >nul 2>&1
if errorlevel 1 (
    echo ERROR: Python is not installed
    echo Please run install_streamlit.bat first
    pause
    exit /b 1
)

echo Starting Streamlit application...
echo.
echo The application will open at:
echo   http://localhost:8501
echo.
echo Press Ctrl+C to stop the server
echo.

streamlit run streamlit_app.py

pause
