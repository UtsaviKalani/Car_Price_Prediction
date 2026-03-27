from flask import Flask, request, jsonify
import pickle

app = Flask(__name__)
model = pickle.load(open('model.pkl', 'rb'))

@app.route('/')
def home():
    return "Car price prediction API running"

@app.route('/predict', methods=['POST'])
def predict():
    data = request.json
    features = [[
        data['year'],
        data['km_driven'],
        data['fuel_type']
    ]]
    prediction = model.predict(features)[0]
    return jsonify({'prediction': float(prediction)})

if __name__ == '__main__':
    app.run(debug=True)
