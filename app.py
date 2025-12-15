import os
import requests
from dotenv import load_dotenv
from flask import Flask, jsonify, request
load_dotenv()
API_KEY = os.environ.get("OPENWEATHERMAP_API_KEY")
OPENWEATHER_URL = "https://api.openweathermap.org/data/2.5/weather"
app = Flask(__name__)
@app.route('/api/weather', methods=['GET'])
def get_weather():
    lat = request.args.get('lat')
    lon = request.args.get('lon')
    city = request.args.get('city')
    zip_code = request.args.get('zip')
    
    params = {
        'appid': API_KEY,
        'units': 'Imperial'
    }
    search_term = "Unknown Location"
    if lat and lon:
        params['lat'] = lat
        params['lon'] = lon
        search_term = f"Lat: {lat}, Lon: {lon}"
    elif zip_code:
        params['zip'] = f"{zip_code},us" 
        search_term = f"Zip Code {zip_code}"
    elif city:
        params['q'] = city
        search_term = f"City {city}"
    else:
        return jsonify({"error": "Required parameters missing. Please provide lat/lon, city, or zip."}), 400
    try:
        response = requests.get(OPENWEATHER_URL, params=params)
        data = response.json()
        if response.status_code != 200:
            message = data.get("message", "External API error.")
            return jsonify({"error": f"Location not found for {search_term}. Error: {message}"}), response.status_code
        return jsonify(data), 200
    except requests.exceptions.RequestException as e:
        print(f"Error connecting to OpenWeatherMap: {e}")
        return jsonify({"error": "Could not connect to the external weather service."}), 500
if __name__ == '__main__':
    from flask_cors import CORS
    CORS(app) 
    app.run(debug=True)