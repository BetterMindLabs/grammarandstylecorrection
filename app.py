import streamlit as st
import google.generativeai as genai

# === Gemini API Setup ===
api_key = st.secrets["api_keys"]["google_api_key"]
genai.configure(api_key=api_key)
model = genai.GenerativeModel("gemini-1.5-flash")

# === Streamlit UI ===
st.set_page_config(page_title="✍️ Grammar & Style Corrector")
st.title("✍️ Grammar and Style Correction")
st.write("Paste your text and receive a refined version with improved grammar, punctuation, and flow.")

# === Text Input ===
user_text = st.text_area("📝 Enter Your Text", height=250, placeholder="e.g. This are very good idea for student who want go college.")

# === Correct Button ===
if st.button("Correct Text") and user_text.strip():
    with st.spinner("Refining your text..."):
        prompt = f"""
Correct the following text for grammar, punctuation, sentence structure, and style. Do not change the original meaning. Return only the corrected version.

Text:
{user_text}
"""

        response = model.generate_content(prompt)
        corrected_text = response.text.strip()

        st.subheader("✅ Corrected Text")
        st.text_area("Result", corrected_text, height=250)
