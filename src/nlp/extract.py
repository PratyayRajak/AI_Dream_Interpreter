# src/nlp/extract.py

from transformers import pipeline

# Load Hugging Face NER pipeline
ner_model = pipeline("ner", model="dslim/bert-base-NER", grouped_entities=True)

# Mini psychological knowledge base
psych_kb = {
    "water": "emotions, subconscious mind",
    "snake": "hidden fears, transformation",
    "flying": "freedom, ambition",
    "death": "transition, change",
    "tree": "growth, stability, family roots",
    "house": "self, identity, personal life",
    "road": "life path, choices, direction",
    "child": "innocence, potential, vulnerability",
    "river": "emotional flow, change",
    "darkness": "uncertainty, hidden fears"
}

def extract_psych_symbols(dream_text: str):
    """
    Extract dream symbols using transformer-based NER
    + match them against psychology knowledge base.
    """
    detected = set()

    # Run NER
    entities = ner_model(dream_text)

    for ent in entities:
        word = ent['word'].lower()
        if word in psych_kb:
            detected.add(word)

    # Extra fallback: keyword match in dream text
    for keyword in psych_kb.keys():
        if keyword in dream_text.lower():
            detected.add(keyword)

    return list(detected)
