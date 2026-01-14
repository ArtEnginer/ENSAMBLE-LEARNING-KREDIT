# 📘 BUKU PETUNJUK PENGGUNAAN APLIKASI
## SISTEM PREDIKSI KREDIT NPL (Non-Performing Loan)

---

## 📑 DAFTAR ISI

1. [Pendahuluan](#1-pendahuluan)
2. [Instalasi dan Persiapan](#2-instalasi-dan-persiapan)
3. [Menjalankan Aplikasi](#3-menjalankan-aplikasi)
4. [Antarmuka Aplikasi](#4-antarmuka-aplikasi)
5. [Panduan Penggunaan Fitur](#5-panduan-penggunaan-fitur)
6. [Tutorial Step-by-Step](#6-tutorial-step-by-step)
7. [Interpretasi Hasil](#7-interpretasi-hasil)
8. [Tips dan Best Practice](#8-tips-dan-best-practice)
9. [Troubleshooting](#9-troubleshooting)
10. [FAQ (Pertanyaan yang Sering Diajukan)](#10-faq-pertanyaan-yang-sering-diajukan)

---

## 1. PENDAHULUAN

### 1.1 Tentang Aplikasi

**NPL Predictor** adalah aplikasi berbasis web untuk memprediksi risiko kredit macet (Non-Performing Loan) menggunakan teknologi Machine Learning. Aplikasi ini membantu lembaga keuangan dalam menilai kelayakan kredit calon peminjam secara otomatis dan objektif.

### 1.2 Tujuan Aplikasi

- **Mempercepat proses analisis kredit** dari yang manual menjadi otomatis
- **Meningkatkan akurasi** dalam penilaian risiko kredit
- **Mengurangi risiko** kredit macet dengan prediksi berbasis data
- **Memberikan rekomendasi** yang objektif dan terukur
- **Dokumentasi riwayat** prediksi untuk evaluasi

### 1.3 Fitur Utama

✅ **Prediksi Otomatis** - Analisis kelayakan kredit dengan AI  
✅ **Dashboard Interaktif** - Visualisasi data real-time  
✅ **Riwayat Prediksi** - Tracking semua prediksi yang dilakukan  
✅ **Analitik Mendalam** - Statistik dan grafik komprehensif  
✅ **Export Data** - Download hasil dalam format Excel/CSV  
✅ **Responsive Design** - Dapat diakses dari desktop, tablet, dan mobile  

### 1.4 Teknologi yang Digunakan

- **Backend**: Flask (Python)
- **Machine Learning**: Random Forest Classifier
- **Frontend**: HTML5, Tailwind CSS, JavaScript
- **Data Storage**: Local Storage (Browser)
- **Visualisasi**: Chart.js

---

## 2. INSTALASI DAN PERSIAPAN

### 2.1 Persyaratan Sistem

#### Minimum System Requirements:
- **Operating System**: Windows 10/11, macOS 10.15+, atau Linux
- **RAM**: 4 GB (Rekomendasi: 8 GB)
- **Storage**: 500 MB ruang kosong
- **Browser**: Chrome 90+, Firefox 88+, Safari 14+, atau Edge 90+
- **Koneksi Internet**: Untuk download dependencies

#### Software Requirements:
- Python 3.8 atau lebih baru
- pip (Python package installer)
- Web browser modern

### 2.2 Instalasi Python

#### Windows:
1. Download Python dari https://www.python.org/downloads/
2. Jalankan installer
3. ✅ **PENTING**: Centang "Add Python to PATH"
4. Klik "Install Now"
5. Verifikasi instalasi:
   ```bash
   python --version
   pip --version
   ```

#### macOS:
```bash
# Menggunakan Homebrew
brew install python3

# Atau download dari python.org
```

#### Linux (Ubuntu/Debian):
```bash
sudo apt update
sudo apt install python3 python3-pip
```

### 2.3 Download Aplikasi

1. **Clone Repository** (jika menggunakan Git):
   ```bash
   git clone [URL_REPOSITORY]
   cd ENSAMBLE-LEARNING-KREDIT
   ```

2. **Atau Extract ZIP**:
   - Download file ZIP
   - Extract ke folder pilihan Anda
   - Buka folder hasil extract

### 2.4 Instalasi Dependencies

1. **Buka Terminal/Command Prompt** di folder aplikasi

2. **Install semua library yang diperlukan**:
   ```bash
   pip install -r requirements.txt
   ```

3. **Tunggu hingga instalasi selesai**

4. **Verifikasi instalasi**:
   ```bash
   pip list
   ```
   
   Pastikan library berikut terinstall:
   - Flask
   - pandas
   - scikit-learn
   - joblib
   - numpy

### 2.5 Struktur Folder

Pastikan struktur folder seperti berikut:

```
ENSAMBLE-LEARNING-KREDIT/
├── app.py                    # File utama aplikasi
├── requirements.txt          # Daftar dependencies
├── DATASET/                  # Folder data
│   ├── dataset_npl.csv      # Dataset utama
│   └── split_data/          # Data split untuk training
├── models/                   # Folder model ML
│   └── model_20260112_100139/
│       ├── best_model_random_forest.joblib
│       ├── label_encoders.joblib
│       ├── scaler.joblib
│       └── model_metadata.json
├── templates/               # HTML templates
│   ├── base.html
│   ├── dashboard.html
│   ├── predict.html
│   ├── history.html
│   ├── analytics.html
│   ├── about.html
│   ├── settings.html
│   └── help.html
└── DOKUMENTASI/            # Folder dokumentasi
    └── BUKU_PETUNJUK_PENGGUNAAN.md
```

### 2.6 Konfigurasi (Opsional)

Anda dapat mengubah konfigurasi di file `app.py`:

```python
# Port aplikasi (default: 5000)
app.run(debug=True, host="0.0.0.0", port=5000)

# Model yang digunakan
MODEL_DIR = "models/model_20260112_100139"
```

---

## 3. MENJALANKAN APLIKASI

### 3.1 Menjalankan Aplikasi

1. **Buka Terminal/Command Prompt**
2. **Navigasi ke folder aplikasi**:
   ```bash
   cd path/to/ENSAMBLE-LEARNING-KREDIT
   ```

3. **Jalankan aplikasi**:
   ```bash
   python app.py
   ```

4. **Tunggu hingga muncul pesan**:
   ```
   * Running on http://0.0.0.0:5000
   * Running on http://127.0.0.1:5000
   ```

5. **Buka browser** dan akses:
   ```
   http://localhost:5000
   ```
   atau
   ```
   http://127.0.0.1:5000
   ```

### 3.2 Menghentikan Aplikasi

- **Windows/Linux**: Tekan `Ctrl + C` di terminal
- **macOS**: Tekan `Cmd + C` atau `Ctrl + C`

### 3.3 Mengakses dari Perangkat Lain

Jika ingin mengakses dari perangkat lain di jaringan yang sama:

1. **Cari IP Address komputer server**:
   - Windows: `ipconfig`
   - macOS/Linux: `ifconfig` atau `ip addr`

2. **Akses dari browser perangkat lain**:
   ```
   http://[IP_ADDRESS]:5000
   ```
   Contoh: `http://192.168.1.100:5000`

### 3.4 Mode Production (Deployment)

Untuk deployment production, gunakan WSGI server seperti Gunicorn:

```bash
# Install Gunicorn
pip install gunicorn

# Jalankan dengan Gunicorn
gunicorn -w 4 -b 0.0.0.0:5000 app:app
```

---

## 4. ANTARMUKA APLIKASI

### 4.1 Navigasi Utama

Aplikasi memiliki menu navigasi di bagian atas:

```
┌──────────────────────────────────────────────────────────┐
│  🏠 Dashboard  │  📊 Prediksi  │  📜 Riwayat  │  📈 Analitik  │  ℹ️ Tentang  │  ⚙️ Settings  │  ❓ Help  │
└──────────────────────────────────────────────────────────┘
```

#### Icon dan Fungsi Menu:
- 🏠 **Dashboard**: Halaman utama dengan ringkasan
- 📊 **Prediksi**: Form input untuk prediksi kredit
- 📜 **Riwayat**: Daftar semua prediksi yang pernah dilakukan
- 📈 **Analitik**: Grafik dan statistik mendalam
- ℹ️ **Tentang**: Informasi tentang model dan akurasi
- ⚙️ **Settings**: Pengaturan aplikasi
- ❓ **Help**: Bantuan dan panduan

### 4.2 Dashboard

Dashboard menampilkan:

#### 📊 Quick Stats (Statistik Cepat)
```
┌───────────────┬───────────────┬───────────────┬───────────────┐
│ Total Prediksi│ Kredit Lancar │ Kredit Macet  │ Akurasi Model │
│      0        │      0 (0%)   │      0 (0%)   │    95.7%      │
└───────────────┴───────────────┴───────────────┴───────────────┘
```

#### 📈 Grafik Tren Prediksi
- Menampilkan tren prediksi per periode (7 hari, 30 hari, 90 hari)
- Perbandingan kredit lancar vs macet

#### 🥧 Distribusi Status Kredit
- Pie chart menampilkan proporsi kredit lancar dan macet

#### 📋 Prediksi Terbaru
- Tabel 5 prediksi terakhir
- Menampilkan: Nama, Status, Risiko, Tanggal, Aksi

### 4.3 Halaman Prediksi

Form prediksi dibagi dalam **3 langkah**:

#### Step 1: Data Pribadi
- Tanggal Lahir
- Pekerjaan (dropdown)
- Status Pernikahan

#### Step 2: Informasi Kredit
- Produk
- Sub Produk
- Plafond (jumlah pinjaman)
- Jangka Waktu (bulan)

#### Step 3: Prescreening
- Status Aplikasi
- Hasil Prescreening SIPKUR
- Hasil Prescreening Dukcapil

### 4.4 Halaman Riwayat

Menampilkan tabel lengkap semua prediksi:

| No | Tanggal | Nama | Pekerjaan | Plafond | Status | Risiko | Aksi |
|----|---------|------|-----------|---------|--------|--------|------|
| 1  | 14/01/2026 | John Doe | PNS | Rp 50.000.000 | Lancar | Rendah | 👁️ 📥 🗑️ |

**Fitur:**
- 🔍 Search/Filter
- 📊 Sort berdasarkan kolom
- 📥 Export ke Excel/CSV
- 👁️ View Detail
- 🗑️ Delete

### 4.5 Halaman Analitik

Visualisasi data mendalam:

1. **Tren Bulanan** (Line Chart)
2. **Distribusi Tingkat Risiko** (Radar Chart)
3. **Top 10 Pekerjaan** (Bar Chart)
4. **Distribusi Plafond** (Bar Chart)
5. **Tabel Statistik Detail**

---

## 5. PANDUAN PENGGUNAAN FITUR

### 5.1 Melakukan Prediksi Kredit

#### Langkah-langkah:

1. **Klik menu "Prediksi"** di navigasi atas

2. **Isi Form Step 1: Data Pribadi**

   **a. Tanggal Lahir**
   - Klik pada field tanggal
   - Pilih tanggal dari date picker
   - Atau ketik manual dengan format: DD/MM/YYYY
   - Contoh: 15/05/1985

   **b. Pekerjaan**
   - Klik dropdown "Pilih Pekerjaan"
   - Pilih dari 31 opsi yang tersedia:
     - PNS
     - Karyawan Swasta
     - Pengusaha
     - Pedagang
     - Dokter/Perawat
     - Guru/Dosen
     - Dan lainnya...
   
   **c. Status Pernikahan**
   - Pilih salah satu:
     - **K** = Kawin
     - **B** = Belum Kawin
     - **C** = Cerai

   **d. Klik tombol "Lanjut ke Informasi Kredit"**

3. **Isi Form Step 2: Informasi Kredit**

   **a. Produk**
   - Pilih jenis produk kredit:
     - KPR (Kredit Pemilikan Rumah)
     - KKB (Kredit Kendaraan Bermotor)
     - KTA (Kredit Tanpa Agunan)
     - Kredit Multiguna
     - Dan produk lainnya

   **b. Sub Produk**
   - Pilih sub kategori sesuai produk utama
   - Contoh untuk KPR:
     - KPR Subsidi
     - KPR Komersial
     - KPR Syariah

   **c. Plafond**
   - Masukkan jumlah pinjaman yang diajukan
   - Format: Angka tanpa titik/koma
   - Contoh: 50000000 (untuk Rp 50 juta)
   - Sistem akan otomatis format dengan pemisah ribuan

   **d. Jangka Waktu**
   - Masukkan durasi pinjaman dalam bulan
   - Contoh: 
     - 12 = 1 tahun
     - 24 = 2 tahun
     - 60 = 5 tahun
     - 120 = 10 tahun

   **e. Klik "Lanjut ke Prescreening"**

4. **Isi Form Step 3: Prescreening**

   **a. Status Aplikasi**
   - Accept = Diterima
   - Reject = Ditolak
   - Waiting Approval = Menunggu Persetujuan
   - Under Review = Sedang Ditinjau

   **b. Hasil Prescreening SIPKUR**
   - Sesuai = Data sesuai dengan SIPKUR
   - Tidak Sesuai = Ada ketidaksesuaian
   - \- (strip) = Belum dilakukan pengecekan

   **c. Hasil Prescreening Dukcapil**
   - Sesuai = Data sesuai dengan Dukcapil
   - Tidak Sesuai = Ada ketidaksesuaian
   - \- (strip) = Belum dilakukan pengecekan

   **d. Klik "Prediksi Sekarang"**

5. **Menunggu Hasil**
   - Loading spinner akan muncul
   - Proses prediksi ±1-2 detik
   - Hasil akan ditampilkan otomatis

6. **Membaca Hasil Prediksi**
   
   Hasil akan menampilkan:

   ```
   ╔═══════════════════════════════════════╗
   ║        HASIL PREDIKSI KREDIT          ║
   ╠═══════════════════════════════════════╣
   ║ Status Prediksi:  [LANCAR/MACET]     ║
   ║ Tingkat Risiko:   [Level]             ║
   ║ Probabilitas:                         ║
   ║   • Lancar:       XX.X%               ║
   ║   • Tidak Lancar: XX.X%               ║
   ║                                       ║
   ║ Rekomendasi:                          ║
   ║ [Teks rekomendasi dari sistem]        ║
   ╚═══════════════════════════════════════╝
   ```

   **Detail Hasil:**
   - ✅ **Status Prediksi**: Lancar atau Tidak Lancar (Macet)
   - 📊 **Probabilitas**: Persentase kemungkinan masing-masing status
   - ⚠️ **Tingkat Risiko**: 
     - Sangat Rendah (< 20%)
     - Rendah (20-40%)
     - Sedang (40-60%)
     - Tinggi (60-80%)
     - Sangat Tinggi (> 80%)
   - 💡 **Rekomendasi**: Saran sistem berdasarkan hasil

7. **Aksi Setelah Prediksi**
   - 📥 **Simpan**: Menyimpan hasil ke riwayat
   - 📄 **Download PDF**: Export hasil ke PDF
   - 🔄 **Prediksi Baru**: Reset form untuk prediksi baru
   - ↩️ **Kembali**: Kembali ke dashboard

### 5.2 Melihat Riwayat Prediksi

1. **Klik menu "Riwayat"**

2. **Menggunakan Fitur Filter/Search**
   ```
   [🔍 Cari berdasarkan nama atau pekerjaan...]
   ```
   - Ketik kata kunci
   - Filter otomatis real-time

3. **Sorting Data**
   - Klik pada header kolom untuk sort
   - Klik lagi untuk reverse sort
   - Kolom yang dapat disort:
     - Tanggal
     - Nama
     - Pekerjaan
     - Plafond
     - Status
     - Risiko

4. **Pagination**
   - Tampilan default: 10 entries per halaman
   - Bisa diubah: 10, 25, 50, 100
   - Navigasi: ◀️ Previous | Next ▶️

5. **Melihat Detail Prediksi**
   - Klik icon 👁️ (mata) pada kolom Aksi
   - Modal popup akan muncul dengan:
     - Semua data input
     - Hasil prediksi lengkap
     - Grafik probabilitas
     - Timestamp

6. **Download Hasil Individual**
   - Klik icon 📥 (download)
   - Pilih format:
     - PDF - Untuk laporan
     - Excel - Untuk analisis
     - JSON - Untuk integrasi

7. **Menghapus Prediksi**
   - Klik icon 🗑️ (trash)
   - Konfirmasi penghapusan
   - Data akan dihapus permanen

8. **Export Semua Data**
   - Klik tombol "📥 Export Semua"
   - Pilih format export
   - File akan otomatis terdownload

9. **Clear All History**
   - Klik tombol "🗑️ Hapus Semua"
   - Konfirmasi dengan ketik: "DELETE ALL"
   - Semua riwayat akan terhapus

### 5.3 Melihat Analitik

1. **Akses Menu Analitik**
   - Klik "Analitik" di menu utama

2. **Grafik Tren Bulanan**
   - **Fungsi**: Melihat pola prediksi per bulan
   - **Interaksi**:
     - Hover mouse untuk detail
     - Klik legend untuk hide/show data
   - **Insight**: Identifikasi tren peningkatan/penurunan kredit macet

3. **Distribusi Tingkat Risiko**
   - **Fungsi**: Melihat sebaran tingkat risiko
   - **Jenis**: Radar Chart
   - **Kategori**: 
     - Sangat Rendah
     - Rendah
     - Sedang
     - Tinggi
     - Sangat Tinggi

4. **Top 10 Pekerjaan**
   - **Fungsi**: Pekerjaan mana yang paling banyak apply kredit
   - **Jenis**: Horizontal Bar Chart
   - **Sorting**: Otomatis dari tertinggi

5. **Distribusi Plafond**
   - **Fungsi**: Melihat range plafond yang paling umum
   - **Range**:
     - < 10 juta
     - 10-25 juta
     - 25-50 juta
     - 50-100 juta
     - 100-250 juta
     - > 250 juta

6. **Tabel Statistik Detail**
   - Breakdown per kategori:
     - Pekerjaan
     - Status Pernikahan
     - Produk
     - Range Usia
   - Kolom:
     - Total prediksi
     - Jumlah lancar
     - Jumlah macet
     - Rasio (%)

7. **Filter Periode**
   - Pilih range tanggal:
     - Hari ini
     - 7 hari terakhir
     - 30 hari terakhir
     - 3 bulan terakhir
     - Custom range

8. **Export Grafik**
   - Klik icon download di pojok grafik
   - Format: PNG atau SVG

### 5.4 Settings & Konfigurasi

1. **Akses Settings**
   - Klik menu "Settings"

2. **Pengaturan Tampilan**
   - **Theme**: Light/Dark mode
   - **Font Size**: Small/Medium/Large
   - **Language**: Bahasa Indonesia/English

3. **Pengaturan Notifikasi**
   - Email notification
   - Browser notification
   - Sound alerts

4. **Pengaturan Data**
   - Auto-save predictions
   - Data retention period
   - Export default format

5. **Pengaturan Model**
   - Switch model version
   - View model metrics
   - Update threshold

6. **Backup & Restore**
   - Backup all data
   - Restore from backup
   - Export settings

### 5.5 Help & Support

1. **Akses Help Page**
   - Klik menu "Help"

2. **Fitur Help**
   - 📚 Tutorial video
   - 📖 Documentation
   - 💬 Live chat support
   - 📧 Email support
   - 🐛 Report bug

3. **Quick Guide**
   - Panduan singkat setiap fitur
   - Screenshot tutorial
   - FAQ interaktif

---

## 6. TUTORIAL STEP-BY-STEP

### Tutorial 1: Prediksi Kredit Pertama Anda

**Skenario**: Bapak Ahmad (35 tahun) adalah PNS yang ingin mengajukan KPR sebesar Rp 100.000.000 untuk jangka waktu 10 tahun.

**Langkah Detail:**

1. **Buka aplikasi** di browser: `http://localhost:5000`

2. **Klik menu "Prediksi"**

3. **Isi Data Step 1:**
   - Tanggal Lahir: `15/01/1991` (untuk usia 35 tahun)
   - Pekerjaan: Pilih `"1 - PNS"`
   - Status Pernikahan: `"K - Kawin"`
   - Klik **"Lanjut"**

4. **Isi Data Step 2:**
   - Produk: `"KPR"`
   - Sub Produk: `"KPR Subsidi"`
   - Plafond: `100000000`
   - Jangka Waktu: `120` (10 tahun × 12 bulan)
   - Klik **"Lanjut"**

5. **Isi Data Step 3:**
   - Status Aplikasi: `"Accept"`
   - Hasil Prescreening SIPKUR: `"Sesuai"`
   - Hasil Prescreening Dukcapil: `"Sesuai"`
   - Klik **"Prediksi Sekarang"**

6. **Tunggu hasil** (1-2 detik)

7. **Interpretasi Hasil:**
   - Jika **Status = Lancar** dan **Risiko = Rendah**
     - ✅ Pemohon layak mendapat kredit
     - Probabilitas lancar tinggi (>80%)
     - Rekomendasi: Approve
   
   - Jika **Status = Macet** dan **Risiko = Tinggi**
     - ⚠️ Pemohon berisiko tinggi
     - Probabilitas macet tinggi (>60%)
     - Rekomendasi: Evaluasi lebih lanjut atau Reject

8. **Simpan hasil**:
   - Klik **"Simpan ke Riwayat"**
   - Beri nama: "Ahmad - KPR Subsidi"
   - Klik **"Simpan"**

9. **Selesai!** Lihat di menu "Riwayat" untuk verifikasi

### Tutorial 2: Analisis Batch Multiple Prediksi

**Skenario**: Anda memiliki 10 calon peminjam dan ingin menganalisis semuanya

**Langkah:**

1. Untuk setiap peminjam:
   - Lakukan prediksi seperti Tutorial 1
   - Simpan dengan nama yang jelas
   - Contoh: "Budi - KTA", "Siti - KKB"

2. Setelah semua selesai:
   - Buka menu **"Riwayat"**
   - Klik **"Export Semua"**
   - Pilih **Excel**

3. Buka file Excel:
   - Analisis dengan Pivot Table
   - Filter berdasarkan status
   - Hitung rasio approval

4. Buka menu **"Analitik"**:
   - Lihat distribusi risiko
   - Identifikasi pola
   - Screenshot grafik untuk laporan

5. Buat laporan summary di Excel

### Tutorial 3: Monitoring Trend Mingguan

**Skenario**: Setiap minggu Anda ingin monitor performa prediksi

**Langkah:**

1. **Senin pagi**:
   - Buka Dashboard
   - Screenshot Quick Stats
   - Catat: Total, Lancar, Macet, Rasio

2. **Setiap hari**:
   - Lakukan prediksi sesuai kebutuhan
   - Pastikan tersimpan di riwayat

3. **Jumat sore**:
   - Buka Analitik
   - Filter: "7 hari terakhir"
   - Lihat Tren Bulanan (weekly view)
   - Export grafik

4. **Bandingkan**:
   - Data Senin vs Jumat
   - Hitung pertumbuhan
   - Identifikasi anomali

5. **Buat laporan mingguan**:
   - Template: Excel
   - Include: Stats, Grafik, Insight
   - Share ke stakeholder

### Tutorial 4: Export dan Reporting

**Skenario**: Perlu laporan bulanan untuk manajemen

**Langkah:**

1. **Pengumpulan Data**:
   - Buka Riwayat
   - Filter periode: "30 hari terakhir"
   - Export ke Excel

2. **Processing di Excel**:
   ```
   - Sheet 1: Raw Data
   - Sheet 2: Summary Statistics
   - Sheet 3: Charts
   - Sheet 4: Insights & Recommendations
   ```

3. **Dashboard di Excel**:
   - Create Pivot Tables
   - Add Slicers
   - Insert Charts

4. **Analitik Web**:
   - Buka menu Analitik
   - Export setiap grafik
   - Insert ke PowerPoint

5. **Final Report**:
   - Cover page
   - Executive Summary
   - Detailed Analysis
   - Charts & Graphs
   - Conclusions & Recommendations

### Tutorial 5: Troubleshooting Prediksi Aneh

**Skenario**: Hasil prediksi tidak sesuai ekspektasi

**Langkah:**

1. **Verifikasi Input**:
   - Check tanggal lahir → usia harus benar
   - Check plafond → tidak ada typo
   - Check jangka waktu → dalam range normal

2. **Cek Konsistensi**:
   - Pekerjaan vs Plafond → apakah masuk akal?
   - Jangka waktu vs Usia → apakah feasible?
   - Prescreening → apakah sudah sesuai?

3. **Ulangi Prediksi**:
   - Reset form
   - Input ulang dengan teliti
   - Bandingkan hasilnya

4. **Bandingkan dengan Historical**:
   - Cari di riwayat: profil serupa
   - Lihat hasil prediksi sebelumnya
   - Identifikasi perbedaan

5. **Jika masih aneh**:
   - Screenshot hasilnya
   - Note semua parameter
   - Contact support
   - Lampirkan detail

---

## 7. INTERPRETASI HASIL

### 7.1 Memahami Output Prediksi

Setiap prediksi menghasilkan beberapa komponen:

#### A. Status Prediksi

```
🟢 LANCAR  atau  🔴 TIDAK LANCAR
```

- **LANCAR**: Peminjam diprediksi akan membayar cicilan tepat waktu
- **TIDAK LANCAR**: Peminjam diprediksi berisiko menunggak/macet

#### B. Probabilitas (Confidence)

```
📊 Probabilitas:
   • Lancar:       78.3%
   • Tidak Lancar: 21.7%
   ────────────────────
   Total:         100.0%
```

**Interpretasi:**
- **>80%**: Confidence sangat tinggi
- **60-80%**: Confidence tinggi  
- **40-60%**: Confidence sedang (borderline)
- **<40%**: Confidence rendah

**Contoh:**
- Lancar 95% → Hampir pasti lancar ✅
- Lancar 55% → Borderline, perlu review manual ⚠️
- Lancar 30% → Cenderung macet ❌

#### C. Tingkat Risiko

| Risiko | Range | Warna | Arti | Rekomendasi |
|--------|-------|-------|------|-------------|
| Sangat Rendah | < 20% | 🟢 Hijau | Aman | Approve |
| Rendah | 20-40% | 🔵 Biru | Low risk | Approve |
| Sedang | 40-60% | 🟡 Kuning | Medium risk | Review manual |
| Tinggi | 60-80% | 🟠 Orange | High risk | Extra checking |
| Sangat Tinggi | > 80% | 🔴 Merah | Very high risk | Reject atau agunan lebih |

#### D. Rekomendasi Sistem

Sistem memberikan rekomendasi otomatis:

1. **"Pemohon layak mendapatkan kredit dengan risiko rendah"**
   - Status: LANCAR
   - Risiko: Sangat Rendah/Rendah
   - Aksi: ✅ APPROVE
   - Syarat tambahan: Standard

2. **"Pemohon memiliki risiko kredit macet yang tinggi. Perlu evaluasi lebih lanjut."**
   - Status: TIDAK LANCAR
   - Risiko: Tinggi/Sangat Tinggi
   - Aksi: ⚠️ REVIEW atau ❌ REJECT
   - Syarat tambahan:
     - Agunan lebih besar
     - Co-applicant
     - Asuransi jiwa
     - Down payment lebih tinggi

### 7.2 Faktor yang Mempengaruhi Prediksi

Model mempertimbangkan 10 faktor utama:

#### 1. **Jangka Waktu** (Penting: ⭐⭐⭐⭐)
   - Semakin panjang → risiko semakin tinggi
   - Sweet spot: 12-60 bulan
   - > 120 bulan → risiko naik signifikan

#### 2. **Plafond** (Penting: ⭐⭐⭐⭐⭐)
   - Jumlah pinjaman vs kemampuan bayar
   - Rasio dengan income (DTI)
   - Terlalu besar → risiko tinggi

#### 3. **Usia** (Penting: ⭐⭐⭐)
   - Ideal: 25-50 tahun
   - < 25: Belum stabil finansial
   - > 55: Mendekati pensiun
   - Usia vs Jangka waktu harus masuk akal

#### 4. **Pekerjaan** (Penting: ⭐⭐⭐⭐⭐)
   - **Low risk**: PNS, TNI/Polri, Pegawai BUMN
   - **Medium risk**: Karyawan swasta, Profesional
   - **High risk**: Freelancer, Belum bekerja

#### 5. **Status Pernikahan** (Penting: ⭐⭐)
   - Kawin: Lebih stabil
   - Belum kawin: Fleksibilitas tinggi
   - Cerai: Potensi beban ganda

#### 6. **Produk** (Penting: ⭐⭐⭐)
   - KPR: Secured, low risk
   - KKB: Medium risk
   - KTA: Unsecured, higher risk

#### 7. **Sub Produk** (Penting: ⭐⭐)
   - Subsidi: Low risk
   - Komersial: Standard risk
   - Syariah: Depends on terms

#### 8. **Hasil Prescreening SIPKUR** (Penting: ⭐⭐⭐⭐)
   - Sesuai: ✅ Good sign
   - Tidak Sesuai: 🚩 Red flag
   - Minus (-): Belum clear

#### 9. **Hasil Prescreening Dukcapil** (Penting: ⭐⭐⭐⭐)
   - Sesuai: ✅ Valid identity
   - Tidak Sesuai: 🚩 Perlu investigasi
   - Minus (-): Belum verifikasi

#### 10. **Status Aplikasi** (Penting: ⭐⭐⭐)
   - Accept: Positive signal
   - Under Review: Neutral
   - Waiting Approval: Neutral
   - Reject: Negative signal

### 7.3 Contoh Kasus dan Interpretasi

#### Kasus 1: Approval Mudah ✅

```
Input:
- Usia: 35 tahun
- Pekerjaan: PNS
- Status Pernikahan: Kawin
- Produk: KPR Subsidi
- Plafond: Rp 80.000.000
- Jangka Waktu: 120 bulan
- SIPKUR: Sesuai
- Dukcapil: Sesuai
- Status Aplikasi: Accept

Hasil:
✅ STATUS: LANCAR
📊 Probabilitas Lancar: 92.5%
🟢 Risiko: Sangat Rendah (7.5%)
💡 Rekomendasi: Approve

Alasan:
- PNS = income stabil
- KPR Subsidi = program pemerintah
- Plafond reasonable
- Prescreening clear
- Profil ideal
```

#### Kasus 2: Perlu Review ⚠️

```
Input:
- Usia: 28 tahun
- Pekerjaan: Freelancer
- Status Pernikahan: Belum Kawin
- Produk: KTA
- Plafond: Rp 150.000.000
- Jangka Waktu: 60 bulan
- SIPKUR: Sesuai
- Dukcapil: Sesuai
- Status Aplikasi: Under Review

Hasil:
⚠️ STATUS: TIDAK LANCAR
📊 Probabilitas Macet: 58.3%
🟡 Risiko: Sedang (58.3%)
💡 Rekomendasi: Evaluasi lebih lanjut

Alasan:
- Freelancer = income tidak stabil
- KTA = unsecured loan
- Plafond terlalu besar
- Usia muda + belum kawin
- Perlu bukti income 6 bulan
```

#### Kasus 3: High Risk - Reject ❌

```
Input:
- Usia: 55 tahun
- Pekerjaan: Belum Bekerja
- Status Pernikahan: Cerai
- Produk: KTA
- Plafond: Rp 200.000.000
- Jangka Waktu: 84 bulan
- SIPKUR: Tidak Sesuai
- Dukcapil: Tidak Sesuai
- Status Aplikasi: Reject

Hasil:
❌ STATUS: TIDAK LANCAR
📊 Probabilitas Macet: 95.8%
🔴 Risiko: Sangat Tinggi (95.8%)
💡 Rekomendasi: Reject

Alasan:
- Tidak ada income
- Usia tinggi + jangka panjang
- Prescreening bermasalah
- Plafond tidak realistis
- Multiple red flags
```

### 7.4 Decision Matrix

Gunakan matriks ini untuk keputusan akhir:

| Probabilitas Macet | Risiko | Keputusan | Syarat Tambahan |
|-------------------|--------|-----------|-----------------|
| 0-20% | Sangat Rendah | ✅ APPROVE | Standard |
| 20-40% | Rendah | ✅ APPROVE | Standard |
| 40-50% | Sedang | ⚠️ REVIEW | Verifikasi income, asuransi |
| 50-60% | Sedang | ⚠️ REVIEW | Co-applicant atau agunan lebih |
| 60-80% | Tinggi | ⚠️ REVIEW | Agunan besar, DP tinggi |
| 80-100% | Sangat Tinggi | ❌ REJECT | Tidak direkomendasikan |

**Catatan**: Decision akhir tetap ada di tangan analis kredit. Model hanya memberikan rekomendasi.

---

## 8. TIPS DAN BEST PRACTICE

### 8.1 Tips Input Data

#### ✅ DO (Lakukan):

1. **Gunakan Data Real dan Lengkap**
   - Input semua field dengan benar
   - Jangan skip field apapun
   - Pastikan data akurat

2. **Verifikasi Tanggal Lahir**
   - Cross-check dengan KTP
   - Hitung usia manual untuk validasi
   - Pastikan format benar

3. **Plafond Realistis**
   - Sesuaikan dengan income
   - Gunakan rule of thumb: Max 30% dari penghasilan
   - Contoh: Gaji Rp 10 juta → Max cicilan Rp 3 juta

4. **Jangka Waktu Masuk Akal**
   - Pertimbangkan usia saat lunas
   - Contoh: Usia 50, jangka 20 tahun → lunas usia 70 (terlalu tua)
   - Ideal: Lunas sebelum usia 60

5. **Prescreening Harus Clear**
   - Selesaikan prescreening terlebih dahulu
   - Jangan gunakan "-" jika sudah ada hasil
   - Update jika ada perubahan

#### ❌ DON'T (Jangan):

1. **Jangan Asal Input**
   - Jangan gunakan data dummy
   - Jangan skip validasi
   - Jangan tebak-tebak

2. **Jangan Manipulasi Data**
   - Input data sebenarnya
   - Jangan ubah demi hasil baik
   - Sistem akan detect anomali

3. **Jangan Abaikan Warning**
   - Perhatikan pesan error
   - Perbaiki sebelum submit
   - Validasi ulang jika perlu

### 8.2 Best Practice Workflow

#### Workflow Ideal:

```
1. PERSIAPAN
   ├─ Kumpulkan dokumen pemohon
   ├─ Verifikasi identitas
   ├─ Lakukan prescreening
   └─ Validasi data

2. INPUT
   ├─ Buka aplikasi
   ├─ Isi form dengan teliti
   ├─ Double check setiap field
   └─ Submit prediksi

3. ANALISIS
   ├─ Baca hasil dengan seksama
   ├─ Perhatikan probabilitas
   ├─ Check tingkat risiko
   └─ Baca rekomendasi

4. KEPUTUSAN
   ├─ Pertimbangkan hasil model
   ├─ Review dokumen pendukung
   ├─ Konsultasi jika perlu
   └─ Buat keputusan final

5. DOKUMENTASI
   ├─ Simpan hasil prediksi
   ├─ Export untuk arsip
   ├─ Catat keputusan final
   └─ Update status aplikasi
```

### 8.3 Tips Interpretasi

1. **Jangan 100% Percaya Model**
   - Model adalah alat bantu, bukan keputusan final
   - Tetap perlu human judgment
   - Pertimbangkan faktor lain di luar model

2. **Perhatikan Borderline Cases**
   - Probabilitas 40-60%: Grey area
   - Perlu analisis mendalam
   - Mungkin perlu interview

3. **Kombinasikan dengan Tools Lain**
   - Credit scoring tradisional
   - Bank checking
   - BI checking
   - Employer verification

4. **Update Berkala**
   - Jika ada perubahan data pemohon
   - Lakukan prediksi ulang
   - Bandingkan hasilnya

### 8.4 Tips Performa Aplikasi

1. **Browser**
   - Gunakan Chrome/Firefox/Edge terbaru
   - Clear cache berkala
   - Disable extensions yang mengganggu

2. **Data Management**
   - Export riwayat setiap bulan
   - Clear history yang tidak terpakai
   - Backup data penting

3. **Network**
   - Gunakan koneksi stabil
   - Jika lemot, restart aplikasi
   - Check server status

### 8.5 Tips Keamanan Data

1. **Access Control**
   - Jangan share kredensial
   - Logout setelah selesai
   - Gunakan password kuat

2. **Data Privacy**
   - Jangan screenshot data sensitif
   - Encrypt file export
   - Delete data lama secara berkala

3. **Backup**
   - Backup mingguan recommended
   - Simpan di multiple lokasi
   - Encrypt backup file

---

## 9. TROUBLESHOOTING

### 9.1 Aplikasi Tidak Bisa Dijalankan

#### Problem: "python: command not found"

**Solusi:**
```bash
# Windows
1. Install Python dari python.org
2. Centang "Add to PATH" saat install
3. Restart Command Prompt
4. Test: python --version

# macOS/Linux
brew install python3
# atau
sudo apt install python3
```

#### Problem: "Module not found"

**Solusi:**
```bash
# Install dependencies
pip install -r requirements.txt

# Jika masih error, install manual:
pip install flask
pip install pandas
pip install scikit-learn
pip install joblib
```

#### Problem: "Port 5000 already in use"

**Solusi:**
```bash
# Windows
netstat -ano | findstr :5000
taskkill /PID [PID_NUMBER] /F

# macOS/Linux
lsof -ti:5000 | xargs kill -9

# Atau ubah port di app.py:
app.run(port=5001)  # Ganti port
```

### 9.2 Error Saat Prediksi

#### Problem: "Error encoding feature"

**Penyebab:** Input tidak sesuai dengan training data

**Solusi:**
1. Pastikan dropdown dipilih dengan benar
2. Jangan ketik manual di dropdown
3. Pastikan tidak ada special character
4. Restart aplikasi dan coba lagi

#### Problem: "Prediction failed"

**Solusi:**
1. Check console browser (F12) untuk detail error
2. Verifikasi semua field terisi
3. Pastikan format data benar:
   - Tanggal: DD/MM/YYYY
   - Plafond: Angka saja, tanpa Rp atau titik
   - Jangka Waktu: Angka dalam bulan
4. Clear cache browser
5. Refresh halaman

#### Problem: "Invalid date format"

**Solusi:**
```
Format yang benar: DD/MM/YYYY
Contoh: 15/01/1985

Bukan:
- 1985-01-15
- 01/15/1985
- 15-01-1985
```

### 9.3 Masalah Tampilan

#### Problem: "Grafik tidak muncul"

**Solusi:**
1. Pastikan ada data di riwayat
2. Refresh halaman (F5)
3. Clear browser cache
4. Coba browser lain
5. Check console untuk error JavaScript

#### Problem: "Layout berantakan"

**Solusi:**
1. Pastikan internet connected (untuk load Tailwind CSS)
2. Zoom browser di 100%
3. Gunakan browser modern
4. Clear cache dan cookies

#### Problem: "Responsive tidak bekerja di mobile"

**Solusi:**
1. Enable JavaScript di browser mobile
2. Gunakan Chrome/Safari mobile
3. Clear data aplikasi
4. Refresh halaman

### 9.4 Masalah Data

#### Problem: "Riwayat hilang setelah restart browser"

**Penyebab:** Local storage terhapus atau browser mode private

**Solusi:**
1. Jangan gunakan Incognito/Private mode
2. Aktifkan cookies dan local storage
3. Export data secara berkala sebagai backup

#### Problem: "Export tidak jalan"

**Solusi:**
1. Check pop-up blocker (harus allowed)
2. Pastikan ada data untuk diexport
3. Gunakan browser modern
4. Allow download di browser settings

### 9.5 Performance Issues

#### Problem: "Aplikasi lambat"

**Solusi:**
1. **Clear History Lama**
   ```javascript
   // Di browser console (F12)
   localStorage.clear();
   ```

2. **Restart Aplikasi**
   ```bash
   # Stop: Ctrl+C
   # Start: python app.py
   ```

3. **Check Resource**
   - RAM usage
   - CPU usage
   - Disk space

4. **Optimize Data**
   - Hapus riwayat > 6 bulan
   - Export lalu clear
   - Keep only recent data

#### Problem: "Browser freeze saat load analitik"

**Solusi:**
1. Terlalu banyak data → Filter periode lebih pendek
2. Close tab lain yang tidak perlu
3. Restart browser
4. Increase browser memory limit

### 9.6 Model Issues

#### Problem: "Hasil prediksi aneh/tidak masuk akal"

**Checklist Debugging:**

```
☐ Verifikasi input data:
  - Tanggal lahir benar?
  - Plafond format benar?
  - Dropdown pilihan valid?

☐ Cross-check dengan cases serupa:
  - Lihat riwayat profil mirip
  - Bandingkan hasilnya

☐ Validate dengan manual calculation:
  - DTI ratio
  - Age vs tenure

☐ Check model version:
  - Pastikan menggunakan model terbaru
  - Lihat di About page

☐ Contact support jika tetap aneh
```

### 9.7 Connection Issues

#### Problem: "Cannot connect to localhost:5000"

**Solusi:**
1. Pastikan aplikasi running (lihat terminal)
2. Coba akses: http://127.0.0.1:5000
3. Check firewall settings
4. Restart aplikasi

#### Problem: "Tidak bisa akses dari device lain"

**Solusi:**
1. Pastikan di network yang sama
2. Check firewall di server
3. Gunakan IP address, bukan localhost
4. Verify app running dengan `host="0.0.0.0"`

---

## 10. FAQ (PERTANYAAN YANG SERING DIAJUKAN)

### 10.1 Umum

**Q: Apakah aplikasi ini gratis?**  
A: Ya, aplikasi ini open source dan gratis digunakan untuk tujuan pendidikan dan riset.

**Q: Apakah perlu koneksi internet?**  
A: Hanya untuk load resources eksternal (Tailwind CSS, Font Awesome). Setelah ter-load, bisa offline.

**Q: Apakah data aman?**  
A: Data disimpan di local storage browser Anda, tidak dikirim ke server eksternal.

**Q: Bisa digunakan untuk production?**  
A: Bisa, tapi perlu penyesuaian seperti:
   - Database server (bukan local storage)
   - Authentication & authorization
   - HTTPS
   - Logging & monitoring

**Q: Support berapa bahasa?**  
A: Saat ini Bahasa Indonesia. English soon.

### 10.2 Tentang Model

**Q: Model menggunakan algoritma apa?**  
A: Random Forest Classifier dengan ensemble learning.

**Q: Akurasi model berapa persen?**  
A: ~95.7% (lihat di About page untuk detail).

**Q: Dataset training berapa banyak?**  
A: Informasi ada di metadata model. Check di About page.

**Q: Apakah model bisa diupdate?**  
A: Ya, dengan retrain menggunakan data baru di Jupyter Notebook.

**Q: Apa itu ensemble learning?**  
A: Teknik yang menggabungkan multiple model untuk hasil lebih akurat.

**Q: Fitur apa yang paling berpengaruh?**  
A: Berdasarkan feature importance:
   1. Plafond
   2. Pekerjaan
   3. Jangka Waktu
   4. Hasil Prescreening
   5. Usia

### 10.3 Penggunaan

**Q: Maksimal berapa prediksi per hari?**  
A: Tidak ada limit, tergantung resource server.

**Q: Apakah bisa batch predict (upload CSV)?**  
A: Saat ini belum. Coming soon di versi berikutnya.

**Q: Hasil prediksi tersimpan berapa lama?**  
A: Permanen di local storage sampai Anda hapus manual.

**Q: Bisa export ke format apa saja?**  
A: Excel, CSV, JSON, dan PDF.

**Q: Apakah ada API untuk integrasi?**  
A: Ya, ada API endpoint:
   - `/api/predict` - POST prediction
   - `/api/model-info` - GET model info

**Q: Bisa diakses dari mobile?**  
A: Ya, fully responsive.

### 10.4 Teknis

**Q: Database apa yang digunakan?**  
A: Saat ini menggunakan browser Local Storage. Untuk production, bisa gunakan PostgreSQL, MySQL, atau MongoDB.

**Q: Bisa deploy ke cloud?**  
A: Ya, bisa deploy ke:
   - Heroku
   - AWS EC2
   - Google Cloud Platform
   - Azure
   - DigitalOcean

**Q: Requirement Python versi berapa?**  
A: Python 3.8 atau lebih baru.

**Q: Bisa jalan di Raspberry Pi?**  
A: Ya, tapi mungkin perlu optimasi model untuk resource terbatas.

**Q: Support multi-user?**  
A: Versi current: single user (local storage).  
   Production: Perlu add database dan auth system.

### 10.5 Troubleshooting

**Q: Kenapa prediksi saya selalu macet?**  
A: Kemungkinan:
   - Input data memang high risk
   - Model bias terhadap pekerjaan/usia tertentu
   - Coba adjust parameter

**Q: Grafik kosong terus?**  
A: Pastikan sudah ada minimal 1 prediksi tersimpan di riwayat.

**Q: Export Excel error?**  
A: Check browser pop-up blocker dan allow download.

**Q: Aplikasi crash saat startup?**  
A: Check:
   - Python version
   - Dependencies installed
   - Model files ada
   - Port available

**Q: Memory usage tinggi?**  
A: Clear riwayat lama atau export lalu hapus.

### 10.6 Development

**Q: Bisa kontribusi ke project?**  
A: Ya, fork repository dan submit pull request.

**Q: Cara menambah fitur baru?**  
A: Edit `app.py` untuk backend, `templates/` untuk frontend.

**Q: Cara retrain model?**  
A: Gunakan Jupyter Notebook yang disediakan.

**Q: Dokumentasi API ada?**  
A: Check di folder `DOKUMENTASI/` atau `/api/docs`.

**Q: Support untuk bahasa pemrograman lain?**  
A: Bisa integrate via REST API dari bahasa apapun.

---

## 📞 KONTAK DAN SUPPORT

### Bantuan Lebih Lanjut

Jika Anda mengalami masalah atau memiliki pertanyaan:

1. **📖 Dokumentasi**: Baca file di folder `DOKUMENTASI/`
2. **💬 Help Page**: Akses menu Help di aplikasi
3. **🐛 Bug Report**: Create issue di repository
4. **📧 Email Support**: [Tambahkan email Anda]
5. **📱 WhatsApp**: [Tambahkan nomor Anda]

### Resources

- **Repository**: [GitHub URL]
- **Documentation**: [Documentation URL]
- **Video Tutorial**: [YouTube URL]
- **Website**: [Website URL]

---

## 📝 CHANGELOG

### Version 1.0.0 (Current)
- ✅ Initial release
- ✅ Prediksi kredit otomatis
- ✅ Dashboard interaktif
- ✅ Riwayat dan analitik
- ✅ Export data
- ✅ Responsive design

### Upcoming Features (Roadmap)
- 🔜 Batch prediction (upload CSV)
- 🔜 Multi-language support
- 🔜 Advanced filtering
- 🔜 Email notifications
- 🔜 User authentication
- 🔜 Database integration
- 🔜 Mobile app

---

## 📄 LISENSI

[Sesuaikan dengan lisensi project Anda]

---

## 🙏 TERIMA KASIH

Terima kasih telah menggunakan aplikasi **NPL Predictor**!

Semoga aplikasi ini membantu Anda dalam proses analisis kredit dan pengambilan keputusan yang lebih baik.

**Happy Predicting! 🚀**

---

*Dokumen ini terakhir diupdate: 14 Januari 2026*  
*Versi Aplikasi: 1.0.0*  
*Versi Model: model_20260112_100139*
