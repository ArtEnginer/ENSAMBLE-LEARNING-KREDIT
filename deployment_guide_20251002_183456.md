
# Credit Risk Prediction Model - Deployment Guide

## Model Information
- **Model Type**: Random Forest (Hyperparameter Tuned)
- **Training Date**: 2025-10-02 18:34:56
- **Oversampling Method**: SMOTE
- **Test Accuracy**: 0.9933
- **Test F1-Weighted**: 0.9933

## Model Performance Summary
- **Best Cross-Validation Score**: 1.0
- **Test F1-Macro Score**: 0.9838
- **Total Training Samples**: 2800
- **Total Test Samples**: 300

## Required Features (13)
- PEKERJAAN
- PLAFOND
- JK_WAKTUBULAN
- KOLEKTABILITAS
- UMUR
- DAYS_SINCE_INPUT
- LOAN_TO_DURATION_RATIO
- STATUS_PERNIKAHAN_ENCODED
- PROVINSI_ENCODED
- SUB_PRODUK_ENCODED
- STATUS_ENCODED
- AGE_GROUP_ENCODED
- LOAN_CATEGORY_ENCODED

## Target Classes (5)
- Lancar
- Kurang Lancar
- Dalam Perhatian Khusus
- Macet
- Diragukan

## Best Hyperparameters
- class_weight: balanced
- max_depth: 5
- min_samples_leaf: 1
- min_samples_split: 2
- n_estimators: 100

## Usage Instructions
1. Load the model package using pickle
2. Prepare new data with the same feature structure
3. Apply the same preprocessing steps
4. Use the predict_credit_risk function
5. Interpret results based on confidence scores

## Model Files
- Main model: credit_risk_model_random_forest_20251002_183456.pkl
- Dependencies: scikit-learn, pandas, numpy, imbalanced-learn

## Notes
- Model expects scaled numerical features
- Categorical features should be encoded using the saved label encoders
- Always validate input data format before prediction
- Target predictions are automatically converted back to original labels
