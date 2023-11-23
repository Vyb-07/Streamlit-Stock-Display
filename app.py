import streamlit as st
import requests

# Set page title
st.title("Weather Dashboard")

# Sidebar for user input
st.sidebar.header("User Input")
city_name = st.sidebar.text_input("Enter City Name", "London")
openweathermap_api_key = "8b3919e94d36e68de42d5fc62fd35f26"

# Fetch weather data from OpenWeatherMap API
if city_name and openweathermap_api_key:
    weather_url = f"http://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={openweathermap_api_key}"
    response = requests.get(weather_url)
    
    if response.status_code == 200:
        weather_data = response.json()

        # Print the full weather data
        print(weather_data)

        # Display weather information
        st.subheader(f"Weather Information for {city_name}")
        st.write(f"Temperature: {weather_data['main']['temp']} K")
        st.write(f"Description: {weather_data['weather'][0]['description']}")
        st.write(f"Humidity: {weather_data['main']['humidity']}%")
        st.write(f"Wind Speed: {weather_data['wind']['speed']} m/s")
    else:
        st.error(f"Failed to fetch weather data. Status code: {response.status_code}")
else:
    st.warning("Enter a city name in the sidebar and ensure you have a valid OpenWeatherMap API key.")
