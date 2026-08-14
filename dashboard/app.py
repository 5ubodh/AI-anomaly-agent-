import sys
from pathlib import Path

import streamlit as st


# --------------------------------------------------
# Project Path
# --------------------------------------------------

PROJECT_ROOT = Path(__file__).resolve().parent.parent
sys.path.append(str(PROJECT_ROOT))

from src.data_loader import load_data
from src.anomaly_detector import detect_anomalies
from src.summarizer import generate_summary


# --------------------------------------------------
# Page Configuration
# --------------------------------------------------

st.set_page_config(
    page_title="AI Anomaly Monitor",
    page_icon="",
    layout="wide"
)


# --------------------------------------------------
# Minimal CSS
# --------------------------------------------------

st.markdown(
    """
    <style>

    .block-container {
        max-width: 1200px;
        padding-top: 3rem;
        padding-bottom: 3rem;
    }

    #MainMenu {
        visibility: hidden;
    }

    footer {
        visibility: hidden;
    }

    .title {
        font-size: 2rem;
        font-weight: 600;
        margin-bottom: 0.2rem;
    }

    .subtitle {
        color: #777;
        font-size: 0.95rem;
        margin-bottom: 2.5rem;
    }

    .metric-label {
        color: #777;
        font-size: 0.85rem;
    }

    .metric-value {
        font-size: 1.5rem;
        font-weight: 600;
        margin-top: 0.2rem;
    }

    .section {
        font-size: 1.2rem;
        font-weight: 600;
        margin-top: 2.5rem;
        margin-bottom: 1rem;
    }

    .anomaly {
        padding: 0.8rem 0;
        border-bottom: 1px solid #eeeeee;
    }

    .anomaly-name {
        font-weight: 600;
    }

    .anomaly-change {
        color: #555;
    }

    .summary {
        color: #444;
        line-height: 1.7;
    }

    </style>
    """,
    unsafe_allow_html=True
)


# --------------------------------------------------
# Load Data
# --------------------------------------------------

DATA_FILE = (
    PROJECT_ROOT
    / "data"
    / "business_anomaly_agent_data.xlsx"
)

try:

    df = load_data(DATA_FILE)

except Exception as error:

    st.error(f"Unable to load data: {error}")
    st.stop()


# --------------------------------------------------
# Analysis
# --------------------------------------------------

anomalies = detect_anomalies(df)

summary = generate_summary(anomalies)

latest = df.iloc[-1]


# --------------------------------------------------
# Header
# --------------------------------------------------

st.markdown(
    '<div class="title">AI Anomaly Monitor</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="subtitle">'
    'Business performance monitoring and anomaly detection'
    '</div>',
    unsafe_allow_html=True
)


# --------------------------------------------------
# KPI Section
# --------------------------------------------------

col1, col2, col3, col4 = st.columns(4)


with col1:

    st.markdown(
        '<div class="metric-label">Revenue</div>',
        unsafe_allow_html=True
    )

    st.markdown(
        f'<div class="metric-value">Rs. {latest["Revenue"]:,.0f}</div>',
        unsafe_allow_html=True
    )


with col2:

    st.markdown(
        '<div class="metric-label">Orders</div>',
        unsafe_allow_html=True
    )

    st.markdown(
        f'<div class="metric-value">{latest["Orders"]:,.0f}</div>',
        unsafe_allow_html=True
    )


with col3:

    st.markdown(
        '<div class="metric-label">Traffic</div>',
        unsafe_allow_html=True
    )

    st.markdown(
        f'<div class="metric-value">{latest["Traffic"]:,.0f}</div>',
        unsafe_allow_html=True
    )


with col4:

    st.markdown(
        '<div class="metric-label">Conversion Rate</div>',
        unsafe_allow_html=True
    )

    st.markdown(
        f'<div class="metric-value">{latest["Conversion_Rate"]:.2f}%</div>',
        unsafe_allow_html=True
    )


# --------------------------------------------------
# Performance
# --------------------------------------------------

st.markdown(
    '<div class="section">Performance</div>',
    unsafe_allow_html=True
)


chart1, chart2 = st.columns(2)


with chart1:

    st.caption("Revenue")

    revenue = df.set_index("Date")[["Revenue"]]

    st.line_chart(revenue)


with chart2:

    st.caption("Traffic")

    traffic = df.set_index("Date")[["Traffic"]]

    st.line_chart(traffic)


# --------------------------------------------------
# Anomalies
# --------------------------------------------------
# --------------------------------------------------
# Anomalies
# --------------------------------------------------

st.markdown(
    '<div class="section">Anomalies</div>',
    unsafe_allow_html=True
)

if anomalies.empty:

    st.write("No significant anomalies detected.")

else:

    st.write(
        f"{len(anomalies)} unusual changes detected."
    )

    for _, anomaly in anomalies.iterrows():

        metric = anomaly["Metric"]
        change = anomaly["Change_Percentage"]
        actual = anomaly["Actual_Value"]
        baseline = anomaly["Baseline"]
        date = anomaly["Date"].strftime("%Y-%m-%d")

        if change < 0:
            direction = "↓"
        else:
            direction = "↑"

        col1, col2, col3 = st.columns([2, 1, 3])

        with col1:
            st.write(f"**{metric}**")

        with col2:
            st.write(f"{direction} {abs(change):.2f}%")

        with col3:
            st.caption(
                f"{date} · Actual: {actual:.2f} · Baseline: {baseline:.2f}"
            )

# --------------------------------------------------
# Business Summary
# --------------------------------------------------

st.markdown(
    '<div class="section">Business Summary</div>',
    unsafe_allow_html=True
)

st.markdown(
    f'<div class="summary">{summary.replace(chr(10), "<br>")}</div>',
    unsafe_allow_html=True
)


# --------------------------------------------------
# Detailed Data
# --------------------------------------------------

with st.expander("View data"):

    st.dataframe(
        df,
        use_container_width=True,
        hide_index=True
    )