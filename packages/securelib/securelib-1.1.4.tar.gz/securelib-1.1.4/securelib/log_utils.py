def monitor_logs(file_path: str) -> list:
    alerts = []
    with open(file_path, 'r') as file:
        for line in file:
            if "ERROR" in line:
                alerts.append(line.strip())
    return alerts
