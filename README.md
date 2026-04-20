# Insurance Risk Prediction Simulator

This project is a simple interactive application built to explore how lifestyle and demographic factors influence healthcare costs and risk profiles.

It combines predictive modeling with interactive visualizations to make these insights easier to understand and explore.

---

## What this app does

- Estimates annual healthcare costs using a machine learning model
- Provides a simple risk score based on key variables
- Allows users to interact with inputs and explore different scenarios
- Includes visualizations to compare individual results with the overall population

---

## Why this project

This application was created as a continuation of a more in-depth analysis.

While the original project focuses on understanding cost drivers through data analysis, this version aims to make those insights more accessible and intuitive.

---

## Model

- Random Forest Regressor  
- R² ≈ 0.86  
- Main drivers:
  - Smoking
  - BMI
  - Age  

---

## Dataset

This app uses a public dataset:

https://www.kaggle.com/datasets/mirichoi0218/insurance

The dataset is included in this repository for simplicity.

---

## Related project

This simulator is based on a full analytical project:

(cola aqui o link do seu outro projeto)

---

## Running the app

```bash
streamlit run app.py
```

---

## Requirements
streamlit
pandas
scikit-learn
joblib
plotly


## Note

This tool is intended for educational purposes.

It does not represent real insurance decision systems, but rather a simplified way to explore how different factors can influence cost and risk patterns.

## Author

Vanessa Donato
