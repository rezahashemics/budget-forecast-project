# app/controller.py
import pandas as pd
from app.models.algorithms import BudgetProcessingLayer
from app.security.protector import SecurityLayer
from app.views.dashboard import render_ui

def start_system(csv_path):
    # 1. Data Ingestion
    df = pd.read_csv(csv_path)
    df['DATE'] = pd.to_datetime(df['DATE'])
    
    # 2. Security Layer
    sec = SecurityLayer()
    df = sec.run_fraud_detection(df)
    
    # 3. Processing Layer
    ml = BudgetProcessingLayer()
    X, y = ml.preprocess(df)
    ml.train_models(X, y)
    preds = ml.get_predictions(X)
    
    # 4. Decision Layer (Pass sliced df to match X's length)
    render_ui(df.iloc[1:], preds)

if __name__ == "__main__":
    start_system('bank.xlsx - Sheet1.csv')
