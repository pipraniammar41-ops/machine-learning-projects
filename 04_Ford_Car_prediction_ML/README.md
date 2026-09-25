# 🚗 Ford Car Price Prediction

A Machine Learning regression project focused on predicting Ford car
prices using vehicle specifications, characteristics, and categorical
information.

## 🎯 Objective

The goal of this project is to predict car prices and understand which
vehicle features are most useful for price prediction.

## 📊 Project Workflow

- Data understanding and EDA
- Duplicate detection and removal
- Data quality investigation
- Invalid value detection
- Missing value handling
- Outlier investigation
- Feature engineering
- Feature selection
- Correlation analysis
- One-hot encoding
- Train-test split
- Feature scaling using StandardScaler
- Linear Regression model training
- Model testing and prediction
- R² evaluation
- Adjusted R² evaluation
- Model improvement

## 🧹 Data Cleaning

- Removed **154 duplicate records**
- Cleaned leading spaces from categorical values
- Identified and removed an invalid year value (`2060`)
- Investigated suspicious price and mileage values
- Handled `engineSize = 0` using group-based median imputation
- Removed one record where engine size could not be reliably determined

## ⚙️ Feature Engineering

Created:

- `car_age`

Categorical features were converted using one-hot encoding:

- `model`
- `transmission`
- `fuelType`

For the final model, `year` was removed after creating `car_age` because
both contained the same information.

## 🤖 Model Used

- Linear Regression

## 📈 Model Performance

| Model | R² | Adjusted R² |
|---|---:|---:|
| Initial Model | 0.8240 | 0.8224 |
| Improved Model | **0.8367** | **0.8352** |

The improved model increased R² from approximately **0.8240 to 0.8367**
after feature engineering, feature selection, and improved preprocessing.

## 🔍 Correlation Analysis

Important numerical relationships with price included:

- `year` → positive relationship
- `mileage` → negative relationship
- `engineSize` → positive relationship
- `tax` → positive relationship
- `mpg` → negative relationship

Correlation was used to understand relationships between features and
the target, not to imply causation.

## 🧠 Concepts Practiced

- Regression
- EDA
- Data Cleaning
- Duplicate Handling
- Outlier Investigation
- Missing Value Handling
- Feature Engineering
- Feature Selection
- Correlation Analysis
- One-Hot Encoding
- StandardScaler
- Train-Test Split
- Linear Regression
- R² Score
- Adjusted R²
- Model Improvement

## 🛠️ Technologies

- Python
- NumPy
- Pandas
- Matplotlib
- Seaborn
- Scikit-learn
- Jupyter Notebook