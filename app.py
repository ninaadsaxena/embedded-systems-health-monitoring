from flask import Flask, render_template, jsonify
import pandas as pd

app = Flask(__name__)

@app.after_request
def add_security_headers(response):
    response.headers['Content-Security-Policy'] = "default-src 'self'"
    response.headers['X-Content-Type-Options'] = 'nosniff'
    response.headers['X-Frame-Options'] = 'DENY'
    response.headers['X-XSS-Protection'] = '1; mode=block'
    return response

@app.route('/')
def index():
    return render_template('App.js')

@app.route('/metrics')
def get_metrics():
    try:
        df = pd.read_csv('processed_metrics.csv')
        return jsonify(df.to_dict(orient='records'))
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route('/anomalies')
def get_anomalies():
    try:
        df = pd.read_csv('anomalies.csv')
        return jsonify(df.to_dict(orient='records'))
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route('/failure_predictions')
def get_failure_predictions():
    try:
        df = pd.read_csv('failure_predictions.csv')
        return jsonify(df.to_dict(orient='records'))
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run(debug=True)
