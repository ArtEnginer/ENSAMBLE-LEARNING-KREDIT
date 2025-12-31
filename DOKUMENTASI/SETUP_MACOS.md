# 🍎 Setup dan Menjalankan Aplikasi di macOS

Panduan lengkap untuk menjalankan Aplikasi Prediksi Kredit Macet berbasis Flask di macOS.

---

## 📋 Daftar Isi

1. [Prasyarat](#-prasyarat)
2. [Instalasi Python](#-instalasi-python)
3. [Setup Project](#-setup-project)
4. [Instalasi Dependencies](#-instalasi-dependencies)
5. [Menjalankan Aplikasi](#-menjalankan-aplikasi)
6. [Troubleshooting](#-troubleshooting)

---

## 🔧 Prasyarat

Pastikan sistem macOS Anda memenuhi persyaratan berikut:

- **macOS Version**: 10.14 (Mojave) atau lebih baru
- **RAM**: Minimal 4GB (Disarankan 8GB)
- **Storage**: Minimal 2GB ruang kosong
- **Terminal**: Terminal bawaan atau iTerm2
- **Homebrew**: Package manager untuk macOS (opsional tapi disarankan)

---

## 🐍 Instalasi Python

### Opsi 1: Menggunakan Homebrew (Disarankan)

1. **Install Homebrew** (jika belum ada):
   ```bash
   /bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
   ```

2. **Install Python 3**:
   ```bash
   brew install python@3.11
   ```

3. **Verifikasi instalasi**:
   ```bash
   python3 --version
   # Output: Python 3.11.x
   ```

### Opsi 2: Download dari Python.org

1. Kunjungi [https://www.python.org/downloads/macos/](https://www.python.org/downloads/macos/)
2. Download Python 3.11 atau lebih baru
3. Install dengan mengikuti wizard instalasi
4. Verifikasi di Terminal:
   ```bash
   python3 --version
   ```

---

## 📂 Setup Project

### 1. Download Project

**Jika menggunakan Git:**
```bash
# Clone repository
git clone <repository-url>
cd ENSAMBLE-LEARNING-KREDIT
```

**Jika menggunakan file ZIP:**
```bash
# Extract file ZIP dan masuk ke folder
cd ~/Downloads/ENSAMBLE-LEARNING-KREDIT
```

### 2. Struktur Folder

Pastikan struktur folder seperti berikut:
```
ENSAMBLE-LEARNING-KREDIT/
├── app.py
├── requirements.txt
├── DATASET/
│   └── dataset_npl.csv
├── models/
│   └── model_20251231_125152/
│       ├── best_model_random_forest.joblib
│       ├── label_encoders.joblib
│       ├── model_metadata.json
│       ├── scaler.joblib
│       └── target_encoder.joblib
└── templates/
    ├── index.html
    ├── predict.html
    └── ... (file HTML lainnya)
```

---

## 📦 Instalasi Dependencies

### 1. Buat Virtual Environment

Virtual environment membantu mengisolasi dependencies project:

```bash
# Masuk ke folder project
cd ENSAMBLE-LEARNING-KREDIT

# Buat virtual environment
python3 -m venv venv

# Aktivasi virtual environment
source venv/bin/activate
```

**Catatan**: Setelah aktivasi, prompt terminal akan berubah menjadi:
```
(venv) username@macbook ENSAMBLE-LEARNING-KREDIT %
```

### 2. Upgrade pip

```bash
pip install --upgrade pip
```

### 3. Install Dependencies

```bash
# Install semua package dari requirements.txt
pip install -r requirements.txt
```

**Proses ini akan menginstall:**
- Flask (Web framework)
- Pandas & NumPy (Data processing)
- Scikit-learn (Machine learning)
- XGBoost & LightGBM (Advanced ML algorithms)
- Matplotlib & Seaborn (Visualization)
- Dan dependencies lainnya

**Estimasi waktu**: 5-10 menit tergantung koneksi internet

### 4. Verifikasi Instalasi

```bash
# Cek package terinstall
pip list

# Verifikasi package penting
python3 -c "import flask; import sklearn; import pandas; print('All dependencies OK!')"
```

---

## 🚀 Menjalankan Aplikasi

### 1. Pastikan Virtual Environment Aktif

```bash
# Jika belum aktif, jalankan:
source venv/bin/activate
```

### 2. Jalankan Flask Application

```bash
python3 app.py
```

**Output yang diharapkan:**
```
 * Serving Flask app 'app'
 * Debug mode: on
WARNING: This is a development server. Do not use it in a production deployment.
 * Running on http://127.0.0.1:5000
Press CTRL+C to quit
 * Restarting with stat
 * Debugger is active!
```

### 3. Akses Aplikasi

Buka browser (Safari, Chrome, Firefox) dan akses:
```
http://localhost:5000
```
atau
```
http://127.0.0.1:5000
```

### 4. Menghentikan Aplikasi

Di terminal, tekan:
```
CTRL + C
```

### 5. Deaktivasi Virtual Environment

Setelah selesai:
```bash
deactivate
```

---

## 🔍 Troubleshooting

### Problem 1: Command not found: python3

**Solusi:**
```bash
# Cek lokasi Python
which python3

# Jika tidak ada, install Python dari Homebrew
brew install python@3.11
```

### Problem 2: Permission denied

**Solusi:**
```bash
# Berikan permission execute
chmod +x app.py

# Atau gunakan sudo (tidak disarankan untuk venv)
# Lebih baik fix ownership folder
sudo chown -R $USER:staff ~/path/to/project
```

### Problem 3: pip install gagal

**Solusi:**
```bash
# Update pip dan setuptools
pip install --upgrade pip setuptools wheel

# Install ulang dependencies
pip install -r requirements.txt --no-cache-dir
```

### Problem 4: Port 5000 sudah digunakan

**Error:**
```
OSError: [Errno 48] Address already in use
```

**Solusi:**

Opsi 1 - Cari proses yang menggunakan port:
```bash
# Cari PID yang menggunakan port 5000
lsof -i :5000

# Kill proses tersebut
kill -9 <PID>
```

Opsi 2 - Ubah port di app.py:
```python
# Di akhir file app.py, ubah:
if __name__ == '__main__':
    app.run(debug=True, port=5001)  # Ganti ke port 5001
```

### Problem 5: Model file tidak ditemukan

**Error:**
```
FileNotFoundError: [Errno 2] No such file or directory: 'models/...'
```

**Solusi:**
```bash
# Pastikan berada di folder yang benar
pwd
# Output harus: /path/to/ENSAMBLE-LEARNING-KREDIT

# Cek apakah folder models ada
ls -la models/

# Pastikan model terbaru ada
ls -la models/model_20251231_125152/
```

### Problem 6: Import error dengan scikit-learn

**Error:**
```
ImportError: cannot import name '...' from 'sklearn'
```

**Solusi:**
```bash
# Uninstall dan reinstall scikit-learn
pip uninstall scikit-learn -y
pip install scikit-learn==1.7.2
```

### Problem 7: M1/M2/M3 Chip Compatibility Issues

Untuk Mac dengan Apple Silicon (M1/M2/M3):

```bash
# Install Rosetta 2 (jika belum)
softwareupdate --install-rosetta

# Atau install dengan arsitektur spesifik
arch -arm64 pip install -r requirements.txt

# Untuk package yang bermasalah (misal: LightGBM)
brew install cmake libomp
pip install lightgbm --install-option=--precompiled
```

### Problem 8: SSL Certificate Error

**Error:**
```
SSL: CERTIFICATE_VERIFY_FAILED
```

**Solusi:**
```bash
# Install certificates
/Applications/Python\ 3.11/Install\ Certificates.command

# Atau update certifi
pip install --upgrade certifi
```

---

## 📱 Tips Penggunaan di macOS

### 1. Shortcut Terminal yang Berguna

```bash
# Buka folder di Finder
open .

# Buka aplikasi di browser default
open http://localhost:5000

# Clear terminal
clear
# atau CMD + K
```

### 2. Menjalankan di Background

```bash
# Jalankan di background
nohup python3 app.py > app.log 2>&1 &

# Cek process
ps aux | grep app.py

# Stop process
kill <PID>
```

### 3. Auto-start saat Login (Opsional)

Buat file `.plist` di `~/Library/LaunchAgents/`:

```bash
nano ~/Library/LaunchAgents/com.kreditmacet.app.plist
```

Isi dengan:
```xml
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
<dict>
    <key>Label</key>
    <string>com.kreditmacet.app</string>
    <key>ProgramArguments</key>
    <array>
        <string>/path/to/venv/bin/python3</string>
        <string>/path/to/app.py</string>
    </array>
    <key>RunAtLoad</key>
    <true/>
    <key>WorkingDirectory</key>
    <string>/path/to/ENSAMBLE-LEARNING-KREDIT</string>
</dict>
</plist>
```

Load service:
```bash
launchctl load ~/Library/LaunchAgents/com.kreditmacet.app.plist
```

---

## 🔒 Keamanan & Best Practices

### 1. Jangan Jalankan sebagai Root

```bash
# JANGAN ini:
sudo python3 app.py

# Gunakan ini:
python3 app.py
```

### 2. Firewall Settings

```bash
# Cek firewall status
sudo /usr/libexec/ApplicationFirewall/socketfilterfw --getglobalstate

# Allow Python connections (jika diperlukan)
sudo /usr/libexec/ApplicationFirewall/socketfilterfw --add /usr/local/bin/python3
```

### 3. Environment Variables (Jika ada)

Buat file `.env`:
```bash
nano .env
```

Isi dengan:
```
FLASK_ENV=development
FLASK_DEBUG=1
SECRET_KEY=your-secret-key-here
```

---

## 📊 Monitoring & Logging

### 1. Lihat Log Real-time

```bash
# Jalankan dengan logging
python3 app.py 2>&1 | tee app.log
```

### 2. Monitoring Resource

```bash
# Monitor CPU & Memory
top

# Atau gunakan Activity Monitor (GUI)
open -a "Activity Monitor"
```

---

## 🔄 Update & Maintenance

### Update Dependencies

```bash
# Aktivasi virtual environment
source venv/bin/activate

# Update semua package
pip list --outdated
pip install --upgrade <package-name>

# Atau update semua sekaligus (hati-hati!)
pip install --upgrade -r requirements.txt
```

### Backup Model

```bash
# Backup folder models
cp -r models/ models_backup_$(date +%Y%m%d)/

# Atau buat archive
tar -czf models_backup_$(date +%Y%m%d).tar.gz models/
```

---

## 🌐 Akses dari Device Lain di Network

### 1. Cari IP Address Mac

```bash
# Cari IP local
ifconfig | grep "inet "
# atau
ipconfig getifaddr en0
```

### 2. Ubah app.py

```python
if __name__ == '__main__':
    # Ganti 127.0.0.1 dengan 0.0.0.0 agar bisa diakses dari network
    app.run(debug=True, host='0.0.0.0', port=5000)
```

### 3. Akses dari Device Lain

```
http://<IP-MAC-ANDA>:5000
# Contoh: http://192.168.1.100:5000
```

---

## 📞 Support & Resources

### Official Documentation
- **Flask**: https://flask.palletsprojects.com/
- **Scikit-learn**: https://scikit-learn.org/
- **Python macOS**: https://www.python.org/downloads/macos/

### Community
- Stack Overflow (tag: python, flask, macos)
- Python Discord Server
- macOS Developer Forums

---

## ✅ Checklist Setup

- [ ] Python 3.11+ terinstall
- [ ] Homebrew terinstall (opsional)
- [ ] Virtual environment dibuat
- [ ] Dependencies terinstall
- [ ] Model files tersedia
- [ ] Aplikasi berjalan tanpa error
- [ ] Browser bisa akses localhost:5000
- [ ] Dapat melakukan prediksi

---

## 📝 Catatan Penting

1. **Selalu gunakan virtual environment** untuk menghindari konflik dependencies
2. **Jangan commit virtual environment** ke git (sudah ada di .gitignore)
3. **Backup model files** secara berkala
4. **Update dependencies** secara teratur untuk security patches
5. **Gunakan Python 3.11+** untuk kompatibilitas optimal dengan scikit-learn 1.7.2

---

**Dibuat**: 31 Desember 2025  
**Untuk**: macOS 10.14+  
**Python**: 3.11+  
**Flask**: 2.3.0+

---

**🎉 Selamat! Aplikasi Prediksi Kredit Macet siap digunakan di macOS!**
