from src.data_loader import load_data
from src.anomaly_detector import detect_anomalies

from src.summarizer import generate_summary
from src.email_alert import create_email_alert
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
summary = generate_summary(anomalies)
subject, body = create_email_alert(summary)
print("\nBusiness Summary:")
print(summary)
print("\nEmail Alert:")
print("Subject:", subject)
print(body)