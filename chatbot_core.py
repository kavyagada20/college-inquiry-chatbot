import os
import pickle
import spacy
import pandas as pd
from sklearn.metrics.pairwise import cosine_similarity

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

MODEL_DIR = os.path.join(BASE_DIR, "models")
INTENT_MODEL_PATH = os.path.join(MODEL_DIR, "intent_model.pkl")
VECTORIZER_PATH = os.path.join(MODEL_DIR, "vectorizer.pkl")

# Load ML artifacts safely
intent_model = None
vectorizer = None

if os.path.exists(INTENT_MODEL_PATH) and os.path.exists(VECTORIZER_PATH):
    intent_model = pickle.load(open(INTENT_MODEL_PATH, "rb"))
    vectorizer = pickle.load(open(VECTORIZER_PATH, "rb"))
else:
    print("⚠️ ML model files not found. Running in fallback mode.")

# Load spaCy model safely
try:
    nlp = spacy.load("en_core_web_sm")
except Exception:
    nlp = None
    print("⚠️ spaCy model not available.")

# Load FAQ data
faq_path = os.path.join(BASE_DIR, "faq_data.csv")
faq_data = pd.read_csv(faq_path)


def predict_intent(user_input):
    if intent_model is None or vectorizer is None:
        return "general_query"
    X = vectorizer.transform([user_input])
    return intent_model.predict(X)[0]

def extract_entities(user_input):
    if nlp is None:
        return []
    doc = nlp(user_input)
    return [(ent.text, ent.label_) for ent in doc.ents]

def retrieve_response(user_input, intent):
    # Filter FAQs with same intent
    subset = faq_data[faq_data['intent'] == intent]

    # Use TF-IDF + cosine similarity to find closest question
    user_vec = vectorizer.transform([user_input])
    faq_vecs = vectorizer.transform(subset['question'])
    sims = cosine_similarity(user_vec, faq_vecs)
    idx = sims.argmax()
    return subset.iloc[idx]['response']

def get_chatbot_response(user_input):
    intent = predict_intent(user_input)
    entities = extract_entities(user_input)
    response = retrieve_response(user_input, intent)

    # Add entity info if relevant
    if entities:
        response += f"\n\n(Detected entities: {entities})"

    return {
        "intent": intent,
        "entities": entities,
        "response": response
    }

# For quick testing
if __name__ == "__main__":
    while True:
        user_input = input("You: ")
        if user_input.lower() in ["exit", "quit"]:
            print("Bot: Goodbye!")
            break
        output = get_chatbot_response(user_input)
        print(f"Bot ({output['intent']}): {output['response']}")



