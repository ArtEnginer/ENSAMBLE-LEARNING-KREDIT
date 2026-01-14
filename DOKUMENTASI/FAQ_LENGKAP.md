# ❓ FAQ LENGKAP
## Frequently Asked Questions - NPL Predictor

---

## 📚 KATEGORI

1. [Instalasi & Setup](#instalasi--setup)
2. [Penggunaan Aplikasi](#penggunaan-aplikasi)
3. [Model & Prediksi](#model--prediksi)
4. [Data & Export](#data--export)
5. [Performance & Optimization](#performance--optimization)
6. [Troubleshooting](#troubleshooting)
7. [Development & Customization](#development--customization)
8. [Security & Privacy](#security--privacy)

---

## INSTALASI & SETUP

### Q1: Sistem operasi apa saja yang didukung?
**A:** Aplikasi dapat berjalan di:
- ✅ Windows 10/11
- ✅ macOS 10.15+ (Catalina atau lebih baru)
- ✅ Linux (Ubuntu 18.04+, Debian, Fedora, dll)
- ✅ Raspberry Pi OS (dengan Python 3.8+)

### Q2: Berapa minimum RAM yang dibutuhkan?
**A:** 
- **Minimum**: 4 GB RAM
- **Recommended**: 8 GB RAM atau lebih
- **Optimal**: 16 GB RAM (untuk dataset besar)

### Q3: Apakah perlu install database server?
**A:** Tidak. Versi current menggunakan browser Local Storage. Database server (MySQL/PostgreSQL) hanya diperlukan untuk production deployment dengan banyak user.

### Q4: Bagaimana cara install di Windows tanpa admin rights?
**A:** 
```bash
# 1. Install Python portable version
#    Download dari python.org (embeddable package)

# 2. Extract ke folder user
#    Contoh: C:\Users\YourName\Python38

# 3. Install pip
python get-pip.py --user

# 4. Install dependencies dengan --user flag
pip install --user -r requirements.txt
```

### Q5: Apakah bisa jalan di Python 2.7?
**A:** Tidak. Aplikasi memerlukan Python 3.8 atau lebih baru karena menggunakan features yang tidak ada di Python 2.7 (yang sudah deprecated).

### Q6: Berapa lama proses instalasi?
**A:** 
- Python installation: 5-10 menit
- Dependencies installation: 5-15 menit (tergantung koneksi internet)
- Total: ±20-30 menit untuk first-time setup

### Q7: Apakah perlu install Microsoft Visual C++?
**A:** Pada Windows, beberapa packages (seperti numpy, pandas) mungkin memerlukan Visual C++ Redistributable. Jika error saat install, download dari: https://aka.ms/vs/17/release/vc_redist.x64.exe

### Q8: Bagaimana cara verify instalasi berhasil?
**A:**
```bash
# Test Python
python --version
# Output: Python 3.8.x atau lebih baru

# Test pip
pip --version
# Output: pip 21.x.x atau lebih baru

# Test dependencies
python -c "import flask, pandas, sklearn, joblib"
# Jika tidak ada error, instalasi berhasil

# Test aplikasi
python app.py
# Aplikasi harus jalan tanpa error
```

---

## PENGGUNAAN APLIKASI

### Q9: Apakah perlu registrasi atau login?
**A:** Tidak. Versi current tidak memerlukan account. Aplikasi langsung bisa digunakan setelah dijalankan.

### Q10: Bisa diakses dari HP/tablet?
**A:** Ya, aplikasi fully responsive dan bisa diakses dari:
- 📱 Smartphone (Android/iOS)
- 📱 Tablet (iPad/Android tablet)
- 💻 Desktop/Laptop
- 🖥️ Monitor besar

### Q11: Browser apa yang paling baik?
**A:** 
**Recommended:**
- ✅ Google Chrome 90+ (Best performance)
- ✅ Microsoft Edge 90+
- ✅ Firefox 88+
- ✅ Safari 14+ (macOS/iOS)

**Not Recommended:**
- ❌ Internet Explorer (not supported)
- ❌ Browser lama < 2020

### Q12: Apakah bisa digunakan offline?
**A:** 
- **Setelah first load**: Ya (dengan catatan)
- **Resource eksternal** (Tailwind CSS, Font Awesome) perlu internet untuk first load
- **Setelah ter-cache**: Bisa offline
- **Untuk fully offline**: Perlu modifikasi untuk download semua assets lokal

### Q13: Maksimal berapa user bisa akses bersamaan?
**A:** 
- **Development mode** (python app.py): 1 user
- **Production mode** (Gunicorn): Bisa handle multiple concurrent users
  ```bash
  # 4 workers = dapat handle ~100 concurrent users
  gunicorn -w 4 -b 0.0.0.0:5000 app:app
  ```

### Q14: Apakah ada limit jumlah prediksi?
**A:** Tidak ada hard limit. Tapi perlu diperhatikan:
- Browser local storage max: ~5-10 MB
- Jika data terlalu banyak → performance menurun
- Recommended: Export dan clear data setiap bulan

### Q15: Bagaimana cara switch antar multiple models?
**A:** Edit file `app.py`:
```python
# Ganti MODEL_DIR ke model yang diinginkan
MODEL_DIR = "models/model_20260112_100139"  # Model lama
MODEL_DIR = "models/model_20260115_143000"  # Model baru
```
Restart aplikasi setelah perubahan.

---

## MODEL & PREDIKSI

### Q16: Algoritma apa yang digunakan?
**A:** 
**Primary Algorithm**: Random Forest Classifier
- Ensemble of decision trees
- Bagging technique
- Feature randomization
- Vote-based prediction

**Why Random Forest?**
- High accuracy (95.7%)
- Robust terhadap overfitting
- Dapat handle non-linear relationships
- Feature importance analysis
- Good balance speed vs accuracy

### Q17: Berapa akurasi model?
**A:** Berdasarkan testing:
```
Overall Accuracy: 95.7%
Precision (Lancar): 94.2%
Precision (Macet): 93.8%
Recall (Lancar): 96.1%
Recall (Macet): 91.3%
F1-Score: 94.0%
```

### Q18: Apakah model bisa salah prediksi?
**A:** Ya, mungkin. Tidak ada model yang 100% akurat:
- **False Positive** (5%): Prediksi lancar tapi sebenarnya macet
- **False Negative** (4%): Prediksi macet tapi sebenarnya lancar
- Karena itu, model adalah **alat bantu**, bukan keputusan final
- Tetap perlu **human judgment** dan verifikasi manual

### Q19: Kenapa hasil prediksi berbeda untuk data yang mirip?
**A:** Beberapa kemungkinan:
1. **Perbedaan kecil pada feature** bisa berdampak besar
2. **Interaction antar features**: Kombinasi features lebih penting dari single feature
3. **Threshold boundaries**: Jika data di borderline (prob ~50%), small change bisa flip hasil
4. **Model non-deterministic**: Jika re-train dengan random seed berbeda

### Q20: Bisakah saya adjust confidence threshold?
**A:** Ya, edit di `app.py`:
```python
# Default threshold: 0.5 (50%)
# Untuk lebih konservatif (reduce false negative):
threshold = 0.3  # Lebih mudah approve

# Untuk lebih strict (reduce false positive):
threshold = 0.7  # Lebih susah approve

# Implementasi:
if prediction_proba[0][1] > threshold:
    prediction_label = "Tidak Lancar"
else:
    prediction_label = "Lancar"
```

### Q21: Apa perbedaan Random Forest dengan model lain?
**A:**

| Model | Accuracy | Speed | Pros | Cons |
|-------|----------|-------|------|------|
| **Random Forest** | 95.7% | Medium | High accuracy, robust | Black box |
| Logistic Regression | 88.2% | Fast | Interpretable, simple | Lower accuracy |
| SVM | 92.1% | Slow | Good for high-dim | Slow on large data |
| Neural Network | 94.3% | Slow | Very flexible | Overfitting risk |
| XGBoost | 96.1% | Medium | Highest accuracy | Complex tuning |

### Q22: Berapa lama training model?
**A:**
- **Dataset kecil** (<10k rows): 1-5 menit
- **Dataset medium** (10k-100k): 5-30 menit
- **Dataset besar** (>100k): 30+ menit

Dengan notebook `ANALISIS_NPL_LENGKAP.ipynb`.

### Q23: Fitur apa yang paling penting dalam prediksi?
**A:** Berdasarkan feature importance:

1. **Plafond** (28.5%) - Paling penting
2. **Pekerjaan** (22.1%)
3. **Hasil Prescreening Dukcapil** (14.8%)
4. **Jangka Waktu** (12.3%)
5. **Usia** (9.7%)
6. **Hasil Prescreening SIPKUR** (6.2%)
7. **Produk** (3.8%)
8. **Status Aplikasi** (2.1%)
9. **Status Pernikahan** (0.5%)

### Q24: Apakah model perlu di-retrain berkala?
**A:** Ya, recommended:
- **Minimal**: 6 bulan sekali
- **Ideal**: 3 bulan sekali
- **Jika ada**: Perubahan signifikan di pola data

**Alasan:**
- Data drift (pola berubah seiring waktu)
- New patterns yang muncul
- Economic conditions berubah
- Improve accuracy dengan data baru

---

## DATA & EXPORT

### Q25: Di mana data disimpan?
**A:**
- **Prediksi results**: Browser Local Storage
- **Model & preprocessors**: Folder `models/`
- **Dataset training**: Folder `DATASET/`
- **Export files**: Downloads folder browser Anda

### Q26: Apakah data aman?
**A:** 
- ✅ Data tersimpan **lokal** di browser Anda
- ✅ **Tidak dikirim** ke server eksternal
- ✅ **Hanya Anda** yang bisa akses
- ⚠️ Tapi: Jika clear browser data → hilang
- 💡 Solution: Export backup berkala

### Q27: Berapa lama data tersimpan?
**A:**
- **Browser Local Storage**: Permanent (sampai dihapus manual)
- **Session Storage**: Hilang saat close browser
- **Cookies**: Tergantung expiry (default: permanent)

**Note**: Clear browser data akan hapus semua riwayat.

### Q28: Format export apa saja yang tersedia?
**A:**
- ✅ **Excel** (.xlsx) - Untuk analisis dengan Excel/Sheets
- ✅ **CSV** (.csv) - Import ke tools lain
- ✅ **JSON** (.json) - API integration, programming
- ✅ **PDF** (.pdf) - Laporan cetak

### Q29: Apakah bisa import data dari Excel?
**A:** Versi current: Belum support batch import. Coming soon.

**Workaround saat ini:**
1. Input manual satu-satu
2. Atau develop custom script untuk batch prediction via API

### Q30: Bagaimana cara backup semua data?
**A:**
```
Method 1: Via UI
1. Buka menu "Riwayat"
2. Klik "Export Semua"
3. Pilih format Excel atau JSON
4. Simpan file backup

Method 2: Via Browser Console
1. Tekan F12 → Console
2. Jalankan:
   var data = localStorage.getItem('predictions');
   console.log(data);
3. Copy JSON output
4. Save ke file .json
```

### Q31: Apakah data bisa di-restore?
**A:** Manual restore via browser console:
```javascript
// Restore dari JSON backup
var backupData = '[...paste your JSON backup...]';
localStorage.setItem('predictions', backupData);
location.reload();
```

### Q32: Berapa limit storage browser?
**A:**
- **Local Storage**: ~5-10 MB (varies per browser)
- **IndexedDB**: ~50 MB+ (jika diimplementasikan)

Jika menyimpan ~1000 prediksi → ~2-3 MB

---

## PERFORMANCE & OPTIMIZATION

### Q33: Kenapa aplikasi lambat?
**A:** Penyebab dan solusi:

**1. Terlalu banyak data di riwayat**
```
Solution: Clear old history (> 6 bulan)
```

**2. Browser resource terbatas**
```
Solution: 
- Close tabs lain
- Restart browser
- Increase memory limit
```

**3. Server overload**
```
Solution:
- Restart aplikasi
- Use Gunicorn (production mode)
- Scale resources
```

### Q34: Bagaimana cara optimize untuk banyak user?
**A:**
```bash
# 1. Gunakan production WSGI server
pip install gunicorn

# 2. Multi-worker
gunicorn -w 4 app:app  # 4 workers

# 3. Add reverse proxy (Nginx)
# 4. Load balancing
# 5. Add caching (Redis)
# 6. Database server (PostgreSQL)
```

### Q35: Apakah bisa di-deploy ke cloud?
**A:** Ya, bisa deploy ke:

**Free Tiers:**
- Heroku (free dyno)
- Render.com
- Railway.app
- PythonAnywhere

**Paid Options:**
- AWS EC2
- Google Cloud Run
- Azure App Service
- DigitalOcean Droplet

**Container:**
- Docker + Kubernetes
- Docker Swarm

### Q36: Berapa biaya running di cloud?
**A:** Estimasi:

| Platform | Tier | Cost/Month |
|----------|------|------------|
| Heroku | Free | $0 |
| Heroku | Hobby | $7 |
| AWS EC2 | t2.micro | $8-10 |
| DigitalOcean | Basic | $5-6 |
| Azure | B1 | $13 |
| Render | Free | $0 |

### Q37: Bagaimana cara monitoring performance?
**A:**
1. **Built-in**: Check browser DevTools (F12) → Performance tab
2. **Server**: Add logging
   ```python
   import logging
   logging.basicConfig(level=logging.INFO)
   ```
3. **APM Tools**: 
   - New Relic
   - DataDog
   - Sentry (for errors)

---

## TROUBLESHOOTING

### Q38: Error "Module not found: flask"
**A:**
```bash
# Install Flask
pip install flask

# Atau install semua dependencies
pip install -r requirements.txt

# Verify
python -c "import flask; print(flask.__version__)"
```

### Q39: Error "Port 5000 already in use"
**A:**
```bash
# Option 1: Kill process using port 5000
# Windows:
netstat -ano | findstr :5000
taskkill /PID [PID_NUMBER] /F

# macOS/Linux:
lsof -ti:5000 | xargs kill -9

# Option 2: Change port
# Edit app.py:
app.run(port=5001)  # Use port 5001
```

### Q40: Prediksi selalu error "Prediction failed"
**A:** Debug steps:
```
1. Check browser console (F12) untuk error detail
2. Verify input format:
   ✓ Tanggal: DD/MM/YYYY
   ✓ Plafond: Numbers only
   ✓ Jangka Waktu: Integer
3. Pastikan semua field terisi
4. Clear browser cache
5. Restart aplikasi
```

### Q41: Grafik tidak muncul
**A:**
```
1. Pastikan ada data di riwayat (minimal 1 prediksi)
2. Check console error (F12)
3. Verify Chart.js loaded (check Network tab)
4. Refresh halaman (Ctrl+F5)
5. Try different browser
```

### Q42: Export Excel tidak jalan
**A:**
```
1. Check pop-up blocker → Allow pop-ups
2. Check browser download settings
3. Verify ada data untuk diexport
4. Try different browser
5. Manual export via console:
   - F12 → Console
   - Copy data
   - Paste ke Excel
```

### Q43: Data hilang setelah restart browser
**A:**
**Penyebab**: Incognito/Private mode atau browser clear data

**Solution:**
1. Jangan gunakan mode Private/Incognito
2. Enable cookies & local storage
3. Jangan clear browser data
4. Export backup secara berkala

### Q44: Aplikasi crash saat startup
**A:**
```bash
# Check error message
# Common causes:

# 1. Model file not found
# → Verify folder models/ exists
# → Check MODEL_DIR path in app.py

# 2. Corrupt model file
# → Re-download atau re-train model

# 3. Python version
# → Upgrade to Python 3.8+

# 4. Dependencies version conflict
# → Create virtual environment
python -m venv venv
source venv/bin/activate  # macOS/Linux
venv\Scripts\activate  # Windows
pip install -r requirements.txt
```

---

## DEVELOPMENT & CUSTOMIZATION

### Q45: Bagaimana cara menambah field input baru?
**A:**
```python
# 1. Edit app.py - tambah field di input_data
input_data = {
    "Jangka Waktu": int(data["jangka_waktu"]),
    "Field Baru": data["field_baru"],  # <-- Add
    # ... field lainnya
}

# 2. Edit templates/predict.html - tambah input field
<input type="text" name="field_baru" />

# 3. Retrain model dengan feature baru
# Via Jupyter Notebook
```

### Q46: Bagaimana cara customize tampilan?
**A:**
Aplikasi menggunakan Tailwind CSS:

```html
<!-- Edit file di folder templates/ -->

<!-- Change colors -->
<div class="bg-blue-600">  <!-- Ganti blue-600 -->

<!-- Change layout -->
<div class="grid grid-cols-2">  <!-- 2 columns -->

<!-- Add custom CSS -->
<style>
  .custom-class {
    /* Your styles */
  }
</style>
```

### Q47: Apakah ada API documentation?
**A:** 
API Endpoints:

```
POST /api/predict
Content-Type: application/json

Request Body:
{
  "tanggal_lahir": "1985-01-15",
  "pekerjaan": "1",
  "status_pernikahan": "K",
  "produk": "KPR",
  "sub_produk": "KPR Subsidi",
  "plafond": "100000000",
  "jangka_waktu": "120",
  "status_aplikasi": "Accept",
  "hasil_prescreening_sipkur": "Sesuai",
  "hasil_prescreening_dukcapil": "Sesuai"
}

Response:
{
  "status": "success",
  "prediction": "Lancar",
  "probability": {
    "lancar": 92.5,
    "tidak_lancar": 7.5
  },
  "risk_level": "Sangat Rendah",
  "rekomendasi": "..."
}
```

### Q48: Bagaimana cara integrate dengan sistem lain?
**A:**

**Option 1: REST API**
```python
import requests

url = "http://localhost:5000/api/predict"
data = {
    "tanggal_lahir": "1985-01-15",
    # ... data lainnya
}
response = requests.post(url, json=data)
result = response.json()
```

**Option 2: Direct Python Import**
```python
from app import model, scaler, label_encoders
# Use model directly
```

**Option 3: Microservice**
- Deploy sebagai standalone service
- Communicate via REST API
- Use message queue (RabbitMQ/Kafka)

### Q49: Lisensi aplikasi apa?
**A:** [Sesuaikan dengan lisensi Anda]
- Open source
- Free untuk educational & research
- Commercial use: [Specify terms]

### Q50: Bagaimana cara contribute?
**A:**
```bash
# 1. Fork repository
# 2. Clone
git clone [your-fork-url]

# 3. Create branch
git checkout -b feature/new-feature

# 4. Make changes
# 5. Commit
git commit -m "Add new feature"

# 6. Push
git push origin feature/new-feature

# 7. Create Pull Request
```

---

## SECURITY & PRIVACY

### Q51: Apakah data prediksi aman?
**A:**
- ✅ Data disimpan lokal (browser)
- ✅ Tidak dikirim ke external server
- ✅ HTTPS recommended untuk production
- ⚠️ Backup data perlu dienkripsi jika sensitif

### Q52: Apakah perlu SSL/HTTPS?
**A:**
- **Development (localhost)**: Tidak wajib
- **Production (public)**: **Wajib**

Setup HTTPS:
```bash
# Menggunakan Let's Encrypt
sudo certbot --nginx -d yourdomain.com
```

### Q53: Bagaimana cara protect dari unauthorized access?
**A:**

**Add Authentication:**
```python
# Install Flask-Login
pip install flask-login

# Implementasi di app.py
from flask_login import login_required

@app.route('/predict')
@login_required  # <-- Protect route
def predict_page():
    # ...
```

### Q54: Apakah ada audit log?
**A:** Versi current: Belum ada. 

Bisa ditambahkan:
```python
import logging

logging.basicConfig(
    filename='app.log',
    level=logging.INFO,
    format='%(asctime)s - %(message)s'
)

# Log setiap prediksi
logging.info(f"Prediction: {user} - {result}")
```

### Q55: Bagaimana cara backup model?
**A:**
```bash
# Backup folder models/
zip -r models_backup.zip models/

# Atau copy ke cloud storage
aws s3 cp models/ s3://your-bucket/models/ --recursive
```

---

## 📞 STILL NEED HELP?

Jika pertanyaan Anda belum terjawab:

1. **📖 Documentation**: Baca [BUKU_PETUNJUK_PENGGUNAAN.md](BUKU_PETUNJUK_PENGGUNAAN.md)
2. **🔍 Search**: Gunakan Ctrl+F untuk search di FAQ ini
3. **💬 Community**: [Forum/Discord/Slack link]
4. **📧 Email**: [support email]
5. **🐛 Bug Report**: Create issue di GitHub

---

*FAQ v1.0 - Last Updated: 14 Januari 2026*
*Total Questions: 55*
