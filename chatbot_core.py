import pickle
import spacy
import pandas as pd
from sklearn.metrics.pairwise import cosine_similarity

# Load model and vectorizer
intent_model = pickle.load(open("models/intent_model.pkl", "rb"))
vectorizer = pickle.load(open("models/vectorizer.pkl", "rb"))

# Load spaCy NER model
nlp = spacy.load("en_core_web_sm")

# Load FAQ data
faq_data = pd.read_csv("data/faq_data.csv")

def predict_intent(user_input):
    X = vectorizer.transform([user_input])
    intent = intent_model.predict(X)[0]
    return intent

def extract_entities(user_input):
    doc = nlp(user_input)
    entities = [(ent.text, ent.label_) for ent in doc.ents]
    return entities

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
