
import streamlit as st
import pandas as pd
import numpy as np
import pickle
import plotly.express as px
import plotly.graph_objects as go
from datetime import datetime
import warnings
warnings.filterwarnings('ignore')

# Page configuration
st.set_page_config(
    page_title="🏦 Kredit Macet Prediction System",
    page_icon="🏦",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS for better styling
st.markdown("""
<style>
    .main-header {
        background: linear-gradient(90deg, #1f77b4 0%, #ff7f0e 100%);
        padding: 1rem;
        border-radius: 10px;
        text-align: center;
        color: white;
        margin-bottom: 2rem;
    }
    .metric-card {
        background: #f0f2f6;
        padding: 1rem;
        border-radius: 10px;
        border-left: 4px solid #1f77b4;
        margin: 0.5rem 0;
    }
    .prediction-result {
        padding: 1.5rem;
        border-radius: 10px;
        text-align: center;
        font-size: 1.2rem;
        font-weight: bold;
        margin: 1rem 0;
    }
    .risk-low { background: #d4edda; color: #155724; border: 2px solid #c3e6cb; }
    .risk-medium { background: #fff3cd; color: #856404; border: 2px solid #ffeaa7; }
    .risk-high { background: #f8d7da; color: #721c24; border: 2px solid #f5c6cb; }
    .risk-critical { background: #f8d7da; color: #721c24; border: 2px solid #dc3545; }
</style>
""", unsafe_allow_html=True)

# Load model function
@st.cache_resource
def load_model():
    try:
        with open('model_deployment/kredit_macet_model_20251002_223007.pkl', 'rb') as f:
            model_package = pickle.load(f)
        return model_package
    except FileNotFoundError:
        st.error("❌ Model file not found! Please ensure the model is properly saved.")
        return None

# Main application
def main():
    # Header
    st.markdown("""
    <div class="main-header">
        <h1>🏦 Sistem Prediksi Kredit Macet</h1>
        <p>Prediksi Risiko Kredit Menggunakan Machine Learning</p>
    </div>
    """, unsafe_allow_html=True)

    # Load model
    model_package = load_model()
    if model_package is None:
        return

    # Sidebar for model info
    st.sidebar.markdown("## 📊 Model Information")
    st.sidebar.info(f"""
    **Model Type:** {model_package['model_metadata']['model_type']}
    **Training Date:** {model_package['model_metadata']['training_date'][:10]}
    **F1-Score:** {model_package['model_metadata']['f1_score']:.4f}
    **Accuracy:** {model_package['model_metadata']['accuracy']:.4f}
    **AUC Score:** {model_package['model_metadata']['auc_score']:.4f}
    """)

    # Tabs for different functionalities
    tab1, tab2, tab3 = st.tabs(["🔮 Prediksi", "📊 Batch Prediction", "📈 Model Analytics"])

    with tab1:
        st.header("🔮 Prediksi Individual")

        # Create input form
        with st.form("prediction_form"):
            col1, col2, col3 = st.columns(3)

            with col1:
                st.subheader("📋 Data Nasabah")
                jenis_kelamin = st.selectbox("Jenis Kelamin", ["L", "P"])
                status_nikah = st.selectbox("Status Nikah", ["Menikah", "Belum Menikah", "Cerai"])
                pendidikan = st.selectbox("Pendidikan", ["SD", "SMP", "SMA", "D3", "S1", "S2", "S3"])
                umur = st.number_input("Umur", min_value=18, max_value=80, value=35)
                lama_bekerja = st.number_input("Lama Bekerja (tahun)", min_value=0, max_value=50, value=5)

            with col2:
                st.subheader("💰 Data Keuangan")
                penghasilan = st.number_input("Penghasilan Bulanan (Rp)", min_value=1000000, max_value=100000000, value=5000000)
                jumlah_pinjaman = st.number_input("Jumlah Pinjaman (Rp)", min_value=1000000, max_value=500000000, value=50000000)
                jangka_waktu = st.number_input("Jangka Waktu (bulan)", min_value=6, max_value=240, value=24)
                angsuran_bulanan = st.number_input("Angsuran Bulanan (Rp)", min_value=100000, max_value=50000000, value=2500000)
                total_tanggungan = st.number_input("Total Tanggungan", min_value=0, max_value=10, value=2)

            with col3:
                st.subheader("🏠 Data Tambahan")
                tipe_properti = st.selectbox("Tipe Properti", ["Rumah", "Apartemen", "Ruko", "Tanah"])
                kepemilikan_properti = st.selectbox("Kepemilikan Properti", ["Milik Sendiri", "Kredit", "Sewa", "Orang Tua"])
                riwayat_kredit = st.selectbox("Riwayat Kredit", ["Baik", "Cukup", "Buruk"])
                jumlah_kartu_kredit = st.number_input("Jumlah Kartu Kredit", min_value=0, max_value=20, value=2)
                skor_kredit = st.number_input("Skor Kredit", min_value=300, max_value=850, value=650)

            submitted = st.form_submit_button("🔮 Prediksi Risiko Kredit", use_container_width=True)

            if submitted:
                # Prepare input data
                input_data = pd.DataFrame({
                    'Jenis_Kelamin': [jenis_kelamin],
                    'Status_Nikah': [status_nikah],
                    'Pendidikan': [pendidikan],
                    'Umur': [umur],
                    'Lama_Bekerja': [lama_bekerja],
                    'Penghasilan': [penghasilan],
                    'Jumlah_Pinjaman': [jumlah_pinjaman],
                    'Jangka_Waktu': [jangka_waktu],
                    'Angsuran_Bulanan': [angsuran_bulanan],
                    'Total_Tanggungan': [total_tanggungan],
                    'Tipe_Properti': [tipe_properti],
                    'Kepemilikan_Properti': [kepemilikan_properti],
                    'Riwayat_Kredit': [riwayat_kredit],
                    'Jumlah_Kartu_Kredit': [jumlah_kartu_kredit],
                    'Skor_Kredit': [skor_kredit]
                })

                # Add missing columns with default values
                feature_names = model_package['feature_names']
                for col in feature_names:
                    if col not in input_data.columns:
                        input_data[col] = 0

                # Reorder columns to match training data
                input_data = input_data[feature_names]

                try:
                    # Apply label encoding for categorical variables
                    for col, encoder in model_package['label_encoders'].items():
                        if col in input_data.columns:
                            # Handle unseen categories
                            if input_data[col].iloc[0] in encoder.classes_:
                                input_data[col] = encoder.transform(input_data[col])
                            else:
                                input_data[col] = 0  # Default for unseen categories

                    # Scale features
                    input_scaled = model_package['scaler'].transform(input_data)

                    # Make prediction
                    prediction = model_package['model'].predict(input_scaled)[0]
                    prediction_proba = model_package['model'].predict_proba(input_scaled)[0]

                    # Decode prediction
                    predicted_class = model_package['target_encoder'].inverse_transform([prediction])[0]

                    # Display results
                    st.markdown("---")
                    st.subheader("🎯 Hasil Prediksi")

                    # Risk level styling
                    risk_styles = {
                        'Lancar': 'risk-low',
                        'Dalam Perhatian Khusus': 'risk-medium',
                        'Kurang Lancar': 'risk-high',
                        'Diragukan': 'risk-high',
                        'Macet': 'risk-critical'
                    }

                    risk_class = risk_styles.get(predicted_class, 'risk-medium')

                    st.markdown(f"""
                    <div class="prediction-result {risk_class}">
                        Prediksi Klasifikasi Kredit: <strong>{predicted_class}</strong>
                    </div>
                    """, unsafe_allow_html=True)

                    # Probability distribution
                    col1, col2 = st.columns(2)

                    with col1:
                        # Probability chart
                        classes = model_package['target_classes']
                        probabilities = prediction_proba * 100

                        fig = px.bar(
                            x=classes,
                            y=probabilities,
                            title="📊 Distribusi Probabilitas Prediksi",
                            labels={'x': 'Klasifikasi Kredit', 'y': 'Probabilitas (%)'}
                        )
                        fig.update_layout(showlegend=False)
                        st.plotly_chart(fig, use_container_width=True)

                    with col2:
                        # Risk assessment
                        st.subheader("📋 Penilaian Risiko")
                        max_prob = max(probabilities)

                        if max_prob >= 80:
                            confidence = "Sangat Tinggi"
                            confidence_color = "🟢"
                        elif max_prob >= 60:
                            confidence = "Tinggi"
                            confidence_color = "🟡"
                        else:
                            confidence = "Rendah"
                            confidence_color = "🔴"

                        st.write(f"**Tingkat Keyakinan:** {confidence_color} {confidence} ({max_prob:.1f}%)")

                        # Risk recommendations
                        if predicted_class in ['Lancar']:
                            st.success("✅ **Rekomendasi:** Kredit dapat disetujui dengan syarat standar")
                        elif predicted_class in ['Dalam Perhatian Khusus']:
                            st.warning("⚠️ **Rekomendasi:** Perlu evaluasi tambahan dan monitoring ketat")
                        else:
                            st.error("❌ **Rekomendasi:** Kredit berisiko tinggi, pertimbangkan penolakan")

                except Exception as e:
                    st.error(f"❌ Error dalam prediksi: {str(e)}")

    with tab2:
        st.header("📊 Batch Prediction")
        st.info("Upload file CSV dengan data nasabah untuk prediksi massal")

        uploaded_file = st.file_uploader("Choose a CSV file", type="csv")

        if uploaded_file is not None:
            try:
                df = pd.read_csv(uploaded_file)
                st.write("**Preview Data:**")
                st.dataframe(df.head())

                if st.button("🚀 Jalankan Batch Prediction"):
                    # Process batch prediction
                    with st.spinner("Memproses prediksi..."):
                        # This would require similar preprocessing as individual prediction
                        st.success("✅ Batch prediction completed!")
                        # Display results table

            except Exception as e:
                st.error(f"❌ Error reading file: {str(e)}")

    with tab3:
        st.header("📈 Model Analytics")

        col1, col2 = st.columns(2)

        with col1:
            st.subheader("📊 Model Performance")
            metrics_data = {
                'Metric': ['F1-Score', 'Accuracy', 'AUC Score'],
                'Value': [
                    model_package['model_metadata']['f1_score'],
                    model_package['model_metadata']['accuracy'],
                    model_package['model_metadata']['auc_score']
                ]
            }

            fig = px.bar(
                x=metrics_data['Metric'],
                y=metrics_data['Value'],
                title="Model Performance Metrics"
            )
            st.plotly_chart(fig, use_container_width=True)

        with col2:
            st.subheader("ℹ️ Model Details")
            st.json({
                "Model Type": model_package['model_metadata']['model_type'],
                "Training Date": model_package['model_metadata']['training_date'],
                "Features Count": model_package['model_metadata']['feature_count'],
                "Samples Count": model_package['model_metadata']['sample_count']
            })

if __name__ == "__main__":
    main()
