# Script untuk menyimpan model hasil hyperparameter tuning
# Jalankan setelah menjalankan notebook sampai hyperparameter tuning

import os
import joblib
import json
from pathlib import Path
from datetime import datetime


def save_tuned_model():
    """
    Menyimpan model yang telah di-tuning beserta preprocessing objects
    """
    print("💾 MENYIMPAN MODEL TERBAIK UNTUK PRODUCTION")
    print("=" * 70)

    # Create models directory
    models_dir = Path("models")
    models_dir.mkdir(exist_ok=True)

    # Create timestamp for file naming
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")

    print(f"📁 Created/verified models directory: {models_dir.absolute()}")

    # Informasi yang akan disimpan - sesuaikan dengan hasil dari notebook
    # Anda perlu menjalankan notebook sampai hyperparameter tuning selesai

    print("📋 To use this script:")
    print("1. Run notebook until hyperparameter tuning is complete")
    print("2. Execute the following code in notebook to save the model:")

    save_code = """
import os
import joblib
import json
from pathlib import Path
from datetime import datetime

# Create models directory
models_dir = Path("models")
models_dir.mkdir(exist_ok=True)
timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")

# Save model
model_filename = f"best_model_{best_model_name.lower().replace(' ', '_')}_{timestamp}.joblib"
joblib.dump(final_model, models_dir / model_filename)

# Save preprocessing objects
scaler_filename = f"scaler_{timestamp}.joblib"
joblib.dump(scaler, models_dir / scaler_filename)

label_encoders_filename = f"label_encoders_{timestamp}.joblib"
joblib.dump(label_encoders, models_dir / label_encoders_filename)

target_encoder_filename = f"target_encoder_{timestamp}.joblib"
joblib.dump(target_encoder, models_dir / target_encoder_filename)

# Save metadata
metadata = {
    "model_info": {
        "model_name": best_model_name,
        "training_timestamp": timestamp,
        "dataset_used": best_combo['Dataset'] if 'best_combo' in locals() else 'Original'
    },
    "performance_metrics": {
        "cv_score": tuned_results_df.iloc[0]['CV_Score'] if 'tuned_results_df' in locals() else None,
        "test_accuracy": tuned_results_df.iloc[0]['Accuracy'] if 'tuned_results_df' in locals() else None,
        "test_f1_weighted": tuned_results_df.iloc[0]['F1_Weighted'] if 'tuned_results_df' in locals() else None
    },
    "feature_info": {
        "feature_names": feature_names,
        "categorical_features": [
            'STATUS_PERNIKAHAN', 'PRODUK', 'SUB_PRODUK',
            'HASIL_PRESCREENING_SLIK', 'HASIL_PRESCREENING_SIKPKUR',
            'HASIL_PRESCREENING_DUKCAPIL', 'HASIL_PRESCREENING_DHNBI',
            'HASIL_PRESCREENING_1', 'STATUS'
        ]
    },
    "target_info": {
        "target_classes": target_encoder.classes_.tolist(),
        "class_labels": {1: "Lancar", 2: "Dalam Perhatian Khusus", 3: "Kurang Lancar", 4: "Diragukan", 5: "Macet"}
    },
    "file_references": {
        "model_file": model_filename,
        "scaler_file": scaler_filename,
        "label_encoders_file": label_encoders_filename,
        "target_encoder_file": target_encoder_filename
    }
}

metadata_filename = f"model_metadata_{timestamp}.json"
with open(models_dir / metadata_filename, 'w', encoding='utf-8') as f:
    json.dump(metadata, f, indent=2, ensure_ascii=False)

print(f"✅ Model package saved successfully!")
print(f"📁 Location: {models_dir.absolute()}")
print(f"📄 Files: {model_filename}, {scaler_filename}, {label_encoders_filename}, {target_encoder_filename}, {metadata_filename}")
"""

    print("\n" + "=" * 50)
    print("COPY AND PASTE THIS CODE IN NOTEBOOK:")
    print("=" * 50)
    print(save_code)
    print("=" * 50)


if __name__ == "__main__":
    save_tuned_model()
