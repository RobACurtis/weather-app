import psycopg2
import requests
import os
from datetime import date
import schedule
import time


key = os.environ.get('WEATHER_API')
user = os.environ.get('USER')
db = os.environ.get('WEATHERDB')
today = date.today()

def getWeatherData():
  response = requests.get("https://api.openweathermap.org/data/2.5/onecall?lat=35.79911912060484&lon=-78.65971601699076&units=imperial&appid=" + key)
  weather = response.json()

  dbConnection="dbname={} user={}".format(db,user)

  conn = psycopg2.connect(dbConnection)
  cur = conn.cursor()

  dailyWeather = weather["daily"]

  for day in dailyWeather:
    SQL = """insert into weatherforecast ("dateRequested","date", "timezone", "timezoneOffset", "lattitude", "longitude", "sunrise", "sunset", "description", "main", "humidity", "temperatureHigh", "temperatureLow")
            values (%s ,%s, %s, %s ,%s, %s, %s, %s, %s, %s, %s, %s, %s );"""
    data = (today, day["dt"], weather["timezone"], weather["timezone_offset"], weather["lat"], weather["lon"], day["sunrise"], day["sunset"],  day["weather"][0]["description"],  day["weather"][0]["main"], day["humidity"], day["temp"]["max"], day["temp"]["min"])
    cur.execute(SQL, data)
    conn.commit()


  cur.close()
  conn.close()


schedule.every().day.at("00:00").do(getWeatherData)

while True:
  schedule.run_pending()
  time.sleep(1)
