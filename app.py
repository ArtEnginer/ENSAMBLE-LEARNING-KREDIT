import os
import json
import joblib
import pandas as pd
from flask import Flask, render_template, request, jsonify
from datetime import datetime

app = Flask(__name__)

# Load model and preprocessors
MODEL_DIR = "models/model_20260114_221327"
METADATA_FILE = os.path.join(MODEL_DIR, "model_metadata.json")

# Load metadata
with open(METADATA_FILE, "r") as f:
    metadata = json.load(f)

# Load model dan preprocessors
model = joblib.load(os.path.join(MODEL_DIR, "best_model_random_forest.joblib"))
label_encoders = joblib.load(os.path.join(MODEL_DIR, "label_encoders.joblib"))
target_encoder = joblib.load(os.path.join(MODEL_DIR, "target_encoder.joblib"))
scaler = joblib.load(os.path.join(MODEL_DIR, "scaler.joblib"))

# Load dataset untuk mendapatkan unique values untuk dropdown
DATASET_PATH = os.path.join("DATASET", "dataset_npl.csv")
df = pd.read_csv(DATASET_PATH)

# Dictionary untuk mapping dan dropdown options
# Nilai harus sesuai dengan label encoder dari model
PEKERJAAN_OPTIONS = [
    "Accounting/Finance Officer",
    "Administrasi umum",
    "Buruh (buruh pabrik,buruh bangunan,buruhtani)",
    "Dokter",
    "Eksekutif",
    "Engineering",
    "Hukum (Pengacara, Notaris)",
    "Ibu rumah tangga",
    "Konsultan/Analis",
    "Lain-Lain",
    "Marketing",
    "Militer",
    "Nelayan",
    "Pegawai pemerintahan/lembaga negara",
    "Pejabat negara/penyelenggara negara",
    "Pelajar/Mahasiswa",
    "Pengajar (Guru,Dosen)",
    "Pengamanan",
    "Pensiunan",
    "Perhotelan & restoran (Koki,Bartender, dsb)",
    "Peternak",
    "Polisi",
    "Teknologi informasi",
    "Tenaga Medis (Perawat, Bidan, dan sebagainya)",
    "Transportasi darat (masinis, sopir,kondektur)",
    "Wiraswasta",
]

STATUS_PERNIKAHAN_OPTIONS = ["Kawin", "Belum Kawin", "Cerai"]

PRODUK_OPTIONS = ["Konsumer", "Mikro"]
SUB_PRODUK_OPTIONS = [
    "Kredit Multi Guna",
    "Kredit Pemilikan Rumah",
    "Mikro Kredit Usaha Rakyat",
    "Mikro Non - Kredit Usaha Rakyat",
]

HASIL_PRESCREENING_SIPKUR_OPTIONS = [
    "TIDAK DILAKUKAN",
    "Terdaftar KUR",
    "Terdaftar KUR di Bank Lain",
    "Tidak Terdaftar KUR",
]
HASIL_PRESCREENING_DUKCAPIL_OPTIONS = ["Sesuai", "Tidak Sesuai"]
STATUS_APLIKASI_OPTIONS = ["Accept", "Lolos Bersyarat", "Reject", "Waiting Approval"]


@app.route("/")
def dashboard():
    """Dashboard utama"""
    return render_template("dashboard.html", metadata=metadata)


@app.route("/predict")
def predict_page():
    """Halaman form prediksi"""
    return render_template(
        "predict.html",
        pekerjaan_options=PEKERJAAN_OPTIONS,
        status_pernikahan_options=STATUS_PERNIKAHAN_OPTIONS,
        produk_options=PRODUK_OPTIONS,
        sub_produk_options=SUB_PRODUK_OPTIONS,
        hasil_prescreening_sipkur_options=HASIL_PRESCREENING_SIPKUR_OPTIONS,
        hasil_prescreening_dukcapil_options=HASIL_PRESCREENING_DUKCAPIL_OPTIONS,
        status_aplikasi_options=STATUS_APLIKASI_OPTIONS,
        metadata=metadata,
    )


@app.route("/history")
def history():
    """Halaman riwayat prediksi"""
    return render_template("history.html", metadata=metadata)


@app.route("/analytics")
def analytics():
    """Halaman analitik"""
    return render_template("analytics.html", metadata=metadata)


@app.route("/about")
def about():
    """Halaman tentang model"""
    return render_template("about.html", metadata=metadata)


@app.route("/settings")
def settings():
    """Halaman pengaturan"""
    return render_template("settings.html", metadata=metadata)


@app.route("/help")
def help_page():
    """Halaman bantuan"""
    return render_template("help.html", metadata=metadata)


