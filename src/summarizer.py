def generate_summary(anomalies):
    """
    Convert detected anomalies into a business-friendly summary.
    """

    if anomalies.empty:
        return "No significant anomalies were detected."

    summaries = []

    for _, anomaly in anomalies.iterrows():

        metric = anomaly["Metric"]
        change = anomaly["Change_Percentage"]
        direction = anomaly["Direction"]

        if direction == "UP":
            movement = "increased"
        else:
            movement = "decreased"

        summary = (
            f"{metric} {movement} by "
            f"{abs(change):.2f}% compared with its recent baseline."
        )

        summaries.append(summary)

    return "\n".join(summaries)