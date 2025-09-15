import streamlit as st
import google.generativeai as genai
import os
from dotenv import load_dotenv

# ---------- CONFIG ----------
st.set_page_config(page_title="AI Study Assistant", page_icon="🤖", layout="wide")

# Load .env file
load_dotenv()
api_key = os.getenv("GEMINI_API_KEY")

# Configure Gemini
if not api_key:
    st.error("⚠️ GEMINI_API_KEY not found. Please set it in your .env file.")
    st.stop()
else:
    genai.configure(api_key=api_key)
    model = genai.GenerativeModel("models/gemini-2.5-flash")

# ---------- FUNCTIONS ----------
def run_ai(task, user_input, target_lang="Hindi"):
    """Run Gemini AI for the selected task"""
    if task == "Summarize":
        prompt = f"Summarize this text in 5 bullet points:\n{user_input}"
    elif task == "Translate":
        prompt = f"Translate this text into {target_lang}:\n{user_input}"
    elif task == "Quiz Generator":
        prompt = f"Generate 5 multiple-choice questions with answers from this text:\n{user_input}"
    elif task == "Motivation":
        prompt = "Give me 1 motivational quote for students"
    elif task == "Personalized Tips":
        prompt = f"Give study tips for this student:\n{user_input}"
    else:  # Chat
        prompt = user_input

    try:
        response = model.generate_content(prompt)
        return response.text
    except Exception as e:
        return f"⚠️ Error from Gemini: {e}"

# ---------- STREAMLIT UI ----------
st.title("🎓 AI Study Assistant (Gemini-Powered)")
st.write("Your smart study buddy: summarize, translate, quiz, motivate, and chat!")

mode = st.radio("Select Mode:", ["Task Mode", "Chat Mode"])

# ================= TASK MODE ==================
if mode == "Task Mode":
    task = st.selectbox(
        "Choose a feature:",
        ["Summarize", "Translate", "Quiz Generator", "Motivation", "Personalized Tips"]
    )

    # Target language selection (only for Translate)
    target_lang = "Hindi"
    if task == "Translate":
        lang_options = ["Hindi", "French", "Spanish", "German", "Arabic", "Urdu", "Chinese"]
        target_lang = st.selectbox("🌍 Select target language:", lang_options)

    user_input = st.text_area("✍️ Enter your text here:")

    if st.button("🚀 Run Assistant"):
        if not user_input.strip():
            st.warning("⚠️ Please enter text!")
        else:
            output = run_ai(task, user_input, target_lang)
            st.subheader("📌 Result:")
            st.write(output)

# ================= CHAT MODE ==================
else:
    st.subheader("💬 Chat Mode")
    if "chat_history" not in st.session_state:
        st.session_state.chat_history = []

    # Display chat history
    for msg in st.session_state.chat_history:
        st.markdown(msg)

    user_input = st.text_input("Type your message:")
    if st.button("Send"):
        if user_input.strip():
            st.session_state.chat_history.append(f"**You:** {user_input}")
            prompt = "\n".join(st.session_state.chat_history) + "\n**AI:**"
            response_text = run_ai("Chat", prompt)
            st.session_state.chat_history.append(f"**AI:** {response_text}")
            st.rerun()   # ✅ updated

