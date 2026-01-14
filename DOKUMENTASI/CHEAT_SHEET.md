# 📋 CHEAT SHEET
## NPL Predictor - Quick Reference

---

## 🎯 MENU NAVIGASI

| Menu | URL | Fungsi |
|------|-----|--------|
| 🏠 Dashboard | `/` | Overview & statistik |
| 📊 Prediksi | `/predict` | Form input prediksi |
| 📜 Riwayat | `/history` | Semua prediksi |
| 📈 Analitik | `/analytics` | Grafik & chart |
| ℹ️ Tentang | `/about` | Info model |
| ⚙️ Settings | `/settings` | Pengaturan |
| ❓ Help | `/help` | Bantuan |

---

## 📝 INPUT FIELDS

### Step 1: Data Pribadi
| Field | Type | Contoh | Keterangan |
|-------|------|--------|------------|
| Tanggal Lahir | Date | 15/01/1985 | Format: DD/MM/YYYY |
| Pekerjaan | Dropdown | PNS | 31 pilihan |
| Status Nikah | Radio | K/B/C | K=Kawin, B=Belum, C=Cerai |

### Step 2: Info Kredit
| Field | Type | Contoh | Keterangan |
|-------|------|--------|------------|
| Produk | Dropdown | KPR | Jenis kredit |
| Sub Produk | Dropdown | KPR Subsidi | Sub kategori |
| Plafond | Number | 100000000 | Tanpa Rp/titik/koma |
| Jangka Waktu | Number | 120 | Dalam bulan |

### Step 3: Prescreening
| Field | Type | Opsi | Keterangan |
|-------|------|------|------------|
| Status Aplikasi | Dropdown | Accept/Reject/Waiting/Review | Status saat ini |
| SIPKUR | Dropdown | Sesuai/Tidak/- | Hasil checking |
| Dukcapil | Dropdown | Sesuai/Tidak/- | Hasil verifikasi |

---

## 🎨 KODE WARNA RISIKO

| Kode | Level | Range | Warna | Rekomendasi |
|------|-------|-------|-------|-------------|
| 🟢 | Sangat Rendah | 0-20% | Green | Approve |
| 🔵 | Rendah | 20-40% | Blue | Approve |
| 🟡 | Sedang | 40-60% | Yellow | Review |
| 🟠 | Tinggi | 60-80% | Orange | Careful |
| 🔴 | Sangat Tinggi | 80-100% | Red | Reject |

---

## 💼 KATEGORI PEKERJAAN

### Low Risk ✅
- 1: PNS
- 18: TNI/Polisi
- 9: Guru/Dosen
- 37: Pegawai Pemerintah

### Medium Risk ⚠️
- 26: Karyawan Swasta
- 10: Dokter/Perawat
- 11: Pengacara/Notaris
- 19: Pengusaha

### High Risk ❌
- 27: Freelancer
- 28: Ibu Rumah Tangga
- 30: Mahasiswa
- 31: Belum Bekerja

---

## 📊 FORMULA & RUMUS

### Perhitungan Usia
```
Usia = Tahun Sekarang - Tahun Lahir
(Dikurangi 1 jika belum ulang tahun)
```

### DTI (Debt to Income) Ratio
```
DTI = (Cicilan Bulanan / Penghasilan) × 100%
Ideal: < 30%
Max: 40%
```

### Cicilan Bulanan Estimasi
```
Cicilan ≈ Plafond / Jangka Waktu
(Simplified, tanpa bunga)

Contoh:
Plafond: Rp 100.000.000
Jangka: 120 bulan
Cicilan: ±Rp 833.333/bulan
```

### Range Usia Ideal
```
Minimum: 21 tahun
Ideal: 25-50 tahun
Maximum: 60 tahun (saat lunas)
```

---

## 🔑 FITUR IMPORTANCE

Urutan pengaruh terhadap prediksi:

1. **Plafond** ⭐⭐⭐⭐⭐ (Paling penting)
2. **Pekerjaan** ⭐⭐⭐⭐⭐
3. **Hasil Prescreening** ⭐⭐⭐⭐
4. **Jangka Waktu** ⭐⭐⭐⭐
5. **Usia** ⭐⭐⭐
6. **Produk** ⭐⭐⭐
7. **Status Aplikasi** ⭐⭐⭐
8. **Status Nikah** ⭐⭐
9. **Sub Produk** ⭐⭐

