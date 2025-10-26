import requests
import tkinter as tk
from tkinter import messagebox

# ---------------------------------------
# 🌤️ Weather App using Tkinter and OpenWeatherMap
# Author: ChatGPT
# ---------------------------------------

API_KEY = "YOUR-API-KEY"  # Your OpenWeatherMap API key
BASE_URL = "https://api.openweathermap.org/data/2.5/weather"


# Function to get weather data from API
def get_weather():
    city = city_entry.get().strip()
    if not city:
        messagebox.showwarning("Input Error", "Please enter a city name.")
        return

    # Build API URL
    url = f"{BASE_URL}?q={city}&appid={API_KEY}&units=metric"

    try:
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()

            # Extract data safely
            temperature = data["main"]["temp"]
            humidity = data["main"]["humidity"]
            pressure = data["main"]["pressure"]
            wind_speed = data["wind"]["speed"] * 3.6  # Convert m/s to km/h

            # Check for precipitation
            precipitation = 0
            if "rain" in data and "1h" in data["rain"]:
                precipitation = data["rain"]["1h"]
            elif "snow" in data and "1h" in data["snow"]:
                precipitation = data["snow"]["1h"]

            # Update labels
            result_city.config(text=f"Weather in {city.title()}")
            result_temp.config(text=f"Temperature: {temperature:.1f} °C")
            result_humidity.config(text=f"Humidity: {humidity}%")
            result_wind.config(text=f"Wind Speed: {wind_speed:.1f} km/h")
            result_pressure.config(text=f"Pressure: {pressure} hPa")
            result_precip.config(text=f"Precipitation: {precipitation} mm (last 1h)" if precipitation > 0 else "Precipitation: None")

        elif response.status_code == 404:
            messagebox.showerror("City Not Found", f"City '{city}' not found. Please try again.")
        else:
            messagebox.showerror("Error", f"API request failed (Status: {response.status_code}).")

    except requests.exceptions.RequestException as e:
        messagebox.showerror("Connection Error", f"An error occurred while connecting to the API:\n{e}")


# ---------------------------------------
# 🪟 GUI Setup
# ---------------------------------------

# Create main window
root = tk.Tk()
root.title("WeatherNow - Weather App")
root.geometry("400x400")
root.resizable(False, False)
root.config(bg="#e8f0f2")

# App Title
title_label = tk.Label(root, text="🌦️ WeatherNow", font=("Arial", 20, "bold"), bg="#e8f0f2", fg="#333")
title_label.pack(pady=10)

# City Input
frame_input = tk.Frame(root, bg="#e8f0f2")
frame_input.pack(pady=10)

city_label = tk.Label(frame_input, text="Enter City:", font=("Arial", 12), bg="#e8f0f2")
city_label.grid(row=0, column=0, padx=5)

city_entry = tk.Entry(frame_input, font=("Arial", 12), width=20)
city_entry.grid(row=0, column=1, padx=5)

search_button = tk.Button(root, text="Get Weather", font=("Arial", 12, "bold"), bg="#4a90e2", fg="white", command=get_weather)
search_button.pack(pady=10)

# Results Frame
frame_results = tk.Frame(root, bg="#f7fbfc", bd=2, relief="groove")
frame_results.pack(pady=10, padx=20, fill="both", expand=True)

result_city = tk.Label(frame_results, text="Weather info will appear here.", font=("Arial", 14, "bold"), bg="#f7fbfc", fg="#333")
result_city.pack(pady=5)

result_temp = tk.Label(frame_results, text="", font=("Arial", 12), bg="#f7fbfc")
result_temp.pack(pady=2)

result_humidity = tk.Label(frame_results, text="", font=("Arial", 12), bg="#f7fbfc")
result_humidity.pack(pady=2)

result_wind = tk.Label(frame_results, text="", font=("Arial", 12), bg="#f7fbfc")
result_wind.pack(pady=2)

result_pressure = tk.Label(frame_results, text="", font=("Arial", 12), bg="#f7fbfc")
result_pressure.pack(pady=2)

result_precip = tk.Label(frame_results, text="", font=("Arial", 12), bg="#f7fbfc")
result_precip.pack(pady=2)

# Run the app
root.mainloop()
