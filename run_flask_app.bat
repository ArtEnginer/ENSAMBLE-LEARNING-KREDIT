@echo off
echo ==========================================
echo  Sistem Prediksi Kredit NPL
echo  Starting Flask Web Application
echo ==========================================
echo.

REM Check if Flask is installed
python -c "import flask" 2>nul
if errorlevel 1 (
    echo [INFO] Flask tidak ditemukan. Menginstall dependencies...
    pip install -r requirements.txt
    echo.
)

echo [INFO] Starting Flask server...
echo [INFO] Aplikasi akan berjalan di: http://localhost:5000
echo [INFO] Tekan Ctrl+C untuk menghentikan server
echo.

python app.py

pause
