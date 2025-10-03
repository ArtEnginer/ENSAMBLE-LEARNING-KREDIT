import streamlit as st
import pandas as pd
import numpy as np
import joblib
import json
from pathlib import Path

# Page config dengan optimasi mobile
st.set_page_config(
    page_title="Prediksi Kredit Macet",
    page_icon="🏦",
    layout="wide",
    initial_sidebar_state="expanded",
    menu_items={
        "About": "# Sistem Prediksi Kredit Macet\nML-powered credit risk assessment",
    },
)

# Custom CSS untuk styling yang lebih elegan dan mobile friendly
st.markdown(
    """
<style>
    /* Main styling */
    .main-header {
        font-size: 2.5rem !important;
        font-weight: 700 !important;
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        text-align: center;
        margin-bottom: 1rem;
    }
    
    .sub-header {
        font-size: 1.2rem !important;
        color: #6c757d !important;
        text-align: center;
        margin-bottom: 2rem;
    }
    
    /* Card styling */
    .prediction-card {
        background: linear-gradient(135deg, #f5f7fa 0%, #c3cfe2 100%);
        border-radius: 15px;
        padding: 1.5rem;
        box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
        border-left: 5px solid #667eea;
    }
    
    .risk-card {
        border-radius: 15px;
        padding: 1.5rem;
        box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
        margin-bottom: 1rem;
    }
    
    .metric-card {
        background: white;
        border-radius: 10px;
        padding: 1rem;
        box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
        border-left: 4px solid #667eea;
        margin-bottom: 0.5rem;
    }
    
    /* Button styling */
    .stButton button {
        width: 100%;
        border-radius: 10px;
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        color: white;
        font-weight: 600;
        border: none;
        padding: 0.75rem 1.5rem;
        transition: all 0.3s ease;
    }
    
    .stButton button:hover {
        transform: translateY(-2px);
        box-shadow: 0 4px 8px rgba(0, 0, 0, 0.2);
    }
    
    /* Form styling */
    .stForm {
        background: white;
        border-radius: 15px;
        padding: 2rem;
        box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
    }
    
    /* Progress bar styling */
    .stProgress > div > div > div > div {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
    }
    
    /* Mobile optimization */
    @media (max-width: 768px) {
        .main-header {
            font-size: 2rem !important;
        }
        .sub-header {
            font-size: 1rem !important;
        }
    }
    
    /* Custom risk colors */
    .risk-low { border-left: 5px solid #28a745 !important; }
    .risk-medium { border-left: 5px solid #ffc107 !important; }
    .risk-high { border-left: 5px solid #fd7e14 !important; }
    .risk-very-high { border-left: 5px solid #dc3545 !important; }
    .risk-extreme { border-left: 5px solid #6f42c1 !important; }
</style>
""",
    unsafe_allow_html=True,
)


@st.cache_resource
def load_model_package():
    """Load model and preprocessing objects"""
    try:
        # Load model and preprocessing objects
        model = joblib.load("models/best_model_random_forest_20251003_103852.joblib")
        scaler = joblib.load("models/scaler_20251003_103852.joblib")
        label_encoders = joblib.load("models/label_encoders_20251003_103852.joblib")
        target_encoder = joblib.load("models/target_encoder_20251003_103852.joblib")

        # Load metadata
        with open(
            "models/model_metadata_20251003_103852.json", "r", encoding="utf-8"
        ) as f:
            metadata = json.load(f)

        return model, scaler, label_encoders, target_encoder, metadata
    except Exception as e:
        st.error(f"Error loading model: {e}")
        return None, None, None, None, None


