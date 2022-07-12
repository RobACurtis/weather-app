import React, { useState, useEffect } from 'react';

export default function Weather() {
  const [data, addData] = useState(null)

  useEffect(() => {
    fetch('http://localhost:8000/')
    .then(res => res.json())
    .then(response => {
      console.log(response)
      addData({
        weather: [response[0], response[1]]
    });
    });
  }, [])


  const description = data ? data.weather[0].description : null;

    // if (state.loading) return null;
    return (
      <div>{description}</div>
    )
  }
