import streamlit as st
from mood.track import analyze_emotion
from nlp.extract import extract_psych_symbols
from generator.interpreter import generate_dream_interpretation
from storage.db import save_dream
from visualization.dashboard import show_dashboard

# --- Custom Styling ---
def apply_custom_css():
    st.markdown("""
    <style>
        .stApp {
            background: linear-gradient(135deg, #1e3c72, #2a5298);
            color: white;
            font-family: 'Trebuchet MS', sans-serif;
        }
        h1, h2, h3 {
            color: #FFD700 !important;
        }
        section[data-testid="stSidebar"] {
            background: linear-gradient(to bottom, #2c5364, #203a43, #0f2027);
            color: white;
        }
        button[kind="secondary"] {
            background: linear-gradient(45deg, #ff6a00, #ee0979) !important;
            color: white !important;
            border-radius: 12px !important;
            font-size: 16px !important;
        }
        .metric-card {
            padding: 20px;
            border-radius: 12px;
            background: #222831;
            color: white;
            text-align: center;
            box-shadow: 0 4px 15px rgba(0,0,0,0.3);
        }
    </style>
    """, unsafe_allow_html=True)

# --- Main App ---
def main():
    apply_custom_css()
    st.sidebar.title("🌙 Dream Navigation")
    page = st.sidebar.radio("Go to:", ["Home", "Dashboard"])

    if page == "Home":
        st.markdown("<h1>🌙 AI Dream Interpreter</h1>", unsafe_allow_html=True)
        st.markdown("#### ✨ Unlock the hidden meaning of your dreams with **AI-powered psychology** 🧠💫")

        dream_input = st.text_area("💭 Describe your dream:", height=150, placeholder="I was walking in a forest and saw a glowing door...")

        if st.button("🔮 Interpret My Dream"):
            if dream_input.strip():
                # 1. Emotion Analysis
                emotion_label = analyze_emotion(dream_input)

                # 2. Extract dream symbols
                symbols = extract_psych_symbols(dream_input)

                # 3. Generate interpretation (via Hugging Face LLaMA or other model)
                interpretation = generate_dream_interpretation(dream_input, symbols, emotion_label)

                # 4. Save dream to DB
                save_dream(dream_input, emotion_label, interpretation)

                # --- Display Results ---
                st.success(f"**Emotion Detected:** {emotion_label}")
                st.info(f"**Dream Symbols Identified:** {', '.join(symbols) if symbols else 'None'}")
                st.markdown("### 🌌 Dream Interpretation")
                st.write(interpretation)
            else:
                st.warning("⚠️ Please enter a dream first!")

    elif page == "Dashboard":
        show_dashboard()


if __name__ == "__main__":
    from storage.db import init_db
    init_db()
    main()
