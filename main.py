from src.data_loader import load_data
from src.anomaly_detector import detect_anomalies
from src.summarizer import generate_summary
from src.email_alert import create_email_alert, send_email


# Excel file location
file_path = "data/business_anomaly_agent_data.xlsx"


# 1. Load the data
df = load_data(file_path)

print("Data loaded successfully!")
print("=" * 50)


# 2. Detect anomalies
anomalies = detect_anomalies(df)

print("\nDetected Anomalies:")
print(anomalies)


# 3. Generate business summary
summary = generate_summary(anomalies)

print("\nBusiness Summary:")
print(summary)


# 4. Create email alert
subject, body = create_email_alert(summary)


# 5. Send email only if anomalies exist
if not anomalies.empty:
    print("\nSending email alert...")
    send_email(subject, body)
else:
    print("\nNo anomalies detected.")
    print("Email alert was not sent.")