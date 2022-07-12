import React, { useState, useEffect } from 'react';
import WeatherCard from './components/weather';

export default function App() {
  const [data, addData] = useState([{}, {}])
  const [days, setDays] = useState(0);
  useEffect(() => {
    fetch(`http://localhost:8000/${days}`)
      .then(res => res.json())
      .then(response => {
        addData([{
          id: response[0].id,
          date: response[0].date,
          timezone: response[0].timezone,
          timezoneOffset: response[0].timezoneOffset,
          lattitude: response[0].lattitude,
          longitude: response[0].longitude,
          sunrise: response[0].sunrise,
          sunset: response[0].sunset,
          description: response[0].description,
          main: response[0].main,
          humidity: response[0].humidity,
          high: response[0].high,
          low: response[0].low
        },
        {
          id: response[1].id,
          date: response[1].date,
          timezone: response[1].timezone,
          timezoneOffset: response[1].timezoneOffset,
          lattitude: response[1].lattitude,
          longitude: response[1].longitude,
          sunrise: response[1].sunrise,
          sunset: response[1].sunset,
          description: response[1].description,
          main: response[1].main,
          humidity: response[1].humidity,
          high: response[1].high,
          low: response[1].low
        }
        ]);
      });
  }, [days])

  return (
    <>
    <div className='background-image'></div>
      <div className='weather-container row center'>
        <div className='title mb-3 cardo-font'>
          <h1>7 Day Weather Forecast</h1>
          <h2>Raleigh, NC</h2>
        </div>
        <div className='row center justify-content-evenly'>
          <WeatherCard data={data[0]} />
          <WeatherCard data={data[1]} />
        </div>
        <div className="buttons row justify-content-between mx-5 padding-button-container">
          <button onClick={() => setDays(days => days - 2)} type="button" className={`btn btn-small btn-outline-primary ${(days <= 0) ? 'opacity-0 disabled' : ''}`}><i className="fa-solid fa-left-long"></i></button>
          <button onClick={() => setDays(days => days + 2)} type="button" className={`btn btn-small btn-outline-primary ${(days >= 6) ? 'opacity-0 disabled' : ''}`}><i className="fa-solid fa-right-long"></i></button>
        </div>
    </div>
  </>
  );
}
