# 🚀 QUICK START GUIDE
## Sistem Prediksi Kredit NPL

*Panduan cepat untuk mulai menggunakan aplikasi dalam 5 menit*

---

## 📥 INSTALASI CEPAT

### 1. Install Python
```bash
# Cek Python sudah terinstall
python --version

# Jika belum, download dari python.org
```

### 2. Install Dependencies
```bash
cd ENSAMBLE-LEARNING-KREDIT
pip install -r requirements.txt
```

### 3. Jalankan Aplikasi
```bash
python app.py
```

### 4. Buka Browser
```
http://localhost:5000
```

---

## ⚡ QUICK ACTIONS

### Melakukan Prediksi (2 Menit)

1. **Klik "Prediksi"** di menu
2. **Isi 3 Step Form:**
   - Step 1: Tanggal Lahir, Pekerjaan, Status Nikah
   - Step 2: Produk, Plafond, Jangka Waktu
   - Step 3: Prescreening
3. **Klik "Prediksi Sekarang"**
4. **Lihat Hasil** → Simpan atau Export

### Melihat Dashboard
- Klik **"Dashboard"** untuk statistik keseluruhan
- Lihat total prediksi, grafik tren, dan recent activity

### Melihat Riwayat
- Klik **"Riwayat"** untuk semua prediksi
- Export ke Excel: Klik **"Export Semua"**

### Analitik & Grafik
- Klik **"Analitik"** untuk visualisasi mendalam
- 4 grafik: Tren, Risiko, Pekerjaan, Plafond

---

## 📊 INTERPRETASI HASIL

### Status Prediksi
- ✅ **LANCAR**: Kredit diprediksi lancar
- ❌ **MACET**: Berisiko tinggi macet

### Tingkat Risiko
| Warna | Level | Probabilitas Macet | Rekomendasi |
|-------|-------|-------------------|-------------|
| 🟢 | Sangat Rendah | < 20% | Approve |
| 🔵 | Rendah | 20-40% | Approve |
| 🟡 | Sedang | 40-60% | Review Manual |
| 🟠 | Tinggi | 60-80% | Extra Check |
| 🔴 | Sangat Tinggi | > 80% | Reject |

---

## ⚙️ CONTOH PENGISIAN

### Contoh 1: KPR PNS (Low Risk)
```
Step 1:
- Tanggal Lahir: 15/01/1985 (Usia 41)
- Pekerjaan: PNS
- Status Nikah: Kawin

Step 2:
- Produk: KPR
- Sub Produk: KPR Subsidi
- Plafond: 100000000 (100 juta)
- Jangka Waktu: 120 (10 tahun)

Step 3:
- Status Aplikasi: Accept
- SIPKUR: Sesuai
- Dukcapil: Sesuai

Hasil: ✅ LANCAR (Risiko: Sangat Rendah)
```

### Contoh 2: KTA Freelancer (High Risk)
```
Step 1:
- Tanggal Lahir: 10/06/1995 (Usia 30)
- Pekerjaan: Freelancer
- Status Nikah: Belum Kawin

Step 2:
- Produk: KTA
- Sub Produk: KTA Regular
- Plafond: 150000000 (150 juta)
- Jangka Waktu: 60 (5 tahun)

Step 3:
- Status Aplikasi: Under Review
- SIPKUR: Sesuai
- Dukcapil: Sesuai

Hasil: ❌ MACET (Risiko: Tinggi)
```

---

## 🔥 TIPS CEPAT

### DO ✅
- ✅ Isi semua field dengan benar
- ✅ Double-check tanggal lahir
- ✅ Plafond: angka saja (tanpa Rp atau titik)
- ✅ Simpan hasil penting ke riwayat
- ✅ Export data secara berkala

### DON'T ❌
- ❌ Jangan skip field
- ❌ Jangan input data dummy
- ❌ Jangan gunakan mode Incognito (data hilang)
- ❌ Jangan abaikan warning/error

---

## 🆘 TROUBLESHOOTING CEPAT

### Aplikasi tidak jalan
```bash
# Check Python
python --version

# Install ulang dependencies
pip install -r requirements.txt

# Ganti port jika 5000 bentrok
# Edit app.py: app.run(port=5001)
```

### Prediksi error
1. Pastikan semua field terisi
2. Format tanggal: DD/MM/YYYY
3. Plafond: angka saja
4. Refresh halaman (F5)

### Grafik kosong
- Pastikan ada data di riwayat
- Lakukan minimal 1 prediksi dulu

### Data hilang
- Jangan gunakan mode Private/Incognito
- Enable cookies & local storage
- Export backup secara rutin

---

## 📱 KEYBOARD SHORTCUTS

| Shortcut | Aksi |
|----------|------|
| `Ctrl + S` | Save/Simpan prediksi |
| `Ctrl + E` | Export data |
| `Ctrl + N` | New prediction |
| `F5` | Refresh halaman |
| `Esc` | Close modal |

---

## 📞 BANTUAN

**Dokumentasi Lengkap**: [BUKU_PETUNJUK_PENGGUNAAN.md](BUKU_PETUNJUK_PENGGUNAAN.md)

**Quick Links**:
- 🏠 Dashboard: http://localhost:5000
- 📊 Prediksi: http://localhost:5000/predict
- 📜 Riwayat: http://localhost:5000/history
- 📈 Analitik: http://localhost:5000/analytics

---

**🎯 SELAMAT MENGGUNAKAN!**

*Last Updated: 14 Januari 2026*
