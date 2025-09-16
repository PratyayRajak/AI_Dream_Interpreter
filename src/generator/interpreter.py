from huggingface_hub import InferenceClient
import os

# Load Hugging Face API key
HF_TOKEN = os.getenv("HUGGINGFACEHUB_API_TOKEN")

# Initialize client with your model
client = InferenceClient(
    "meta-llama/Llama-3.1-8B-Instruct",
    token=HF_TOKEN
)

def generate_dream_interpretation(dream_text: str, knowledge: str, emotion: str) -> str:
    """
    Generate dream interpretation using Hugging Face API (Llama 3.1 8B Instruct).
    """

    prompt = f"""
    You are a neuro-symbolic dream interpreter.
    Dream: {dream_text}
    Extracted symbols & knowledge: {knowledge}
    Detected emotional tone: {emotion}

    Please provide:
    1. Symbolic meaning of the dream.
    2. Psychological insights based on Jung/Freud.
    3. Practical advice for emotional well-being.
    """

    # Use conversational endpoint (chat)
    response = client.chat_completion(
        model="meta-llama/Llama-3.1-8B-Instruct",
        messages=[
            {"role": "system", "content": "You are an expert dream interpreter and psychologist."},
            {"role": "user", "content": prompt}
        ],
        max_tokens=400,
        temperature=0.7,
    )

    # HuggingFace returns structured response
    return response.choices[0].message["content"]
