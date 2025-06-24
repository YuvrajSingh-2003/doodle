# -*- coding: utf-8 -*-
"""
Created on Wed Jun 25 00:29:22 2025

@author: lenovo
"""
import requests
def weather_det(city, api_key):
    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}"
    try:
        response = requests.get(url)
        response.raise_for_status()
        data = response.json()
        temperature = data["main"]["temp"] - 273.15
        feels_like = data["main"]["feels_like"] - 273.15
        humidity = data["main"]["humidity"]
        pressure = data["main"]["pressure"]
        wind_speed = data["wind"]["speed"]
        wind_direction = data["wind"]["deg"]
        visibility = data.get("visibility", 0) / 1000
        weather_description = data["weather"][0]["description"].capitalize()
        clouds = data["clouds"]["all"]
        
        print(f"Weather in {city}")
        print(f"Temperature: {temperature:.2f}°C (Feels like: {feels_like:.2f}°C)")
        print(f"Humidity: {humidity}%")
        print(f"Pressure: {pressure} hPa")
        print(f"Wind Speed: {wind_speed} m/s")
        print(f"Wind Direction: {wind_direction}°")
        print(f"Visibility: {visibility:.2f} km")
        print(f"Cloudiness: {clouds}%")
        print(f"Description: {weather_description}")
        
    except requests.exceptions.RequestException as e:
        print(f"Error fetching data: {e}")
api_key = "dd6b27327526572f0cd3579c0006270e"
city = input("Enter city: ")
weather_det(city, api_key)