import requests
import json

# Function to fetch weather data
def get_weather(city, api_key):
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"
    response = requests.get(url)
    
    # Check if the response is successful (status code 200)
    if response.status_code == 200:
        data = response.json()
        
        # Extracting relevant information from the data
        city_name = data['name']
        country = data['sys']['country']
        temp = data['main']['temp']
        temp_min = data['main']['temp_min']
        temp_max = data['main']['temp_max']
        humidity = data['main']['humidity']
        pressure = data['main']['pressure']
        description = data['weather'][0]['description']
        wind_speed = data['wind']['speed']
        
        # Printing weather data
        print(f"Weather in {city_name}, {country}:")
        print(f"Temperature: {temp}°C (Min: {temp_min}°C, Max: {temp_max}°C)")
        print(f"Humidity: {humidity}%")
        print(f"Pressure: {pressure} hPa")
        print(f"Weather description: {description}")
        print(f"Wind speed: {wind_speed} m/s")
    else:
        print("City not found or an error occurred. Please check the city name.")

# Main function to take city input and display weather
def main():
    # Replace this with your OpenWeatherMap API key
    api_key = "YOUR_API_KEY_HERE"
    
    city = input("Enter city name: ")
    get_weather(city, api_key)

if __name__ == "__main__":
    main()
