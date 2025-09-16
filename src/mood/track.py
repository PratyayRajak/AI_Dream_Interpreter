from transformers import pipeline

# Load Hugging Face emotion analysis pipeline
emotion_classifier = pipeline("text-classification", model="j-hartmann/emotion-english-distilroberta-base", top_k=1)

def analyze_emotion(text: str) -> str:
    """
    Analyze the dominant emotion in the given text using a transformer model.
    Returns the emotion label (e.g., joy, sadness, fear, anger, love, etc.).
    """
    if not text.strip():
        return "neutral"

    try:
        results = emotion_classifier(text)
        # results is like [[{'label': 'joy', 'score': 0.87}]]
        return results[0][0]['label']
    except Exception as e:
        print("Emotion analysis error:", e)
        return "unknown"