def create_risk_gauge(confidence, risk_level):
    """Create a visual risk gauge"""
    color_map = {
        1: "#28a745",  # Low - Green
        2: "#ffc107",  # Medium - Yellow
        3: "#fd7e14",  # High - Orange
        4: "#dc3545",  # Very High - Red
        5: "#6f42c1",  # Extreme - Purple
    }

    color = color_map.get(risk_level, "#6c757d")

    gauge_html = f"""
    <div style="text-align: center; margin: 1rem 0;">
        <div style="width: 200px; height: 200px; margin: 0 auto; position: relative;">
            <div style="width: 100%; height: 100%; border-radius: 50%; 
                        background: conic-gradient({color} 0% {confidence}%, #e9ecef {confidence}% 100%);
                        position: relative;">
                <div style="position: absolute; top: 50%; left: 50%; transform: translate(-50%, -50%);
                            width: 80%; height: 80%; background: white; border-radius: 50%; 
                            display: flex; align-items: center; justify-content: center;">
                    <span style="font-size: 2rem; font-weight: bold; color: {color};">
                        {confidence:.1f}%
                    </span>
                </div>
            </div>
        </div>
        <div style="margin-top: 1rem; font-weight: bold; color: {color}; font-size: 1.2rem;">
            Confidence Level
        </div>
    </div>
    """
    return gauge_html


