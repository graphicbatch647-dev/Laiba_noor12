from flask import Flask, render_template, request
import requests
import os

app = Flask(__name__)

API_KEY = "aapki_api_key_yahan"
BASE_URL = "http://api.openweathermap.org/data/2.5/weather"

@app.route("/", methods=["GET", "POST"])
def index():
    weather = None
    error = None
    if request.method == "POST":
        city = request.form.get("city")
        response = requests.get(BASE_URL, params={
            "q": city,
            "appid": API_KEY,
            "units": "metric"
        })
        if response.status_code == 200:
            data = response.json()
            weather = {
                "city": data["name"],
                "temp": data["main"]["temp"],
                "description": data["weather"][0]["description"],
                "humidity": data["main"]["humidity"]
            }
        else:
            error = "City nahi mili! Dobara try karein."
    return render_template("index.html", weather=weather, error=error)

if __name__ == "__main__":
    app.run(debug=True)