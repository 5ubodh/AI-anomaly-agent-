import pandas as pd


def detect_anomalies(df, window=7, threshold=0.20):
    """
    Detect unusual changes in business metrics.

    window:
        Number of previous days used to calculate the baseline.

    threshold:
        Percentage difference required to flag an anomaly.
        0.20 means 20%.
    """

    metrics = [
        "Revenue",
        "Orders",
        "Conversion_Rate",
        "Traffic",
        "Cost",
        "Refunds"
    ]

    results = []

    for metric in metrics:

        # Calculate the average of previous days
        baseline = df[metric].rolling(window=window).mean().shift(1)

        # Calculate percentage change from baseline
        percentage_change = (df[metric] - baseline) / baseline

        # Check whether the change is large enough
        anomaly = percentage_change.abs() >= threshold

        for i in range(len(df)):

            if anomaly.iloc[i]:

                direction = "UP" if percentage_change.iloc[i] > 0 else "DOWN"

                results.append({
                    "Date": df["Date"].iloc[i],
                    "Metric": metric,
                    "Actual_Value": df[metric].iloc[i],
                    "Baseline": round(baseline.iloc[i], 2),
                    "Change_Percentage": round(
                        percentage_change.iloc[i] * 100, 2
                    ),
                    "Direction": direction
                })

    return pd.DataFrame(results)