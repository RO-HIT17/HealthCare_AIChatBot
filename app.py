
from flask import Flask, request, jsonify
from process1 import process_symptoms

app = Flask(__name__)

@app.route('/chatbot', methods=['POST'])
def chatbot():
    data = request.get_json()
    symptoms_text = data.get('symptoms')
    response = process_symptoms(symptoms_text)
    return jsonify(response)

if __name__ == '__main__':
    app.run(debug=True)