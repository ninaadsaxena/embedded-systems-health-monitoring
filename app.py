from flask import Flask, render_template, jsonify
import pandas as pd

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/metrics')
def get_metrics():
    df = pd.read_csv('processed_metrics.csv')
    return jsonify(df.to_dict(orient='records'))

@app.route('/anomalies')
def get_anomalies():
    df = pd.read_csv('anomalies.csv')
    return jsonify(df.to_dict(orient='records'))

@app.route('/failure_predictions')
def get_failure_predictions():
    df = pd.read_csv('failure_predictions.csv')
    return jsonify(df.to_dict(orient='records'))

if __name__ == "__main__":
    app.run(debug=True)