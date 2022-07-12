import React from 'react';
import getDate from './date';
import getTime from './getTime';

export default function WeatherCard(props) {
  const date = getDate(props.data.date);
  const sunrise = getTime(props.data.sunrise);
  const sunset = getTime(props.data.sunset);
  const description = props.data.description;
  const humidity = props.data.humidity;
  const high = props.data.high;
  const low = props.data.low;
  const icon = 'images/sunny.png'

    // if (state.loading) return null;
    return (
      <>
      <div className="card" style={{ width: "18rem" }}>
        <div className="img-container row center">
          <img className="card-img-top icon" src={icon} alt="weather" />
        </div>
        <div className="card-body">
          <h5 className="card-title text-center">{date}</h5>
          <ul className='list-group'>
            <li className='list-group-item'>{description}</li>
            <li className='list-group-item'>Humidity: {humidity}</li>
            <li className='list-group-item'>High: {high}</li>
            <li className='list-group-item'>Low: {low}</li>
            <li className='list-group-item'>Sunrise Time: {sunrise}</li>
            <li className='list-group-item'>Sunset Time: {sunset}</li>
          </ul>
        </div>
      </div>
      </>
    )
  }
