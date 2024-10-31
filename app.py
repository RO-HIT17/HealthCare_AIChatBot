
from flask import Flask, request, jsonify
from process import process_symptoms 
app = Flask(__name__)

@app.route('/chatbot', methods=['POST'])
def chatbot():
    data = request.get_json()
    symptoms = data.get('symptoms')
    response = process_symptoms(symptoms)
    return jsonify(response)

if __name__ == '__main__':
    app.run(debug=True)