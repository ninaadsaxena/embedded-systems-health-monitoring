import psutil
import time
import json

def collect_system_metrics():
    metrics = {
        'cpu_usage': psutil.cpu_percent(interval=1),
        'memory_usage': psutil.virtual_memory().percent,
        'disk_usage': psutil.disk_usage('/').percent,
        'network_stats': psutil.net_io_counters()._asdict()
    }
    return metrics

def save_metrics_to_file(metrics, filename='system_metrics.json'):
    with open(filename, 'a') as f:
        json.dump(metrics, f)
        f.write('\n')

if __name__ == "__main__":
    while True:
        metrics = collect_system_metrics()
        save_metrics_to_file(metrics)
        time.sleep(5)