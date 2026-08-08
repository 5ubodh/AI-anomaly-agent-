import pandas as pd
from pathlib import Path


def load_data(file_path):
   

    path = Path(r"D:\vs code\AI Anomaly Agent\data\business.xlsx")

    if not path.exists():
        raise FileNotFoundError(f"File not found: {path}")

    df = pd.read_excel(path)

    required_columns = [
        "Date",
        "Revenue",
        "Orders",
        "Conversion_Rate",
        "Traffic",
        "Cost",
        "Refunds"
    ]

    missing_columns = [
        column for column in required_columns
        if column not in df.columns
    ]

    if missing_columns:
        raise ValueError(f"Missing columns: {missing_columns}")

    df["Date"] = pd.to_datetime(df["Date"])

    df = df.sort_values("Date").reset_index(drop=True)

    return df