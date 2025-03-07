from sklearn.linear_model import LinearRegression
import pandas as pd

def train_predictive_model(df):
    X = df[['cpu_usage', 'memory_usage', 'disk_usage']]
    y = df['failure']
    model = LinearRegression()
    model.fit(X, y)
    return model

def predict_failures(model, df):
    df['failure_prediction'] = model.predict(df[['cpu_usage', 'memory_usage', 'disk_usage']])
    return df

if __name__ == "__main__":
    df = pd.read_csv('processed_metrics.csv')
    model = train_predictive_model(df)
    predictions = predict_failures(model, df)
    predictions.to_csv('failure_predictions.csv')
    print(predictions[predictions['failure_prediction'] > 0.5])
