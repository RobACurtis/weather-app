import psycopg2
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from datetime import date


app = FastAPI()
today = str(date.today())

origins = [
    "http://localhost:3000",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["GET"],
    allow_headers=["*"],
)

@app.get("/{days}")
def home(days: str):
  conn = psycopg2.connect("dbname=weather user=robcurtis")
  cur = conn.cursor()
  SQL = """
        SELECT *
        FROM weatherforecast
        where "dateRequested" = %s
        LIMIT 2 OFFSET %s;
       """
  data = (today, days)
  cur.execute(SQL,data)
  rows = cur.fetchall()
  dailyWeather = []
  for r in rows:
    dailyWeather.append({
      "id":r[0],
      "dateRequested": r[1],
      "date": r[2],
      "timezone": r[3],
      "timezoneOffset": r[4],
      "lattitude": r[5],
      "longitude": r[6],
      "sunrise": r[7],
      "sunset": r[8],
      "description": r[9],
      "main": r[10],
      "humidity": r[11],
      "high": r[12],
      "low": r[13]
      })
    cur.close()
    conn.close()
  return dailyWeather
