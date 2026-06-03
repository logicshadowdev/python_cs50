import requests

API_KEY = "e38062fbaa03d18e991c18ea1c0dd6ea"

city = input("Enter city name: ")

url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"

response = requests.get(url)
data = response.json()

if data["cod"] == 200:
    temp = data["main"]["temp"]
    feels = data["main"]["feels_like"]
    desc = data["weather"][0]["description"]
    humidity = data["main"]["humidity"]

    print(f"\n🌍 Weather in {city.upper()}")
    print(f"🌡️  Temperature: {temp}°C")
    print(f"🤔 Feels like: {feels}°C")
    print(f"💧 Humidity: {humidity}%")
    print(f"☁️  Condition: {desc.title()}")

else:
    print("❌ City not found!")