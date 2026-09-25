# 🏥 Insurance Cost Prediction

A Machine Learning regression project focused on predicting medical
insurance charges using customer demographic, lifestyle, and regional
information.

## 🎯 Objective

The goal of this project is to predict insurance charges and understand
which features have a stronger relationship with insurance costs.

## 📊 Project Workflow

- Data loading and understanding
- Exploratory Data Analysis (EDA)
- Missing value analysis
- Duplicate detection and removal
- Numerical and categorical feature analysis
- Distribution and outlier analysis
- Correlation analysis
- Categorical feature encoding
- Feature engineering
- BMI category creation
- Feature scaling using StandardScaler
- Pearson correlation analysis
- Train-test split
- Linear Regression model training
- Model testing and prediction
- R² evaluation
- Adjusted R² evaluation

## ⚙️ Feature Engineering

Created additional features including:

- `is_female`
- `is_smoker`
- BMI categories:
  - Normal
  - Overweight
  - Obese

Categorical region and BMI features were converted into numerical
features using one-hot encoding.

## 🤖 Model Used

- Linear Regression

## 📈 Model Performance

- **R² Score:** 0.805
- **Adjusted R²:** 0.796

The model was evaluated on the test dataset using R² and Adjusted R².

## 🔍 Correlation Analysis

Pearson correlation was used to examine the relationship between individual
features and insurance charges.

Among the analyzed features, `is_smoker` showed the strongest positive
Pearson correlation with insurance charges in this dataset.

## 🧠 Concepts Practiced

- Regression
- EDA
- Data Cleaning
- Duplicate Handling
- Categorical Encoding
- One-Hot Encoding
- Feature Engineering
- Feature Scaling
- StandardScaler
- Pearson Correlation
- Train-Test Split
- Linear Regression
- R² Score
- Adjusted R²

## 🛠️ Technologies

- Python
- NumPy
- Pandas
- Matplotlib
- Seaborn
- Scikit-learn
- SciPy
- Jupyter Notebook