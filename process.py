# process.py
import nltk
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB

nltk.download('punkt_tab')


data = [
    ("fever cough throat ", "Flu", "Paracetamol"),
    ("headache nausea", "Migraine", "Ibuprofen"),
    
]

symptoms_list = [item[0] for item in data]
diseases = [item[1] for item in data]
medicines = [item[2] for item in data]

vectorizer = CountVectorizer()
X = vectorizer.fit_transform(symptoms_list)
clf = MultinomialNB()
clf.fit(X, diseases)

def extract_symptoms(text):
    words = nltk.word_tokenize(text.lower())
    symptoms = [word for word in words if word in vectorizer.get_feature_names_out()]
    return ' '.join(symptoms)

def process_symptoms(text):
    symptoms = extract_symptoms(text)
    if not symptoms:
        return {"error": "No recognizable symptoms found"}
    X_test = vectorizer.transform([symptoms])
    predicted_disease = clf.predict(X_test)[0]
    medicine = medicines[diseases.index(predicted_disease)]
    return {"disease": predicted_disease, "medicine": medicine}