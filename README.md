# mediahuis

This application is for technical test of Mediahuis company.

In order to run the application you have two options:
1) on local server of Django
2) on docker

1- on local server of Django:

    . check out the project from (https://github.com/kouroshh/mediahuis.git)
    . install the latest Python==>3.9.1
    . install the latest Postgres==>13.1
    . Install pgAdmin4 (optional to have view of database)
    . python3 -m venv virtpy (create virual env and then activate it)
    . pip3 install -r requirements.txt (install all the libs)
    . add the following config in setting.py for DB:
        'NAME': 'restaurant_db',
        'USER': 'postgres', (* set yours)
        'PASSWORD': '123456' (* set yours)
    . python3 manage.py makemigrations
    . python3 manage.py migrate
    . python3 manage.py fill_db path_to_csv (insert all the data into the database)
    . python3 manage.py runserver

2- on Docker:

    . add the following config in setting.py:
        'NAME': 'postgres',
        'USER': 'postgres',
        'PASSWORD': 'postgres',
        'HOST': 'db',
        'PORT': 5432

    . sudo docker-compose run web django-admin startproject composeexample .

    . docker-compose up
    note: docker compose up is inserting the data too

How to use the apis:

This application consists of two main api which are both GET:
1) http://0.0.0.0:8000/restaurant/<str:day>
   the response of calling this api on browser or CURL is the list of restaurants which are open on the specific day. please use one of the following parameters: "Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"

2) http://0.0.0.0:8000/restaurantname/<str:keyword>
   the response of calling this api on browser or CURL is the filttered list of restaurants that contains the exaxt keyword as the param. 

There is also on static page called Offers:
 - http://127.0.0.1:8000/offers/

