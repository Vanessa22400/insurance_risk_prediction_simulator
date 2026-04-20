# Insurance Risk Prediction Simulator

This project is a simple interactive application built to explore how lifestyle and demographic factors influence healthcare costs and risk profiles.

It is based on a broader data analysis project, but here the focus is different: instead of looking at the data from a technical perspective, the goal is to make these insights more accessible and intuitive to interact with.

The idea is to allow someone to explore different scenarios and better understand how factors such as smoking, BMI and age can impact long-term outcomes.

---

## What this app does

- Estimates annual healthcare costs using a machine learning model
- Provides a simple risk score based on key variables
- Allows users to interact with inputs and explore different profiles
- Translates analytical results into a more intuitive format

---

## Why this project

This application was created as a continuation of a more in-depth analysis.

While the original project focuses on understanding cost drivers and risk patterns through data analysis and modeling, this version aims to make those insights easier to visualize and interact with.

It also reflects an interest in going beyond analysis, building something closer to a real-world application.

---

## Model

- Random Forest Regressor  
- R² ≈ 0.86  
- Main drivers identified:
  - Smoking
  - BMI
  - Age  

---

## Related project

This simulator is based on the following project:

Insurance Risk Analytics: Cost Drivers, Risk Segmentation and Predictive Modeling  
(you can add the GitHub link here)

The original project includes:
- Exploratory Data Analysis
- Risk segmentation
- Clustering (K-Means)
- Causal inference (Propensity Score Matching)
- Predictive modeling (regression and classification)

---

## Running the app

```bash
streamlit run app.py

---

## Requirements
streamlit
pandas
scikit-learn
joblib


## Note

This tool is intended for educational purposes.

It does not represent real insurance decision systems, but rather a simplified way to explore how different factors can influence cost and risk patterns.

## Author

Vanessa Donato
