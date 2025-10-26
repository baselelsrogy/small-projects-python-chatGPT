from tkinter import *
from tkinter import messagebox
import requests
import math


def get_weather():
    api_key = "YOUR-API-KEY"
    city = entry_city.get().capitalize().strip()

    if not city :
        messagebox.showwarning("Input Error", "Please enter a city name.")
        return

    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric&lang=ar"

    try :
    
        response = requests.get(url)
        data = response.json()
    
        if response.status_code == 200:
            # Weather Info
            temperature_val = math.trunc(data["main"]["temp"])
            humidity_val = data["main"]["humidity"]
            windSpeed_val = data["wind"]["speed"]
            chanceOfRain_val = data.get("pop", 0) * 100 if "pop" in data else 0
            pressure_val = data["main"]["pressure"]

            # Updade labels dynamically
            city_name.config(text=f"Weather in {city}:")
            temperature.config(text=f"Temperature: {temperature_val}°C")
            humidity.config(text=f"Humidity: {humidity_val}%")
            wind_speed.config(text=f"Wind Speed: {windSpeed_val} km/h")
            pressure.config(text=f"Pressure: {pressure_val} hPa")
            chance_of_rain.config(text=f"Precipitation: {chanceOfRain_val}%")
    
        else:
            messagebox.showerror("Error", "City not found, Please check spelling.")
  
    except ValueError as err :
        messagebox.showerror("Network Error", "Failed to connect to weather service.")

# GUI
frame = Tk()
frame.title("Weather App")
frame.geometry("900x700")
frame.configure(bg="lightblue")

mylabel = Label(frame, text="Weather App", fg="black", bg="lightblue", font="Arial 30 bold", padx=10, pady=10)
mylabel.pack(pady=20)

frame_city = Frame(frame, bg="lightblue")
frame_city.pack(side=TOP, fill=BOTH, pady=10, padx=10)

label_city = Label(frame_city, width=20, bg="lightblue", text="Enter City Name:", font="Arial 20 bold")
label_city.pack(side=LEFT, padx=30)

entry_city = Entry(frame_city, width=30, font="Arial 20 bold")
entry_city.pack(side=RIGHT, padx=30)

btn_getweather = Button(frame, text="Get Weather", bg="#71c716", font="Arial 15 bold", width=15, relief=RAISED, command=get_weather)
btn_getweather.pack(pady=30)

frame_details = Frame(frame, width=850, height=400, bg="lightblue")
frame_details.pack(side=LEFT, anchor="nw", padx=20, fill=X)

city_name = Label(frame_details, text="Weather in -:", font="Arial 20", bg="lightblue")
city_name.pack(padx=(80,0), pady=30)

temperature = Label(frame_details, text="Temperature: - °C", font="Arial 20", bg="lightblue")
temperature.pack(padx=(80,0), pady=(0,25))

humidity = Label(frame_details, text="Humidity: - %", font="Arial 20", bg="lightblue")
humidity.pack(padx=(80,0), pady=(0,25))

wind_speed = Label(frame_details, text="Wind Speed: - km/h", font="Arial 20", bg="lightblue")
wind_speed.pack(padx=(80,0), pady=(0,25))

pressure = Label(frame_details, text="Pressure: - hPa", font="Arial 20", bg="lightblue")
pressure.pack(padx=(80,0), pady=(0,25))

chance_of_rain = Label(frame_details, text="Precipitation: - %", font="Arial 20", bg="lightblue")
chance_of_rain.pack(padx=(80,0), pady=(0,25))

btn_exit = Button(frame, text="Exit", width=12, height=1, bg="red", fg="black", font="Arial 10", command=exit)
btn_exit.pack(side=BOTTOM, anchor="se", padx=20, pady=20)

frame.mainloop()