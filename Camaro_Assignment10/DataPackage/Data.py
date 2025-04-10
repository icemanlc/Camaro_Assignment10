# File Name : Data.py
# Student Name: Peter Phan, Lucas Iceman, Caitlin Hutchins
# email:  phanpv@mail.uc.edu, icemanlc@mail.uc.edu, hutchicu@mail.uc.edu
# Assignment Number: Assignment 10
# Due Date:   4/10/2025
# Course #/Section:   IS4010-001
# Semester/Year:   Spring 2025
# Brief Description of the assignment: execute an API using a URL, extract and print data to the console.

# Brief Description of what this module does: Learn about accessing a database and producing results from the data. 
# Citations: W3Schools: https://www.w3schools.com/python/python_string_formatting.asp
#StackOverflow: https://stackoverflow.com/questions/1871524/how-can-i-convert-json-to-csv
# Anything else that's relevant: 
import requests
import json
import csv

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
        

    def save_to_csv(self, weather_list, filename="mars_weather.csv"):
        with open(filename, mode='w', newline='') as file:
            writer = csv.DictWriter(file, fieldnames=["sol", "temp", "wind", "pressure"])
            writer.writeheader()
            for entry in weather_list:
                writer.writerow(entry) 