@app.route("/api/predict", methods=["POST"])
@app.route("/predict", methods=["POST"])
def predict_api():
    try:
        # Ambil data dari form
        data = request.json

        # Hitung usia dari tanggal lahir
        birth_date = datetime.strptime(data["tanggal_lahir"], "%Y-%m-%d")
        today = datetime.today()
        usia = (
            today.year
            - birth_date.year
            - ((today.month, today.day) < (birth_date.month, birth_date.day))
        )

        # Prepare input data sesuai dengan fitur yang dibutuhkan model
        # Urutan harus sesuai dengan metadata.features
        input_data = {
            "Sub Produk": data["sub_produk"],
            "Status Aplikasi": data["status_aplikasi"],
            "Plafond": float(data["plafond"]),
            "Jangka Waktu": int(data["jangka_waktu"]),
            "Hasil Prescreening Dukcapil": data["hasil_prescreening_dukcapil"],
            "Produk": data["produk"],
            "Status Pernikahan": data["status_pernikahan"],
            "Usia": usia,
            "Pekerjaan": data["pekerjaan"],
            "Hasil Prescreening SIPKUR": data["hasil_prescreening_sipkur"],
        }

        # Convert to DataFrame dengan urutan yang benar
        input_df = pd.DataFrame([input_data], columns=metadata["features"])

        print("DEBUG - Input columns:", input_df.columns.tolist())
        print("DEBUG - Expected features:", metadata["features"])

        # Encode categorical features
        for col in input_df.columns:
            if col in label_encoders:
                try:
                    input_df[col] = label_encoders[col].transform(input_df[col])
                except ValueError as e:
                    print(f"DEBUG - Error encoding {col}: {e}")
                    print(f"DEBUG - Valid values: {list(label_encoders[col].classes_)}")
                    print(f"DEBUG - Received value: {input_df[col].values[0]}")
                    return (
                        jsonify(
                            {
                                "status": "error",
                                "message": f"Nilai '{input_df[col].values[0]}' tidak valid untuk {col}",
                            }
                        ),
                        400,
                    )

        print("DEBUG - After encoding:", input_df.dtypes)
        print("DEBUG - DataFrame values:", input_df.values)

        # Pastikan semua data numeric
        input_df = input_df.astype(float)

        # Scale features - convert to numpy array to avoid feature name issues
        input_scaled = scaler.transform(input_df.values)

        # Predict
        prediction = model.predict(input_scaled)
        prediction_proba = model.predict_proba(input_scaled)

        # Decode prediction
        prediction_label = target_encoder.inverse_transform(prediction)[0]

        # Get probability
        prob_lancar = prediction_proba[0][0] * 100
        prob_tidak_lancar = prediction_proba[0][1] * 100

        # Determine risk level
        if prob_tidak_lancar < 20:
            risk_level = "Sangat Rendah"
            risk_color = "green"
        elif prob_tidak_lancar < 40:
            risk_level = "Rendah"
            risk_color = "blue"
        elif prob_tidak_lancar < 60:
            risk_level = "Sedang"
            risk_color = "yellow"
        elif prob_tidak_lancar < 80:
            risk_level = "Tinggi"
            risk_color = "orange"
        else:
            risk_level = "Sangat Tinggi"
            risk_color = "red"

        # Rekomendasi
        if prediction_label == "Lancar":
            rekomendasi = "Pemohon layak mendapatkan kredit dengan risiko rendah."
        else:
            rekomendasi = "Pemohon memiliki risiko kredit macet yang tinggi. Perlu evaluasi lebih lanjut."

        result = {
            "status": "success",
            "prediction": prediction_label,
            "probability": {
                "lancar": round(prob_lancar, 2),
                "tidak_lancar": round(prob_tidak_lancar, 2),
            },
            "risk_level": risk_level,
            "risk_color": risk_color,
            "rekomendasi": rekomendasi,
            "input_summary": {
                "usia": usia,
                "pekerjaan": data["pekerjaan"],
                "plafond": f"Rp {float(data['plafond']):,.0f}",
                "jangka_waktu": f"{data['jangka_waktu']} bulan",
                "status_pernikahan": data["status_pernikahan"],
                "produk": data["produk"],
                "sub_produk": data["sub_produk"],
            },
        }

        return jsonify(result)

    except Exception as e:
        return (
            jsonify({"status": "error", "message": f"Terjadi kesalahan: {str(e)}"}),
            400,
        )


@app.route("/api/model-info")
def model_info():
    """Endpoint untuk mendapatkan informasi model"""
    return jsonify(metadata)


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5000)
