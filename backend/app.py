from flask import Flask, request, jsonify
from flask_cors import CORS
from decision_tree import get_next_step
from pymongo import MongoClient
import os

app = Flask(__name__)
CORS(app)

# MongoDB connection setup
client = MongoClient('mongodb://localhost:27017/')
db = client['physical_therapy']
patients_collection = db['patients']

@app.route('/next-step', methods=['POST'])
def next_step():
    data = request.json
    answers = data.get('answers', {})
    patient_data = data.get('patient_data', {})
    next_step = get_next_step(answers)

    if 'recommendation' in next_step:
        # Save patient data and recommendation to MongoDB
        patient_data['answers'] = answers
        patient_data['recommendation'] = next_step['recommendation']
        patient_data['instructions'] = next_step['instructions']
        patients_collection.insert_one(patient_data)

    return jsonify(next_step)

if __name__ == '__main__':
    app.run(debug=True)
