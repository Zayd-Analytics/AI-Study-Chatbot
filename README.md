# 🎓 AI Study Assistant (Gemini-Powered)

A smart study buddy built with **Streamlit** and **Google Gemini AI**, designed to help students with summarization, translation, quiz generation, motivation, and personalized study tips.

---

## 🚀 Features

* **Summarize**: Convert long texts into concise bullet points.
* **Translate**: Translate text into multiple languages (Hindi, French, Spanish, German, Arabic, Urdu, Chinese).
* **Quiz Generator**: Create multiple-choice questions (MCQs) with answers from your text.
* **Motivation**: Get motivational quotes for students.
* **Personalized Tips**: Receive tailored study tips.
* **Chat Mode**: Have free-flowing conversations with the AI.

---

## 🛠️ Tech Stack

* **Frontend**: [Streamlit](https://streamlit.io/)
* **AI Model**: [Google Gemini](https://ai.google/)
* **Language**: Python
* **Environment Management**: `dotenv`

---

## 📂 Project Structure

```
ai-study-assistant/
│
├── app.py              # Main Streamlit app
├── requirements.txt    # Dependencies
├── .env                # Contains GEMINI_API_KEY
└── README.md           # Documentation
```

---

## ⚙️ Installation

1. **Clone the repository:**



2. **Create virtual environment (recommended):**

   ```bash
   python -m venv venv
   source venv/bin/activate   # On Linux/Mac
   venv\Scripts\activate      # On Windows
   ```

3. **Install dependencies:**

   ```bash
   pip install -r requirements.txt
   ```

4. **Add your Gemini API key:**

   * Create a `.env` file in the project root
   * Add the following line:

     ```env
     GEMINI_API_KEY=your_api_key_here
     ```

5. **Run the app:**

   ```bash
   streamlit run app.py
   ```

---

## 📋 Requirements

Dependencies listed in `requirements.txt`:

```
streamlit==1.26.0
google-generativeai==0.13.1
python-dotenv==1.0.0
```

✅ Note: All audio dependencies have been removed for simpler deployment.

---

## 🌍 Deployment

You can deploy this app for free on:

* [Streamlit Cloud](https://streamlit.io/cloud)
* [Render](https://render.com)
* [Railway](https://railway.app)
* [Hugging Face Spaces](https://huggingface.co/spaces)

### Example Render Settings:

* **Build Command:** `pip install -r requirements.txt`
* **Start Command:** `streamlit run app.py --server.port $PORT --server.address 0.0.0.0`

---

## 📌 Usage

1. Select **Task Mode** or **Chat Mode**.
2. If in **Task Mode**, choose from the available features (Summarize, Translate, Quiz Generator, Motivation, Personalized Tips).
3. Enter your text input.
4. Get instant AI-powered results.
5. In **Chat Mode**, talk freely with the AI.

---

## ✨ Example Use Cases

* 📘 Summarizing long notes into concise study material.
* 🌍 Translating notes into another language.
* 📝 Creating practice quizzes from textbooks.
* 💡 Getting personalized study strategies.
* 🔥 Staying motivated with daily quotes.

---

## 🤝 Contributing

Contributions are welcome! Feel free to fork this repository, make changes, and submit a pull request.

---

## 📜 License

This project is licensed under the MIT License.

---

## 💡 Author

👤 **Mohd Zayd Quadri**

📧 Contact: \[[mzq0730@gmail.com]

🌟 If you like this project, don’t forget to star the repo!
