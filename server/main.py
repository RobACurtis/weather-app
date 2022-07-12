import psycopg2
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

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
        LIMIT 2 OFFSET %s;
       """
  data = (days,)
  cur.execute(SQL,data)
  rows = cur.fetchall()
  dailyWeather = []
  for r in rows:
    dailyWeather.append({
      "id":r[0],
      "date": r[1],
      "timezone": r[2],
      "timezoneOffset": r[3],
      "lattitude": r[4],
      "longitude": r[5],
      "sunrise": r[6],
      "sunset": r[7],
      "description": r[8],
      "main": r[9],
      "humidity": r[10],
      "high": r[11],
      "low": r[12]
      })
    cur.close()
    conn.close()
  return dailyWeather
