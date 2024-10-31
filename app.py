from flask import Flask, request, jsonify
import pandas as pd

app = Flask(__name__)

# Load dataset
data = pd.read_csv('symptom_disease_medication.csv')

# Helper function to find diseases and medications based on symptoms
def analyze_symptoms(symptoms):
    # Filter data to match symptoms
    matched_diseases = data[data['symptom'].isin(symptoms)]['disease'].unique()
    matched_medications = data[data['symptom'].isin(symptoms)]['medication'].unique()
    return matched_diseases, matched_medications

# Route to analyze symptoms
@app.route('/analyze', methods=['POST'])
def analyze():
    symptoms = request.json.get('symptoms')
    if not symptoms:
        return jsonify({"error": "No symptoms provided"}), 400

    diseases, medications = analyze_symptoms(symptoms)
    return jsonify({
        "probable_diseases": diseases.tolist(),
        "suggested_medications": medications.tolist()
    })

if __name__ == '__main__':
    app.run(debug=True)
