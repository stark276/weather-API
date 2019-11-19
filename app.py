from flask import Flask, render_template, request
import requests
import pprint

app = Flask(__name__)



@app.route('/weather')
def weather():
    # users_city = request.args.get('city')
    # print(users_city)
    return render_template('weather_form.html')

@app.route('/weather_results', methods=["GET"])
def weather_results_page():
    weather_url = "https://api.openweathermap.org/data/2.5/weather?"
    users_city = request.args.get("city")
    params = {
        'q': users_city,
        'appid': '3793abe0393da66929acbd9cc350ab91'
    }
    response = requests.get(weather_url, params=params)
    response_json = response.json()
    print(response_json)
    # city = response_json['city']
    temp = response_json["main"]['temp']
    
    return render_template('weather_results.html', city=users_city, temp=temp)

if __name__ == '__main__':
    app.run()


