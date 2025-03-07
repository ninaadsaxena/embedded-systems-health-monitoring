import json
import pandas as pd

def load_metrics_from_file(filename='system_metrics.json'):
    data = []
    with open(filename, 'r') as f:
        for line in f:
            data.append(json.loads(line))
    return pd.DataFrame(data)

def process_data(df):
    df['timestamp'] = pd.to_datetime(df['timestamp'])
    df.set_index('timestamp', inplace=True)
    return df

if __name__ == "__main__":
    df = load_metrics_from_file()
    processed_df = process_data(df)
    processed_df.to_csv('processed_metrics.csv')
    print(processed_df.head())