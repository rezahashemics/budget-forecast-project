# app/models/algorithms.py
from sklearn.linear_model import LinearRegression
from sklearn.ensemble import RandomForestRegressor
from sklearn.preprocessing import MinMaxScaler
import numpy as np

class BudgetProcessingLayer:
    def __init__(self):
        self.lr = LinearRegression()
        self.rf = RandomForestRegressor(n_estimators=100)
        self.scaler = MinMaxScaler()

    def preprocess(self, df):
        # Feature Engineering: Lagged values (Page 14)
        df['target'] = df['BALANCE AMT']
        df['lag_1'] = df['BALANCE AMT'].shift(1)
        df = df.dropna()
        X = df[['lag_1', 'WITHDRAWAL AMT', 'DEPOSIT AMT']]
        y = df['target']
        return X, y

    def train_models(self, X, y):
        self.lr.fit(X, y)
        self.rf.fit(X, y)

    def get_predictions(self, X):
        return {
            "LinearRegression": self.lr.predict(X),
            "RandomForest": self.rf.predict(X)
        }
