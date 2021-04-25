# Watering System API
Backend application for the Watering System project created in Python and Django for Embedded Systems course at the AGH University. This application allows collects and stores data from humidity sensors.

## Virtual environment
 - activation: `.venv\Scripts\activate`
 - installing dependencies: `pip3 install -r requirements.txt`

## Docker
 - build image: `docker-compose build`
 - run image: `docker-compose up`
 - run image: `docker-compose run api sh -c "[target command]"`

## Migrations
 - migrate: `docker-compose run api sh -c "python3 manage.py makemigrations api_core"`
