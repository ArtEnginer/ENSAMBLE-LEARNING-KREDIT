#!/usr/bin/env python3
"""
Kredit Macet Prediction App Launcher
Simple script to start the Streamlit application
"""

import subprocess
import sys
import os

def main():
    print("Starting Kredit Macet Prediction App...")
    print("=" * 50)

    try:
        # Change to deployment directory
        os.chdir('d:\PROYEK\BU RUSDAH\ENSAMBLE-LEARNING-KREDIT\model_deployment')

        # Run streamlit app
        subprocess.run([
            sys.executable, "-m", "streamlit", "run", 
            "streamlit_app.py", 
            "--server.port=8501",
            "--server.address=0.0.0.0"
        ], check=True)

    except subprocess.CalledProcessError as e:
        print(f"Error starting app: {e}")
    except KeyboardInterrupt:
        print("\nApp stopped by user")

if __name__ == "__main__":
    main()
