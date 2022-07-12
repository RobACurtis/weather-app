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


@app.get("/")
def home():
  conn = psycopg2.connect("dbname=weather user=robcurtis")
  cur = conn.cursor()
  SQL = """
        SELECT *
        FROM weatherforecast
        LIMIT 2;
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
    cur.close()
    conn.close()
  return dailyWeather
