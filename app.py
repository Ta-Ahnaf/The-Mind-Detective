import streamlit as st
from transformers import AutoTokenizer, AutoModelForSequenceClassification
import torch
import torch.nn.functional as F
from emotion_resources import get_random_resource  # Import the function from your resources file

# ---------------------- Model Loading ----------------------
HF_MODEL_REPO = "TA-AHNAF/Emotion_Detector_GOEMOTION"

@st.cache_resource
def load_model():
    tokenizer = AutoTokenizer.from_pretrained(HF_MODEL_REPO)
    model = AutoModelForSequenceClassification.from_pretrained(HF_MODEL_REPO)
    model.eval()
    return tokenizer, model

tokenizer, model = load_model()

# ---------------------- Emotion Data ----------------------
emotions = [
    "admiration", "amusement", "anger", "annoyance", "approval", "caring",
    "confusion", "curiosity", "desire", "disappointment", "disapproval",
    "disgust", "embarrassment", "excitement", "fear", "gratitude", "grief",
    "joy", "love", "nervousness", "optimism", "pride", "realization",
    "relief", "remorse", "sadness", "surprise", "neutral"
]

colors = {
    "anger": "#FF4C4C", "joy": "#FFD93D", "sadness": "#4D79FF", "neutral": "#A6A6A6"
}

emojis = {
    "anger": "😡", "joy": "😄", "sadness": "😢", "neutral": "😐"
}

# ---------------------- Streamlit Layout ----------------------
st.set_page_config(page_title="Emotion Detector", page_icon="🧠", layout="centered")

st.markdown("""
    <style>
        .card {
            background-color: #ffffff;
            padding: 25px;
            border-radius: 12px;
            box-shadow: 0 4px 12px rgba(0,0,0,0.08);
            margin-top: 20px;
            text-align: center;
        }
        .confidence-bar {
            height: 18px;
            border-radius: 9px;
            background-color: #e0e0e0;
            overflow: hidden;
            margin: 10px 0;
        }
        .confidence-fill {
            height: 100%;
            color: white;
            line-height: 18px;
        }
        .stButton>button {
            background-color: #4D79FF;
            color: white;
            border-radius: 8px;
            padding: 8px 20px;
            font-weight: bold;
        }
        .stTextArea>div>textarea {
            border-radius: 8px;
        }
        .suggestion-text {
            color: black;
        }
        .quote-text {
            color: gray;
            font-size: 20px;
            font-style: italic;
            margin-top: 20px;
        }
        .all-rights {
            text-align: center;
            font-size: 14px;
            color: gray;
            position: fixed;
            bottom: 0;
            left: 50%;
            transform: translateX(-50%);
            background: none;
        }
        body {
            margin-bottom: 60px; /* space for footer */
        }
        .disclaimer {
            font-size: 12px;
            color: gray;
            margin-top: 10px;
        }
    </style>
""", unsafe_allow_html=True)

st.title("🧠 The-Mind-Detective 🎩")
st.write("Type your thoughts below and let AI detect your **emotion**.")

user_input = st.text_area("Enter your text here:")

if st.button("Detect Emotion"):
    if user_input.strip():
        # ---------------------- Prediction ----------------------
        inputs = tokenizer(user_input, return_tensors="pt")
        with torch.no_grad():
            outputs = model(**inputs)
            probs = F.softmax(outputs.logits, dim=-1)
            predicted_idx = torch.argmax(probs, dim=1).item()
            confidence = probs[0][predicted_idx].item()

        predicted_emotion = emotions[predicted_idx]
        color = colors.get(predicted_emotion, "#4D79FF")
        emoji = emojis.get(predicted_emotion, "✨")

        # ---------------------- Random Resources ----------------------
        resources = get_random_resource(predicted_emotion)
        quote = resources.get("quote", "Embrace your emotions.")
        activity = resources.get("activity", "Do something you enjoy.")
        game = resources.get("game")
        book = resources.get("book")
        movie = resources.get("movie")

        # ---------------------- Display Card ----------------------
        st.markdown(f"""
            <div class="card" style="border-left: 6px solid {color};">
                <h2 style="color: {color};">{emoji} <b>{predicted_emotion.capitalize()}</b> {emoji}</h2>
                <div class="confidence-bar">
                    <div class="confidence-fill" style="width: {confidence*100}%; background-color: {color};">
                        {confidence*100:.1f}%
                    </div>
                </div>
                <p class="suggestion-text">Suggested activity: <b>{activity}</b></p>
                {"<p class='suggestion-text'>Game recommendation: <b>" + game + "</b></p>" if game else ""}
                {"<p class='suggestion-text'>Book recommendation: <b>" + book + "</b></p>" if book else ""}
                {"<p class='suggestion-text'>Movie recommendation: <b>" + movie + "</b></p>" if movie else ""}
                <p class="quote-text">"{quote}"</p>
                <p class="disclaimer">⚠️ This tool may fail to detect certain subtle emotions accurately.</p>
            </div>
        """, unsafe_allow_html=True)
    else:
        st.warning("⚠️ Please enter some text to analyze.")

# Footer
st.markdown('<p class="all-rights">All rights reserved © MD. Tahmid Ahnaf</p>', unsafe_allow_html=True)
