from flask import Flask, request, jsonify
import os
import requests
from flask_cors import CORS 
from dotenv import load_dotenv

app = Flask(__name__)
CORS(app, resources={r"/*": {"origins": "*"}})

load_dotenv()

API_KEY = os.getenv('API_KEY')
BASE_URL = 'http://api.openweathermap.org/data/2.5/weather'

@app.route('/api/weather', methods=['GET'])
def get_weather():
    city = request.args.get('city')
    if not city:
        return jsonify({"error": "No city provided"}), 400

    params = {
        'q': city,
        'appid': API_KEY,
        'units': 'metric'  # Use metric units for temperature
    }

    response = requests.get(BASE_URL, params=params)
    data = response.json()

    if response.status_code != 200 or data.get('cod') != 200:
        return jsonify({"error": "Failed to fetch weather data. Please try again."}), 500

    weather = {
        "city": data["name"],
        "temperature": data["main"]["temp"],
        "description": data["weather"][0]["description"],
        "icon": data["weather"][0]["icon"],
        "wind_speed": data["wind"]["speed"],
        "visibility": data["visibility"],
        "latitude": data["coord"]["lat"],
        "longitude": data["coord"]["lon"]
    }

    return jsonify(weather)

if __name__ == '__main__':
    # Run the Flask app on localhost and port 5000
    app.run(host='0.0.0.0', port=5000, debug=True)