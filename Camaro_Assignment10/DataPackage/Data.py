import requests
import json

class Data:
    def get_weather_data(self):
        response = requests.get('https://api.nasa.gov/insight_weather/?api_key=f3a8rz56U5IoORGzeSC8nRANkrddeJ2MHSxr4voW&feedtype=json&ver=1.0')
        json_string = response.content
        parsed_json = json.loads(json_string)
        sol_keys = parsed_json["sol_keys"]
        weather_list = []

        for sol in sol_keys:
            sol_data = parsed_json[sol]
            temp = sol_data["AT"]["av"]
            wind = sol_data["HWS"]["av"]
            pressure = sol_data["PRE"]["av"]

            weather_list.append({
                "sol": sol,
                "temp": temp,
                "wind": wind,
                "pressure": pressure
    })
            return weather_list
