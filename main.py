import psycopg2
from fastapi import FastAPI, Path
from fastapi.staticfiles import StaticFiles

conn = psycopg2.connect("dbname=weather user=robcurtis")
cur = conn.cursor()
app = FastAPI()


app.mount("/static", StaticFiles(directory="static"), name="static")

@app.get("/")
def home():
  SQL = """
        SELECT *
        FROM weatherforecast;
       """
  cur.execute(SQL)
  rows = cur.fetchall()
  dailyWeather = []
  for r in rows:
    dailyWeather.append({
      "id":r[0],
      "date": r[1],
      "timezone": r[2],
      "lattitude": r[3],
      "longitude": r[4],
      "sunrise": r[5],
      "sunset": r[6],
      "description": r[7],
      "humidity": r[8],
      "high": r[9],
      "low": r[10]
      })
  return dailyWeather
