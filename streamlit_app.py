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

# Custom CSS untuk Material Design 3 Android Style
st.markdown(
    """
<style>
    @import url('https://fonts.googleapis.com/css2?family=Roboto:wght@300;400;500;700&display=swap');
    
    /* Root Variables - Material Design 3 */
    :root {
        --md-primary: #6750A4;
        --md-primary-container: #EADDFF;
        --md-on-primary: #FFFFFF;
        --md-secondary: #625B71;
        --md-secondary-container: #E8DEF8;
        --md-tertiary: #7D5260;
        --md-surface: #FFFBFE;
        --md-surface-variant: #E7E0EC;
        --md-background: #F5F5FF;
        --md-error: #B3261E;
        --md-success: #198754;
        --md-warning: #FFC107;
        --md-shadow: rgba(0, 0, 0, 0.1);
    }
    
    /* Base Styling */
    .stApp {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        font-family: 'Roboto', sans-serif;
    }
    
    .main .block-container {
        padding-top: 2rem;
        padding-bottom: 2rem;
        max-width: 1200px;
    }
    
    /* Material Design App Bar */
    .app-header {
        background: rgba(255, 255, 255, 0.95);
        backdrop-filter: blur(20px);
        -webkit-backdrop-filter: blur(20px);
        border-radius: 28px;
        padding: 2rem;
        margin-bottom: 1.5rem;
        box-shadow: 0 8px 32px rgba(0, 0, 0, 0.12);
        border: 1px solid rgba(255, 255, 255, 0.3);
        animation: slideDown 0.5s ease-out;
    }
    
    .app-title {
        font-size: 2.5rem;
        font-weight: 700;
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        text-align: center;
        margin: 0;
        letter-spacing: -0.5px;
    }
    
    .app-subtitle {
        font-size: 1rem;
        color: #5f6368;
        text-align: center;
        margin-top: 0.5rem;
        font-weight: 400;
    }
    
    /* Material Card Design */
    .material-card {
        background: rgba(255, 255, 255, 0.95);
        backdrop-filter: blur(20px);
        -webkit-backdrop-filter: blur(20px);
        border-radius: 24px;
        padding: 1.5rem;
        margin-bottom: 1rem;
        box-shadow: 0 4px 16px rgba(0, 0, 0, 0.08);
        border: 1px solid rgba(255, 255, 255, 0.5);
        transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1);
        animation: fadeIn 0.5s ease-out;
    }
    
    .material-card:hover {
        transform: translateY(-4px);
        box-shadow: 0 12px 32px rgba(0, 0, 0, 0.15);
    }
    
    /* Chip Design */
    .status-chip {
        display: inline-block;
        padding: 6px 16px;
        border-radius: 16px;
        font-size: 0.875rem;
        font-weight: 500;
        letter-spacing: 0.5px;
        margin: 4px;
        transition: all 0.2s ease;
    }
    
    .chip-success {
        background: #E8F5E9;
        color: #2E7D32;
    }
    
    .chip-warning {
        background: #FFF3E0;
        color: #E65100;
    }
    
    .chip-error {
        background: #FFEBEE;
        color: #C62828;
    }
    
    .chip-info {
        background: #E3F2FD;
        color: #1565C0;
    }
    
    /* Modern Input Styling */
    .stTextInput > div > div > input,
    .stNumberInput > div > div > input,
    .stSelectbox > div > div {
        border-radius: 12px !important;
        border: 2px solid #E7E0EC !important;
        padding: 12px 16px !important;
        font-size: 1rem !important;
        transition: all 0.3s ease !important;
        background: white !important;
    }
    
    .stTextInput > div > div > input:focus,
    .stNumberInput > div > div > input:focus,
    .stSelectbox > div > div:focus-within {
        border-color: #6750A4 !important;
        box-shadow: 0 0 0 3px rgba(103, 80, 164, 0.1) !important;
    }
    
    /* FAB (Floating Action Button) Style */
    .stButton button {
        width: 100%;
        border-radius: 28px !important;
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%) !important;
        color: white !important;
        font-weight: 600 !important;
        border: none !important;
        padding: 1rem 2rem !important;
        font-size: 1.1rem !important;
        letter-spacing: 0.5px !important;
        box-shadow: 0 8px 24px rgba(103, 80, 164, 0.3) !important;
        transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1) !important;
        text-transform: uppercase !important;
    }
    
    .stButton button:hover {
        transform: scale(1.02) translateY(-2px) !important;
        box-shadow: 0 12px 32px rgba(103, 80, 164, 0.4) !important;
    }
    
    .stButton button:active {
        transform: scale(0.98) !important;
    }
    
    /* Bottom Sheet Style Form */
    .stForm {
        background: rgba(255, 255, 255, 0.98);
        border-radius: 24px 24px 0 0;
        padding: 2rem;
        box-shadow: 0 -4px 24px rgba(0, 0, 0, 0.12);
        backdrop-filter: blur(20px);
        -webkit-backdrop-filter: blur(20px);
    }
    
    /* Expander Material Design */
    .streamlit-expanderHeader {
        background: linear-gradient(135deg, #EADDFF 0%, #E8DEF8 100%) !important;
        border-radius: 16px !important;
        padding: 1rem 1.5rem !important;
        font-weight: 600 !important;
        font-size: 1.1rem !important;
        color: #6750A4 !important;
        border: none !important;
        margin-bottom: 0.5rem !important;
        transition: all 0.3s ease !important;
    }
    
    .streamlit-expanderHeader:hover {
        background: linear-gradient(135deg, #D5C5F5 0%, #DDD0F3 100%) !important;
        transform: translateX(4px);
    }
    
    /* Progress Ring Design */
    .progress-ring {
        position: relative;
        width: 180px;
        height: 180px;
        margin: 0 auto;
    }
    
    .progress-ring-circle {
        transition: stroke-dashoffset 0.8s cubic-bezier(0.4, 0, 0.2, 1);
        transform: rotate(-90deg);
        transform-origin: 50% 50%;
    }
    
    /* Result Card with Glassmorphism */
    .result-card {
        background: rgba(255, 255, 255, 0.95);
        backdrop-filter: blur(40px);
        -webkit-backdrop-filter: blur(40px);
        border-radius: 28px;
        padding: 2rem;
        box-shadow: 0 8px 32px rgba(0, 0, 0, 0.12);
        border: 1px solid rgba(255, 255, 255, 0.6);
        margin: 1rem 0;
        animation: scaleIn 0.5s cubic-bezier(0.4, 0, 0.2, 1);
    }
    
    /* Metric Card - Android Style */
    .metric-container {
        background: linear-gradient(135deg, rgba(103, 80, 164, 0.1) 0%, rgba(118, 75, 162, 0.05) 100%);
        border-radius: 20px;
        padding: 1.5rem;
        margin: 0.5rem 0;
        border: 2px solid rgba(103, 80, 164, 0.2);
        transition: all 0.3s ease;
    }
    
    .metric-container:hover {
        background: linear-gradient(135deg, rgba(103, 80, 164, 0.15) 0%, rgba(118, 75, 162, 0.1) 100%);
        border-color: rgba(103, 80, 164, 0.3);
        transform: translateY(-2px);
    }
    
    .metric-value {
        font-size: 2rem;
        font-weight: 700;
        color: #6750A4;
        margin: 0;
    }
    
    .metric-label {
        font-size: 0.875rem;
        color: #625B71;
        font-weight: 500;
        text-transform: uppercase;
        letter-spacing: 1px;
        margin-top: 0.5rem;
    }
    
    /* Sidebar Material Design */
    section[data-testid="stSidebar"] {
        background: rgba(255, 255, 255, 0.95) !important;
        backdrop-filter: blur(20px);
        -webkit-backdrop-filter: blur(20px);
        border-right: 1px solid rgba(255, 255, 255, 0.3);
    }
    
    section[data-testid="stSidebar"] > div {
        padding-top: 2rem;
    }
    
    /* Modern Divider */
    hr {
        border: none;
        height: 2px;
        background: linear-gradient(90deg, transparent, #E7E0EC, transparent);
        margin: 2rem 0;
    }
    
    /* Animations */
    @keyframes slideDown {
        from {
            opacity: 0;
            transform: translateY(-20px);
        }
        to {
            opacity: 1;
            transform: translateY(0);
        }
    }
    
    @keyframes fadeIn {
        from {
            opacity: 0;
        }
        to {
            opacity: 1;
        }
    }
    
    @keyframes scaleIn {
        from {
            opacity: 0;
            transform: scale(0.95);
        }
        to {
            opacity: 1;
            transform: scale(1);
        }
    }
    
    /* Ripple Effect */
    .ripple {
        position: relative;
        overflow: hidden;
    }
    
    .ripple::after {
        content: '';
        position: absolute;
        top: 50%;
        left: 50%;
        width: 0;
        height: 0;
        border-radius: 50%;
        background: rgba(255, 255, 255, 0.5);
        transform: translate(-50%, -50%);
        transition: width 0.6s, height 0.6s;
    }
    
    .ripple:active::after {
        width: 300px;
        height: 300px;
    }
    
    /* Mobile Optimization */
    @media (max-width: 768px) {
        .app-title {
            font-size: 1.75rem;
        }
        
        .app-subtitle {
            font-size: 0.875rem;
        }
        
        .material-card {
            padding: 1rem;
            border-radius: 20px;
        }
        
        .result-card {
            padding: 1.5rem;
        }
    }
    
    /* Custom Scrollbar */
    ::-webkit-scrollbar {
        width: 8px;
        height: 8px;
    }
    
    ::-webkit-scrollbar-track {
        background: rgba(231, 224, 236, 0.3);
        border-radius: 10px;
    }
    
    ::-webkit-scrollbar-thumb {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        border-radius: 10px;
    }
    
    ::-webkit-scrollbar-thumb:hover {
        background: linear-gradient(135deg, #5568d3 0%, #6a3f8f 100%);
    }
    
    /* Info Alert Material Style */
    .stAlert {
        border-radius: 16px !important;
        border: none !important;
        padding: 1rem 1.5rem !important;
        backdrop-filter: blur(10px);
    }
    
    /* Success Badge */
    .success-badge {
        background: linear-gradient(135deg, #4CAF50 0%, #45a049 100%);
        color: white;
        padding: 8px 20px;
        border-radius: 20px;
        font-weight: 600;
        display: inline-block;
        box-shadow: 0 4px 12px rgba(76, 175, 80, 0.3);
    }
    
    /* Warning Badge */
    .warning-badge {
        background: linear-gradient(135deg, #FF9800 0%, #F57C00 100%);
        color: white;
        padding: 8px 20px;
        border-radius: 20px;
        font-weight: 600;
        display: inline-block;
        box-shadow: 0 4px 12px rgba(255, 152, 0, 0.3);
    }
    
    /* Error Badge */
    .error-badge {
        background: linear-gradient(135deg, #F44336 0%, #D32F2F 100%);
        color: white;
        padding: 8px 20px;
        border-radius: 20px;
        font-weight: 600;
        display: inline-block;
        box-shadow: 0 4px 12px rgba(244, 67, 54, 0.3);
    }
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


def create_circular_progress(confidence, risk_level):
    """Create a circular progress indicator like Android"""
    color_map = {
        1: "#4CAF50",  # Success Green
        2: "#FFC107",  # Warning Amber
        3: "#FF9800",  # Orange
        4: "#F44336",  # Error Red
        5: "#9C27B0",  # Purple
    }

    color = color_map.get(risk_level, "#6c757d")

    # Calculate circle parameters
    radius = 70
    circumference = 2 * 3.14159 * radius
    offset = circumference - (confidence / 100) * circumference

    progress_html = f"""
    <div style="display: flex; justify-content: center; align-items: center; margin: 2rem 0;">
        <div style="position: relative; width: 180px; height: 180px;">
            <svg width="180" height="180" style="transform: rotate(-90deg);">
                <circle
                    cx="90"
                    cy="90"
                    r="{radius}"
                    stroke="#E7E0EC"
                    stroke-width="12"
                    fill="none"
                />
                <circle
                    cx="90"
                    cy="90"
                    r="{radius}"
                    stroke="url(#gradient{risk_level})"
                    stroke-width="12"
                    fill="none"
                    stroke-dasharray="{circumference}"
                    stroke-dashoffset="{offset}"
                    stroke-linecap="round"
                    style="transition: stroke-dashoffset 0.8s cubic-bezier(0.4, 0, 0.2, 1);"
                />
                <defs>
                    <linearGradient id="gradient{risk_level}" x1="0%" y1="0%" x2="100%" y2="100%">
                        <stop offset="0%" style="stop-color:{color};stop-opacity:1" />
                        <stop offset="100%" style="stop-color:{color};stop-opacity:0.7" />
                    </linearGradient>
                </defs>
            </svg>
            <div style="position: absolute; top: 50%; left: 50%; transform: translate(-50%, -50%);
                        text-align: center;">
                <div style="font-size: 2.5rem; font-weight: 700; color: {color};">
                    {confidence:.0f}%
                </div>
                <div style="font-size: 0.875rem; color: #625B71; font-weight: 500; margin-top: 4px; color:white;">
                    CONFIDENCE
                </div>
            </div>
        </div>
    </div>
    """
    return progress_html


def main():
    # Modern App Header
    st.markdown(
        """
    <div class="app-header">
        <div style="text-align: center; margin-bottom: 0.5rem;">
            <span style="font-size: 3rem;">🏦</span>
        </div>
        <h1 class="app-title">Credit Risk Analyzer</h1>
        <p class="app-subtitle">AI-Powered Credit Assessment System</p>
    </div>
    """,
        unsafe_allow_html=True,
    )

    # Load model dengan progress indicator
    with st.spinner("🔄 Loading AI Model..."):
        model, scaler, label_encoders, target_encoder, metadata = load_model_package()

    if model is None:
        st.error(
            "❌ Model tidak dapat dimuat. Pastikan file model ada di folder 'models'."
        )
        return

    # Sidebar - Material Design
    with st.sidebar:
        st.markdown(
            """
        <div class="material-card">
            <h3 style="color: #6750A4; margin-top: 0;">📊 Model Information</h3>
        """,
            unsafe_allow_html=True,
        )

        if metadata:
            st.markdown(
                f"""
            <div class="metric-container">
                <div class="metric-value">{metadata['model_info']['model_name']}</div>
                <div class="metric-label">Model Type</div>
            </div>
            """,
                unsafe_allow_html=True,
            )

            col1, col2 = st.columns(2)
            with col1:
                st.markdown(
                    f"""
                <div class="metric-container">
                    <div class="metric-value">{metadata['performance_metrics']['test_accuracy']:.3f}</div>
                    <div class="metric-label">Accuracy</div>
                </div>
                """,
                    unsafe_allow_html=True,
                )

            with col2:
                st.markdown(
                    f"""
                <div class="metric-container">
                    <div class="metric-value">{metadata['performance_metrics']['test_f1_weighted']:.3f}</div>
                    <div class="metric-label">F1-Score</div>
                </div>
                """,
                    unsafe_allow_html=True,
                )

        st.markdown("</div>", unsafe_allow_html=True)

        st.markdown("---")

        st.markdown(
            """
        <div class="material-card">
            <h3 style="color: #6750A4; margin-top: 0;">💡 Quick Guide</h3>
            <div style="line-height: 2;">
                <div style="display: flex; align-items: center; margin: 0.5rem 0;">
                    <span style="font-size: 1.5rem; margin-right: 1rem;">📝</span>
                    <span style="color: #625B71;">Fill customer data</span>
                </div>
                <div style="display: flex; align-items: center; margin: 0.5rem 0;">
                    <span style="font-size: 1.5rem; margin-right: 1rem;">🎯</span>
                    <span style="color: #625B71;">Click predict button</span>
                </div>
                <div style="display: flex; align-items: center; margin: 0.5rem 0;">
                    <span style="font-size: 1.5rem; margin-right: 1rem;">📊</span>
                    <span style="color: #625B71;">View results & insights</span>
                </div>
            </div>
        </div>
        """,
            unsafe_allow_html=True,
        )

    # Main Content with Material Cards
    st.markdown(
        """
    <div class="material-card">
        <h2 style="color: #6750A4; margin-top: 0;">📝 Customer Information</h2>
    """,
        unsafe_allow_html=True,
    )

    with st.form("prediction_form"):
        # Demografis
        with st.expander("👤 **Demographic Information**", expanded=True):
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
                    "Occupation",
                    options=pekerjaan_options,
                    format_func=lambda x: x[1],
                    index=0,
                )[0]

                status_nikah = st.selectbox(
                    "Marital Status",
                    ["B (Belum Menikah)", "D (Cerai)", "K (Kawin)"],
                    index=2,
                )

            with col2:
                plafond = st.number_input(
                    "Credit Limit (IDR)",
                    min_value=0,
                    max_value=1000000000,
                    value=25000000,
                    step=1000000,
                    help="Jumlah plafond kredit yang diajukan",
                )

                jk_waktu = st.number_input(
                    "Loan Period (Months)",
                    min_value=6,
                    max_value=360,
                    value=36,
                    help="Jangka waktu pengembalian kredit",
                )

        # Produk Info
        with st.expander("💳 **Product Information**", expanded=True):
            col3, col4 = st.columns(2)

            with col3:
                produk = st.selectbox("Product Type", ["Konsumer", "Mikro"], index=0)
                sub_produk = st.selectbox(
                    "Sub Product", ["KMG", "KPR", "Mikro KUR", "Mikro NON KUR"], index=1
                )

            with col4:
                status = st.selectbox(
                    "Application Status",
                    ["Accept", "Lolos Bersyarat", "Reject", "Waiting Approval"],
                    index=0,
                )

        # Prescreening
        with st.expander("🔍 **Prescreening Results**", expanded=True):
            col5, col6 = st.columns(2)

            with col5:
                slik = st.selectbox("SLIK Result", ["Low", "Medium", "High"], index=0)
                sikpkur = st.selectbox(
                    "SIKPKUR Result",
                    [
                        "-",
                        "Terdaftar KUR",
                        "Terdaftar KUR di Bank Lain",
                        "Tidak Terdaftar KUR",
                    ],
                    index=0,
                )
                dukcapil = st.selectbox(
                    "DUKCAPIL Result", ["Sesuai", "Tidak Sesuai"], index=0
                )

            with col6:
                dhnbi = st.selectbox("DHNBI Result", ["Tidak", "Ya"], index=0)
                prescreening_1 = st.selectbox(
                    "Prescreening 1 Result", ["Lolos", "Tidak Lolos"], index=0
                )

        # Submit Button
        submitted = st.form_submit_button(
            "🎯 ANALYZE CREDIT RISK",
            use_container_width=True,
            type="primary",
        )

    st.markdown("</div>", unsafe_allow_html=True)

    # Results Section
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

            # Display Results - Material Design Style
            st.markdown("---")

            # Risk Badge Mapping
            risk_badges = {
                1: ("success-badge", "✅ LOW RISK"),
                2: ("warning-badge", "🟡 MEDIUM RISK"),
                3: ("warning-badge", "🟠 HIGH RISK"),
                4: ("error-badge", "🔴 VERY HIGH RISK"),
                5: ("error-badge", "🚨 EXTREME RISK"),
            }

            badge_class, badge_text = risk_badges.get(
                prediction_class, ("", "❓ UNKNOWN")
            )

            st.markdown(
                f"""
            <div class="result-card">
                <div style="text-align: center;">
                    <div class="{badge_class}" style="font-size: 1.2rem; margin-bottom: 1rem;">
                        {badge_text}
                    </div>
                    <h2 style="color: #6750A4; margin: 0.5rem 0;">{predicted_label}</h2>
                </div>
            """,
                unsafe_allow_html=True,
            )

            # Circular Progress
            st.markdown(
                create_circular_progress(confidence, prediction_class),
                unsafe_allow_html=True,
            )

            # Risk Description
            risk_descriptions = {
                1: "✅ Nasabah memiliki track record yang baik dan kemungkinan besar akan melunasi kredit tepat waktu.",
                2: "🟡 Nasabah memerlukan monitoring berkala. Terdapat potensi keterlambatan pembayaran.",
                3: "🟠 Kredit kurang lancar. Direkomendasikan untuk melakukan verifikasi tambahan dan tindakan preventif.",
                4: "🔴 Kredit sangat diragukan. Perlu evaluasi mendalam sebelum approval.",
                5: "🚨 Risiko kredit macet sangat tinggi. Pertimbangan khusus sangat diperlukan.",
            }

            st.markdown(
                f"""
                <div class="material-card" style="background: rgba(255, 255, 255, 0.7); margin-top: 1rem;">
                    <p style="color: #625B71; font-size: 1rem; line-height: 1.6; margin: 0;">
                        {risk_descriptions.get(prediction_class, "Risiko tidak teridentifikasi.")}
                    </p>
                </div>
            """,
                unsafe_allow_html=True,
            )

            st.markdown("</div>", unsafe_allow_html=True)

            # Probability Breakdown
            st.markdown(
                """
            <div class="material-card" style="margin-top: 1rem;">
                <h3 style="color: #6750A4; margin-top: 0;">📊 Detailed Risk Analysis</h3>
            """,
                unsafe_allow_html=True,
            )

            for i, prob in enumerate(prediction_proba):
                actual_class = target_encoder.classes_[i]
                class_label = class_labels[str(actual_class)]
                prob_percent = prob * 100

                # Color coding
                if prob_percent > 50:
                    bar_color = "#F44336"
                elif prob_percent > 30:
                    bar_color = "#FF9800"
                elif prob_percent > 15:
                    bar_color = "#FFC107"
                else:
                    bar_color = "#4CAF50"

                st.markdown(
                    f"""
                <div style="margin: 1rem 0;">
                    <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 0.5rem;">
                        <span style="font-weight: 600; color: white;">Class {actual_class} - {class_label}</span>
                        <span style="font-weight: 700; color: {bar_color}; font-size: 1.1rem;">{prob_percent:.1f}%</span>
                    </div>
                    <div style="background: #E7E0EC; border-radius: 10px; height: 12px; overflow: hidden;">
                        <div style="background: linear-gradient(90deg, {bar_color}, {bar_color}CC); 
                                    width: {prob_percent}%; height: 100%; border-radius: 10px;
                                    transition: width 0.8s cubic-bezier(0.4, 0, 0.2, 1);"></div>
                    </div>
                </div>
                """,
                    unsafe_allow_html=True,
                )

            st.markdown("</div>", unsafe_allow_html=True)

        except Exception as e:
            st.markdown(
                f"""
            <div class="material-card" style="background: #FFEBEE; border-left: 4px solid #F44336;">
                <h4 style="color: #C62828; margin-top: 0;">❌ Prediction Error</h4>
                <p style="color: #D32F2F; margin: 0;">{str(e)}</p>
            </div>
            """,
                unsafe_allow_html=True,
            )

    # Footer
    st.markdown("---")
    st.markdown(
        """
    <div style="text-align: center; padding: 2rem 0;">
        <div class="material-card" style="max-width: 600px; margin: 0 auto;">
            <p style="color: #625B71; margin: 0; font-size: 0.875rem;">
                <strong>Credit Risk Analyzer</strong> © 2025
            </p>
        </div>
    </div>
    """,
        unsafe_allow_html=True,
    )


if __name__ == "__main__":
    main()
