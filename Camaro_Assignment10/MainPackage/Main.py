# File Name : Main.py
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
from DataPackage.Data import *

if __name__ == "__main__":
    data = Data()
    weather_data = data.get_weather_data()

    print("Latest Mars Weather Data:")
    for entry in weather_data:
        print(f"Sol: {entry['sol']}")
        print(f" Average Temp: {entry['temp']} C")
        print(f" Average Wind Speed: {entry['wind']} m/s")
        print(f" Average Pressure: {entry['pressure']} Pa")
