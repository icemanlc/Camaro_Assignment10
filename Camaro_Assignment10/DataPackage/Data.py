# File Name : Data.py
# Student Name: Peter Phan,
# email:  phanpv@mail.uc.edu,
# Assignment Number: Assignment 10
# Due Date:   4/10/2025
# Course #/Section:   IS4010-001
# Semester/Year:   Spring 2025
# Brief Description of the assignment: execute an API using a URL, extract and print data to the console.

# Brief Description of what this module does: Learn about accessing a database and producing results from the data. 
# Citations: W3Schools: https://www.w3schools.com/python/python_string_formatting.asp
#
# Anything else that's relevant: 
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
