from src.data_loader import load_data
from src.anomaly_detector import detect_anomalies


file_path = "data/business_anomaly_agent_data.xlsx"


# Load the Excel data
df = load_data(file_path)

print("Data loaded successfully!")
print()


# Detect anomalies
anomalies = detect_anomalies(df)


print("ANOMALIES DETECTED:")
print()

print(anomalies)