import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from storage.db import fetch_dreams

def show_dashboard():
    st.markdown("<h1>📊 Dream Journal Dashboard</h1>", unsafe_allow_html=True)
    st.markdown("✨ Track your dream patterns, emotions, and insights over time 🌌")

    dreams = fetch_dreams()
    if not dreams:
        st.info("😴 No dreams saved yet. Record your first dream on the Home page.")
        return

    df = pd.DataFrame(dreams, columns=["ID", "Dream", "Emotion", "Interpretation", "Timestamp"])

    # --- Stats Cards ---
    col1, col2, col3 = st.columns(3)
    with col1:
        st.markdown(f"<div class='metric-card'><h2>{len(df)}</h2><p>Total Dreams</p></div>", unsafe_allow_html=True)
    with col2:
        common_emotion = df["Emotion"].mode()[0]
        st.markdown(f"<div class='metric-card'><h2>{common_emotion}</h2><p>Most Common Emotion</p></div>", unsafe_allow_html=True)
    with col3:
        st.markdown(f"<div class='metric-card'><h2>{df['Timestamp'].min().split()[0]}</h2><p>First Dream Logged</p></div>", unsafe_allow_html=True)

    # --- Past Dreams Table ---
    st.subheader("📝 Past Dreams")
    st.dataframe(df[["Timestamp", "Dream", "Emotion", "Interpretation"]], use_container_width=True)

    # --- Emotion Trends Chart ---
    st.subheader("📈 Emotion Trends Over Time")
    plt.figure(figsize=(8,4))
    df_sorted = df.sort_values("Timestamp")
    plt.plot(df_sorted["Timestamp"], df_sorted["Emotion"], marker="o", linestyle="--", color="gold")
    plt.xticks(rotation=45, ha="right")
    plt.ylabel("Emotion")
    plt.title("Dream Emotions Timeline")
    st.pyplot(plt)
