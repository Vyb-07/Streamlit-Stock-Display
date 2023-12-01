# Weather-Display
Here is a README.md file you can use for your Streamlit weather app:

```md
# Streamlit Weather App

This is a simple weather dashboard app built with Streamlit to fetch and display weather data for a given city using the OpenWeatherMap API.

## Usage
```
1. Sign up for a free API key at [OpenWeatherMap]
```
https://openweathermap.org/api
```
2. Clone this repo

```bash
git clone https://github.com/Vyb-07/Weather-Display.git
```

3. Install requirements

```bash 
pip install -r requirements.txt
```

4. Add your OpenWeatherMap API key to the app code
```python
openweathermap_api_key = "YOUR_WEATHER_API_KEY" 
```

5. Run the app

```bash
streamlit run app.py
```

6. Enter a city name in the sidebar to fetch its weather data

## Features

- Fetch current weather data from OpenWeatherMap API including:

  - Temperature
  - Weather description
  - Humidity
  - Wind speed

- User friendly input via Streamlit sidebar
- Error handling for invalid city names & API keys

## TODO

- Add ability to switch between metric and imperial units
- Display graphical weather icons 
- Add support for forecasts, historical data, etc.

## Credits

This app uses the [OpenWeatherMap](https://openweathermap.org/api) API to fetch weather data.
```

Let me know if you would like any changes to this README!
