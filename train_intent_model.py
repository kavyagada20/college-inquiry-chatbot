import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
import spacy
import pickle

# Load data
data = pd.read_csv("data/faq_data.csv")

# TF-IDF Vectorization
vectorizer = TfidfVectorizer(stop_words='english')
X = vectorizer.fit_transform(data['question'])
y = data['intent']

# Train model
model = LogisticRegression()
model.fit(X, y)

# Save model and vectorizer
with open("models/intent_model.pkl", "wb") as f:
    pickle.dump(model, f)

with open("models/vectorizer.pkl", "wb") as f:
    pickle.dump(vectorizer, f)

print("✅ Intent classification model trained and saved successfully!")
