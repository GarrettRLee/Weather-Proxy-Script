<h1 align="center">Weather Proxy Script</h1>  
<h3 align="center">A Python Flask application for pulling local weather information from the OpenWeatherMap.Org API</h3>


<h1 align="center">Purpose</h1> 

The primary function of the script is to fetch current weather conditions from the external OpenWeatherMap.Org API using GPS information.

An HTML script acts as the frontend interface, while the Python script acts as the server.

# Prerequisites
- Python 3 must be installed on your system
- A OpenWeatherMap API key is required for authentification with OpenWeatherMap.Org

# Clone the repository
Clone the repository to your device using the command:
```
git clone https://github.com/GarrettRLee/Weather-Proxy-Script.git
```
# Setting up a virtual environment
Open the project folder in a command terminal.
```
cd Weather-Proxy-Script
```
Create a virtual environment to run the script on.
```
python -m venv venv
```
If you are using a Powershell terminal, use this command to activate the virtual environment.
```
.\venv\Scripts\activate
```
If you are using Git Bash, use this command instead.
```
source venv/bin/activate
```
# Library Installation
Flask must be installed prior to running the script.

Use this command in order to download the necessary libraries:
```
pip install Flask requests python-dotenv Flask-CORS
```
# Setting up the API key
One of the repositories files is named ".env.example". Inside of this file, you will find the following text:
```
"OPENWEATHERMAP_API_KEY="OPENWEATHERMAP_API_KEY="[PASTE_YOUR_API_KEY_HERE]"
```
Replace [PASTE_YOUR_API_KEY_HERE] with your personal OpenWeatherMap.org API key.

Lastly, rename the ".env.example" file to ".env".
# Running the Script
Now that everything is set up, run the Python script using the following command:
```
python app.py
```
Open your file explorer, navigate to the "Weather-Proxy-Script" folder, and click on the index.HTML file.
# Celebrate!
Hooray!

You should be presented with a webpage asking for permission to use your location, which will then be able to give you your local weather information.

Your script is running!