---

## 🎯 DECISION MATRIX

| Prob. Macet | Action | Syarat |
|-------------|--------|--------|
| 0-20% | ✅ Approve | Standard |
| 20-40% | ✅ Approve | Standard |
| 40-60% | ⚠️ Review | Verifikasi extra |
| 60-80% | ⚠️ Careful | Agunan lebih/Co-applicant |
| 80-100% | ❌ Reject | Tidak recommended |

---

## 🔧 COMMAND LINE

### Menjalankan Aplikasi
```bash
# Standard
python app.py

# Custom port
python app.py --port 5001

# Production (Gunicorn)
gunicorn -w 4 -b 0.0.0.0:5000 app:app
```

### Debugging
```bash
# Check Python
python --version

# Check dependencies
pip list

# Install dependencies
pip install -r requirements.txt

# Update pip
python -m pip install --upgrade pip
```

### Port Management
```bash
# Windows - Check port
netstat -ano | findstr :5000

# Kill process (Windows)
taskkill /PID [PID] /F

# macOS/Linux - Check port
lsof -i :5000

# Kill process (macOS/Linux)
kill -9 [PID]
```

---

## 📥 EXPORT FORMATS

| Format | Use Case | Command |
|--------|----------|---------|
| Excel | Analisis data | Export → Excel |
| CSV | Import ke tools lain | Export → CSV |
| JSON | API integration | Export → JSON |
| PDF | Laporan cetak | Download PDF |

---

## 🌐 API ENDPOINTS

### GET Endpoints
```
GET /                    → Dashboard
GET /predict            → Form prediksi
GET /history            → Riwayat
GET /analytics          → Analitik
GET /api/model-info     → Info model (JSON)
```

### POST Endpoints
```
POST /api/predict       → Prediksi (JSON)
```

### Request Example (JSON)
```json
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
```

### Response Example (JSON)
```json
{
  "status": "success",
  "prediction": "Lancar",
  "probability": {
    "lancar": 92.5,
    "tidak_lancar": 7.5
  },
  "risk_level": "Sangat Rendah",
  "risk_color": "green",
  "rekomendasi": "Pemohon layak mendapat kredit"
}
```

---

## ⌨️ KEYBOARD SHORTCUTS

| Key | Action |
|-----|--------|
| `Ctrl + N` | New prediction |
| `Ctrl + S` | Save result |
| `Ctrl + E` | Export |
| `Ctrl + H` | Go to History |
| `Ctrl + D` | Go to Dashboard |
| `F5` | Refresh |
| `Esc` | Close modal |
| `Tab` | Next field |
| `Shift + Tab` | Previous field |

---

## 🐛 COMMON ERRORS

| Error | Cause | Solution |
|-------|-------|----------|
| Module not found | Dependencies tidak installed | `pip install -r requirements.txt` |
| Port in use | Port 5000 sudah dipakai | Ganti port atau kill process |
| Prediction failed | Input tidak valid | Check format semua field |
| Chart empty | Tidak ada data | Lakukan prediksi dulu |
| Export error | Pop-up blocked | Allow pop-up di browser |
| Data hilang | Incognito mode | Jangan gunakan private mode |

---

## 📈 MODEL METRICS

```
Model: Random Forest Classifier
Accuracy: ~95.7%
Precision: ~94.2%
Recall: ~93.8%
F1-Score: ~94.0%

Features: 10
Training Data: [Check metadata]
Model Version: model_20260112_100139
```

---

## 🔐 SECURITY BEST PRACTICES

✅ **DO**
- Logout setelah selesai
- Export data berkala
- Backup riwayat
- Clear old data
- Strong password (jika ada auth)

❌ **DON'T**
- Share kredensial
- Screenshot data sensitif
- Leave session open
- Store password in browser
- Use public computer tanpa logout

---

## 📞 QUICK HELP

| Issue | Solution |
|-------|----------|
| Lupa password | Reset via email/admin |
| App tidak jalan | Check Python & dependencies |
| Hasil aneh | Verify input data |
| Performance lambat | Clear old history |
| Export gagal | Check browser settings |

**Full Documentation**: [BUKU_PETUNJUK_PENGGUNAAN.md](BUKU_PETUNJUK_PENGGUNAAN.md)

---

*Cheat Sheet v1.0 - Updated: 14 Jan 2026*
