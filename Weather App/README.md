# 🌦️ Weather App (Tkinter + OpenWeatherMap API)

A simple and elegant **desktop weather application** built with **Python’s Tkinter** library.  
It allows users to **enter any city name** and instantly get current weather details like temperature, humidity, wind speed, and pressure — all displayed in a clean graphical interface.

---

## 🌟 Features

- 🏙️ Search for **any city** worldwide
- 🌡️ Get **real-time temperature**, humidity, pressure, and wind speed
- 🌧️ Displays **precipitation chances** (if available)
- ⚠️ Input validation and clear error messages
- 💻 Built entirely with **Tkinter GUI** and **OpenWeatherMap API**

---

## 🧠 How It Works

1. The user enters a **city name** in the input field.
2. When the “Get Weather” button is clicked:
   - The app fetches weather data using the **OpenWeatherMap API**.
   - Data such as temperature, humidity, pressure, and wind speed are extracted.
3. Results are dynamically displayed in the GUI.
4. If the city is not found or a network issue occurs, the app shows a message box alert.

---

## ⚙️ Requirements

- Python **3.x**
- Required library:
  ```bash
  pip install requests
  ```

## 🚀 How to Run

1. Clone this repository:
   ```bash
    git clone https://github.com/baselelsrogy/small-projects-python-chatGPT
   ```
2. Navigate to the project directory:
   ```bash
    cd weather-app
   ```
3. Run the application:
   ```bash
   python weather_app.py
   ```
