import requests

def get_weather(api_key, location):
    url = f"http://api.openweathermap.org/data/2.5/weather?q={location}&appid={api_key}&units=metric"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        return data
    else:
        print("Error fetching weather data.")
        print(response.content)  # Print response content for debugging
        return None

def display_weather(weather_data):
    if weather_data:
        city = weather_data['name']
        country = weather_data['sys']['country']
        description = weather_data['weather'][0]['description']
        temp = weather_data['main']['temp']
        feels_like = weather_data['main']['feels_like']
        humidity = weather_data['main']['humidity']
        print(f"Weather in {city}, {country}:")
        print(f"Description: {description}")
        print(f"Temperature: {temp}°C")
        print(f"Feels like: {feels_like}°C")
        print(f"Humidity: {humidity}%")
    else:
        print("No weather data to display.")

def main():
    api_key = "cdc94666e9207efb1b47848fa924aebe"  # Replace this with your OpenWeatherMap API key
    location = input("Enter city name: ")
    weather_data = get_weather(api_key, location)
    display_weather(weather_data)

if __name__ == "__main__":
    main()
