import os
import pickle
import joblib
import json
from pathlib import Path
from datetime import datetime


# Script untuk menyimpan model yang telah di-tuning
def save_model_package():
    print("💾 MENYIMPAN MODEL TERBAIK UNTUK PRODUCTION")
    print("=" * 70)

    # Create models directory
    models_dir = Path("models")
    models_dir.mkdir(exist_ok=True)

    # Create timestamp for file naming
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")

    print(f"📁 Created/verified models directory: {models_dir.absolute()}")

    return models_dir, timestamp


if __name__ == "__main__":
    save_model_package()
