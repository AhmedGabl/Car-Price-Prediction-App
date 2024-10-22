# Car Price Prediction App

## Overview
This repository contains a machine learning project for predicting used car prices based on various vehicle attributes such as model, year, fuel type, mileage, and more. It includes:
- A **Random Forest** model for regression.
- A **Tkinter-based GUI** that allows users to input car details and predict the price.

## Features
- **Model Training**: The `notebooks/usedCarPrice.ipynb` notebook demonstrates the entire pipeline from data cleaning, feature engineering, to model training using Random Forest.
- **GUI Application**: The `gui/car_price_gui.py` file creates an interactive user interface for predicting car prices based on user inputs.

## Project Structure
```bash
Car-Price-Prediction-App/
│
├── notebooks/
│   ├── usedCarPrice.ipynb          # Notebook for model training
│   ├── py.ipynb                    # Additional notebook for development
│
├── gui/
│   └── car_price_gui.py            # Tkinter GUI application
│
├── models/
│   └── car_price_model.pkl         # Trained model
│   └── label_encoders.pkl          # Label encoders for categorical features
│
├── README.md                       # This file
└── requirements.txt                # Python dependencies (if needed)
