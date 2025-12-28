# app/security/protector.py
from cryptography.fernet import Fernet
from sklearn.ensemble import IsolationForest
import pandas as pd

class SecurityLayer:
    def __init__(self):
        # AES-256 Symmetric Key
        self.key = Fernet.generate_key()
        self.cipher = Fernet(self.key)

    def encrypt_sensitive_data(self, value):
        return self.cipher.encrypt(str(value).encode())

    def run_fraud_detection(self, df):
        """Anomaly Detection as per Page 13 of PDF"""
        model = IsolationForest(contamination=0.01, random_state=42)
        df['anomaly_score'] = model.fit_predict(df[['WITHDRAWAL AMT', 'DEPOSIT AMT']])
        return df
