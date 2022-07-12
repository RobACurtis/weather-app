import psycopg2
import requests

response = requests.get("https://api.openweathermap.org/data/2.5/onecall?lat=33.44&lon=-94.04&appid=")
weather = response.json()

conn = psycopg2.connect("dbname=weather user=robcurtis")
cur = conn.cursor()

dailyWeather = weather["daily"]

for day in dailyWeather:
  SQL = """insert into weatherforecast ("date", "timezone", "lattitude", "longitude", "sunrise", "sunset", "description", "humidity", "temperature-high", "temperature-low")
          values (%s, %s, %s ,%s, %s, %s, %s, %s, %s, %s );"""
  data = (day["dt"], weather["timezone"], weather["lat"], weather["lon"], day["sunrise"], day["sunset"],  day["weather"][0]["description"], day["humidity"], day["temp"]["max"], day["temp"]["min"])
  cur.execute(SQL, data)
  conn.commit()


cur.close()
conn.close()
