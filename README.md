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

## Preview
![ezgif com-gif-maker](https://user-images.githubusercontent.com/96838616/178605471-25985a54-511e-42c0-b77a-0ab87f799444.gif)


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

2. Install all dependencies with pip.

    ```shell
    pip install uvicorn
    pip install psycopg2
    pip install schedule
    pip install fastapi
    ```
    
3. Make an account to get an API Key

  https://openweathermap.org/api/one-call-api

4. Start postgreSQL.

  ```shell
  brew services start postgresql
  ```
  
5. Create a database.

```shell
createdb yourDatabaseName
  ```

6. Add your API Key to your .bash_profile.
      - open terminal
      - in your home directory type 
      
  ```shell

    nano .bash_profile
    export WEATHER_API=youraccesskey
    export USER=databaseuser
    export WEATHERDB=nameofyourdatabase
    type ' x ' to save
    type ' y ' to confirm
    then close out of terminal

 ```
 
7. Import schema.sql into your database

8. View your database through pgweb. You can view it in your browser at localhost:8081

```shell
pgweb --db=yourDatabaseName
  ```
 
9. Start the server 

```shell
uvicorn main:app --reload
  ```
10. Start the project. Once started, you can view the application by opening localhost:3000 in your browser

```shell
npm run start
  ```


