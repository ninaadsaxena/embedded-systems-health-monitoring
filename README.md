# Embedded Systems Health Monitoring Tool

## Description
This project is an Embedded Systems Health Monitoring Tool that uses AI to detect and diagnose issues in real-time. It analyzes system logs, performance metrics, and sensor data to identify anomalies and predict failures.

## Key Features
- Real-time monitoring and alerting
- AI-based anomaly detection
- Predictive maintenance suggestions
- Integration with existing diagnostic tools

## Technology Stack
- **Languages:** Python, C++
- **Libraries:** TensorFlow/Keras (for AI models), scikit-learn (for data processing), pandas (for data analysis)
- **Tools:** Windbg (for debugging), git (for version control)
- **Frameworks:** Flask (for the web interface), Celery (for task scheduling)

## Project Structure
- `data_collection.py`: Collects system metrics and saves them to a file.
- `data_processing.py`: Loads and processes the collected metrics.
- `anomaly_detection.py`: Detects anomalies in the processed metrics.
- `predictive_maintenance.py`: Predicts potential failures and suggests maintenance actions.
- `app.py`: Flask web server to display metrics, anomalies, and failure predictions.
- `templates/index.html`: HTML template for the web interface.
- `README.md`: Project documentation.

## Installation
1. Clone the repository:
    ```bash
    git clone <repository-url>
    ```
2. Navigate to the project directory:
    ```bash
    cd <project-directory>
    ```
3. Install the required dependencies:
    ```bash
    pip install -r requirements.txt
    ```

## Usage
1. Run the data collection module:
    ```bash
    python data_collection.py
    ```
2. Run the data processing module:
    ```bash
    python data_processing.py
    ```
3. Run the anomaly detection module:
    ```bash
    python anomaly_detection.py
    ```
4. Run the predictive maintenance module:
    ```bash
    python predictive_maintenance.py
    ```
5. Start the Flask web server:
    ```bash
    python app.py
    ```
6. Open the web interface in your browser:
    ```
    http://127.0.0.1:5000/
    ```

## License
This project is licensed under the MIT License.