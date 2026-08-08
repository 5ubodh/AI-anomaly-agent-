from src.data_loader import load_data


file_path = r"D:\vs code\AI Anomaly Agent\data\business.xlsx"

df = load_data(file_path)

print("Data loaded successfully!")
print()

print(df.head())
print()

print("Shape:", df.shape)
print()

print("Columns:")
print(df.columns.tolist())