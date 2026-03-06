# Production-Ready Missing Data Imputation and Churn Prediction Pipeline

## Overview
This project demonstrates a production-oriented machine learning pipeline for handling missing data and evaluating how imputation strategies affect downstream predictive performance.

The project compares multiple imputation strategies including statistical, neighbour-based, iterative, and machine-learning-based approaches.

**System Architecture**
User/Data Upload
        │
        ▼
     API Layer (Flask)
        │
        ▼
   Data Loader
        │
        ▼
   Preprocessing
        │
        ▼
   Imputation Methods
   ├─ Median
   ├─ KNN
   ├─ MICE
   └─ Random Forest
        │
        ▼
   Evaluation Metrics
   ├─ MAPE
   ├─ RMSPE
   └─ F1 Score


## Dataset
Telco Customer Churn Dataset

Rows: 7,043  
Features: 21  
Mixed numerical and categorical data.

## Imputation Methods Compared
- Median / Mode
- KNN Imputation
- MICE (Multiple Imputation by Chained Equations)
- Random Forest Custom Imputer
- XGBoost Imputer
- Neural Network Imputer

## Evaluation Metrics
Reconstruction Quality:
- Mean Absolute Percentage Error (MAPE)
- Root Mean Square Percentage Error (RMSPE)
- Categorical Reconstruction Accuracy

Predictive Performance:
- Logistic Regression Accuracy
- F1 Score

## Key Findings
Random Forest based imputation achieved the strongest overall performance across missingness levels (2%, 5%, and 10%), providing the lowest reconstruction error and strongest predictive stability.

## Tech Stack
Python  
Pandas  
NumPy  
Scikit-learn  
XGBoost  
Matplotlib  

## Future Work
- Validation dataset experiment
- MLOps pipeline with CI/CD
- API deployment
- Cloud containerisation
