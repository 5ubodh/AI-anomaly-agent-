def create_email_alert(summary):
    """
    Create an email alert message from the anomaly summary.
    """

    subject = "AI Anomaly Agent - Business Alert"

    body = f"""
Hello,

The AI Anomaly Agent detected unusual changes in your business data.

ANOMALY SUMMARY
---------------
{summary}

Please review the affected metrics and investigate the possible cause.

This is an automated alert from the AI Anomaly Agent.
"""

    return subject, body