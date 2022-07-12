# Weather App

#### A web application to view a 7 day weather forecast. 

I built this full stack, single page application as a challenge to learn how to integrate a Python server with a React App.


## Technologies Used
  - React
  - CSS
  - Bootstrap
  - JavaScript
  - PostgreSQL
  - pip3
  - Python
  - Uvicorn
  - FastAPI
  - Schedule
  - psycopg2

  
 ## Feature List
  - User can view the weather for today and tomorrow
  - User can view the weather for upcoming days

## Preview!
![ezgif com-gif-maker (1)](https://user-images.githubusercontent.com/96838616/178612585-fcac0639-c08c-4bf7-8736-6f8774bcb0f1.gif)





# Development

### System Requirements 
- Python 3
- pip3
- Postgres
- npm
- pgweb


## Getting Started 

1. Clone the repository.

```shell
git@github.com:RobACurtis/weather-app.git
```

2. Install all dependencies with pip and npm.

```shell
pip install uvicorn
pip install psycopg2
pip install schedule
pip install fastapi
 ```
    
```shell
npm install
```
    
3. Make an account to get an API Key

    Get your API key [here](https://openweathermap.org/api/one-call-api)

4. Start postgreSQL.

  ```shell
  brew services start postgresql
  ```
  
5. Create a database.

```shell
createdb yourDatabaseName
  ```

6. Set environment variables.
  - open terminal
  - in your home directory type 

```shell
nano .bash_profile
```
```shell
export WEATHER_API="youraccesskey"
export USER="databaseuser"
export WEATHERDB="nameofyourdatabase"
````
    
- type ' x ' to save
- type ' y ' to confirm
- then close out of terminal

7. View your database through pgweb. You can view it in your browser at localhost:8081

```shell
pgweb --db=yourDatabaseName
  ```
  
8. Import schema.sql into your database
9. Run main.py to import weather data into your database (scheduled to run everyday at midnight)
```shell
python3 get-weather.py
```

9. Start the server 

```shell
uvicorn main:app --reload
  ```
10. Start the project. Once started, you can view the application by opening localhost:3000 in your browser

```shell
npm run start
  ```