def main():
    # Header dengan gradient yang lebih menarik
    st.markdown(
        '<h1 class="main-header">🏦 Prediksi Kredit Macet</h1>', unsafe_allow_html=True
    )
    st.markdown(
        '<p class="sub-header">Sistem Prediksi Kolektabilitas Kredit dengan Machine Learning</p>',
        unsafe_allow_html=True,
    )

    # Load model dengan progress indicator
    with st.spinner("🔄 Memuat model machine learning..."):
        model, scaler, label_encoders, target_encoder, metadata = load_model_package()

    if model is None:
        st.error(
            "❌ Model tidak dapat dimuat. Pastikan file model ada di folder 'models'."
        )
        return

    # Sidebar untuk model info dengan card yang lebih elegan
    with st.sidebar:
        st.markdown("### 📊 Informasi Model")

        if metadata:
            with st.container():
                st.markdown('<div class="metric-card">', unsafe_allow_html=True)
                st.metric(
                    label="Model Type", value=metadata["model_info"]["model_name"]
                )
                st.markdown("</div>", unsafe_allow_html=True)

                col_metrics1, col_metrics2 = st.columns(2)
                with col_metrics1:
                    st.markdown('<div class="metric-card">', unsafe_allow_html=True)
                    st.metric(
                        label="Accuracy",
                        value=f"{metadata['performance_metrics']['test_accuracy']:.4f}",
                    )
                    st.markdown("</div>", unsafe_allow_html=True)

                with col_metrics2:
                    st.markdown('<div class="metric-card">', unsafe_allow_html=True)
                    st.metric(
                        label="F1-Score",
                        value=f"{metadata['performance_metrics']['test_f1_weighted']:.4f}",
                    )
                    st.markdown("</div>", unsafe_allow_html=True)

        st.markdown("---")
        st.markdown("### 💡 Panduan Penggunaan")
        st.info(
            """
        1. Isi semua data nasabah
        2. Klik tombol prediksi
        3. Lihat hasil dan rekomendasi
        """
        )

    # Main content area
    # Untuk mobile friendly, kita gunakan single column layout dengan expander
    st.markdown("### 📝 Input Data Nasabah")

    with st.form("prediction_form"):
        # Gunakan expander untuk mengorganisir form input
        with st.expander("**Informasi Demografis**", expanded=True):
            col1, col2 = st.columns(2)

            with col1:
                pekerjaan_options = [
                    (4, "04 - Eksekutif"),
                    (5, "05 - Administrasi umum"),
                    (6, "06 - Teknologi informasi"),
                    (7, "07 - Konsultan/Analis"),
                    (8, "08 - Marketing"),
                    (9, "09 - Pengajar (Guru,Dosen)"),
                    (11, "11 - Pensiunan"),
                    (12, "12 - Pelajar/Mahasiswa"),
                    (13, "13 - Wiraswasta"),
                    (19, "19 - Tenaga Medis (Perawat, Bidan, dan sebagainya)"),
                    (21, "21 - Perhotelan & restoran (Koki,Bartender, dsb)"),
                    (26, "26 - Pengamanan"),
                    (31, "31 - Transportasi darat (masinis, sopir,kondektur)"),
                    (34, "34 - Ibu rumah tangga"),
                    (36, "36 - Pejabat negara/penyelenggara negara"),
                    (37, "37 - Pegawai pemerintahan/lembaga negara"),
                    (99, "99 - Lain-Lain"),
                ]
                pekerjaan = st.selectbox(
                    "Pekerjaan",
                    options=pekerjaan_options,
                    format_func=lambda x: x[1],
                    index=0,  # Default to first option (4)
                )[0]

                status_nikah = st.selectbox(
                    "Status Pernikahan",
                    ["B (Belum Menikah)", "D (Cerai)", "K (Kawin)"],
                    index=2,  # Default to 'K' to match notebook
                )

            with col2:
                plafond = st.number_input(
                    "Plafond Kredit (Rp)",
                    min_value=0,
                    max_value=1000000000,
                    value=25000000,
                    step=1000000,
                    help="Jumlah plafond kredit yang diajukan",
                )

                jk_waktu = st.number_input(
                    "Jangka Waktu (Bulan)",
                    min_value=6,
                    max_value=360,
                    value=36,
                    help="Jangka waktu pengembalian kredit",
                )

        with st.expander("**Informasi Produk**", expanded=True):
            col3, col4 = st.columns(2)

            with col3:
                produk = st.selectbox("Jenis Produk", ["Konsumer", "Mikro"], index=0)
                sub_produk = st.selectbox(
                    "Sub Produk", ["KMG", "KPR", "Mikro KUR", "Mikro NON KUR"], index=1
                )

            with col4:
                status = st.selectbox(
                    "Status Pengajuan",
                    ["Accept", "Lolos Bersyarat", "Reject", "Waiting Approval"],
                    index=0,
                )

        with st.expander("**Hasil Prescreening**", expanded=True):
            col5, col6 = st.columns(2)

            with col5:
                slik = st.selectbox("Hasil SLIK", ["Low", "Medium", "High"], index=0)
                sikpkur = st.selectbox(
                    "Hasil SIKPKUR",
                    [
                        "-",
                        "Terdaftar KUR",
                        "Terdaftar KUR di Bank Lain",
                        "Tidak Terdaftar KUR",
                    ],
                    index=0,
                )
                dukcapil = st.selectbox(
                    "Hasil DUKCAPIL", ["Sesuai", "Tidak Sesuai"], index=0
                )

            with col6:
                dhnbi = st.selectbox("Hasil DHNBI", ["Tidak", "Ya"], index=0)
                prescreening_1 = st.selectbox(
                    "Hasil Prescreening 1", ["Lolos", "Tidak Lolos"], index=0
                )

        # Predict button yang lebih menarik
        submitted = st.form_submit_button(
            "🎯 Prediksi Kolektabilitas Kredit",
            use_container_width=True,
            type="primary",
        )

    # Results section
    if submitted:
        try:
            # Extract code for model input
            status_nikah_code = status_nikah[0]

            # Prepare input data
            input_data = pd.DataFrame(
                {
                    "PEKERJAAN": [pekerjaan],
                    "PLAFOND": [plafond],
                    "JK_WAKTUBULAN": [jk_waktu],
                    "STATUS_PERNIKAHAN": [status_nikah_code],
                    "PRODUK": [produk],
                    "SUB_PRODUK": [sub_produk],
                    "HASIL_PRESCREENING_SLIK": [slik],
                    "HASIL_PRESCREENING_SIKPKUR": [sikpkur],
                    "HASIL_PRESCREENING_DUKCAPIL": [dukcapil],
                    "HASIL_PRESCREENING_DHNBI": [dhnbi],
                    "HASIL_PRESCREENING_1": [prescreening_1],
                    "STATUS": [status],
                }
            )

            # Encode categorical features
            categorical_features = metadata["feature_info"]["categorical_features"]
            input_encoded = input_data.copy()

            for col in categorical_features:
                if col in input_data.columns:
                    input_encoded[col] = label_encoders[col].transform(input_data[col])

            # Scale features
            input_scaled = scaler.transform(input_encoded)

            # Make prediction
            prediction_encoded = model.predict(input_scaled)[0]
            prediction_class = target_encoder.inverse_transform([prediction_encoded])[0]
            prediction_proba = model.predict_proba(input_scaled)[0]

            # Get class labels
            class_labels = metadata["target_info"]["class_labels"]
            predicted_label = class_labels[str(prediction_class)]
            confidence = max(prediction_proba) * 100

            # Display results dengan layout yang lebih baik untuk mobile
            st.markdown("---")
            st.markdown("## 🎯 Hasil Prediksi")

            # Main prediction card
            risk_classes = {
                1: ("risk-low", "✅"),
                2: ("risk-medium", "🟡"),
                3: ("risk-high", "🟠"),
                4: ("risk-very-high", "🔴"),
                5: ("risk-extreme", "🚨"),
            }

            risk_class, emoji = risk_classes.get(prediction_class, ("", "❓"))

            st.markdown(
                f'<div class="prediction-card {risk_class}">', unsafe_allow_html=True
            )

            col_result1, col_result2 = st.columns([1, 2])

            with col_result1:
                # Gauge chart
                st.markdown(
                    create_risk_gauge(confidence, prediction_class),
                    unsafe_allow_html=True,
                )

            with col_result2:
                st.markdown(f"### {emoji} {predicted_label}")
                st.markdown(f"**Tingkat Keyakinan:** {confidence:.2f}%")

                # Risk description
                risk_descriptions = {
                    1: "Nasabah berpotensi melunasi kredit dengan lancar. Risiko rendah.",
                    2: "Perlu perhatian khusus dalam monitoring. Risiko sedang.",
                    3: "Kredit kurang lancar, perlu tindakan preventif. Risiko tinggi.",
                    4: "Kredit diragukan, perlu evaluasi mendalam. Risiko sangat tinggi.",
                    5: "Kredit berpotensi macet, pertimbangan khusus diperlukan. Risiko ekstrim.",
                }

                st.info(
                    risk_descriptions.get(
                        prediction_class, "Risiko tidak teridentifikasi."
                    )
                )

            st.markdown("</div>", unsafe_allow_html=True)

            # Probability breakdown dengan visual yang lebih baik
            st.markdown("### 📊 Detail Probabilitas")

            prob_data = []
            for i, prob in enumerate(prediction_proba):
                actual_class = target_encoder.classes_[i]
                class_label = class_labels[str(actual_class)]
                prob_percent = prob * 100

                col_prob1, col_prob2, col_prob3 = st.columns([1, 3, 1])
                with col_prob1:
                    st.markdown(f"**{actual_class}**")
                with col_prob2:
                    st.progress(float(prob))
                with col_prob3:
                    st.markdown(f"**{prob_percent:.1f}%**")

                st.caption(f"{class_label}")
                st.markdown("---")

        except Exception as e:
            st.error(f"❌ Error dalam prediksi: {str(e)}")
            st.info("Silakan periksa input data dan coba lagi.")

    # Footer yang lebih informatif
    st.markdown("---")
    st.markdown(
        """
    <div style="text-align: center; color: #6c757d; margin-top: 2rem;">
        <p>© 2024 Sistem Prediksi Kredit Macet. All rights reserved.</p>
    </div>
    """,
        unsafe_allow_html=True,
    )


if __name__ == "__main__":
    main()
