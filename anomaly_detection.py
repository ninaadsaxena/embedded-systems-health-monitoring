from sklearn.ensemble import IsolationForest
import pandas as pd

def train_anomaly_detector(df):
    model = IsolationForest(contamination=0.1)
    model.fit(df)
    return model

def detect_anomalies(model, df):
    df['anomaly'] = model.predict(df)
    return df

if __name__ == "__main__":
    df = pd.read_csv('processed_metrics.csv')
    model = train_anomaly_detector(df)
    anomalies = detect_anomalies(model, df)
    anomalies.to_csv('anomalies.csv')
    print(anomalies[anomalies['anomaly'] == -1])