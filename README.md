# Description of the Plantsfinder (automated plant selection project)
Plantsfinder is a catalog of plants with an automated selection of their assortment. It is used by both amateur gardeners and professionals in the field of landscape design. The material is presented in simple language, understandable to a person who does not have special knowledge. At the same time, descriptions of plants are detailed and contain all the information necessary for work.

Plantsfinder helps when:
1. It's hard for you to choose what to plant. To get a list of all items that match the characteristics of the site, set the search parameters in the menu: frost resistance zone, humidity, illumination, and others.
2. The person has chosen what he wants to see on the site, but wants to check his choice. In this way, he will avoid unsuccessful experiments with plants that are initially unsuitable for planting in a given area. This will save him both time and money.
3. The person has already planted plants, but they do not grow well. Perhaps the reason is not in diseases and pests, but simply in the wrong place. Knowing what the plant needs, he can help him. For example, transplant to another place or change care: increase or decrease the acidity of the soil, water more or less.

Plant selection criteria are arranged in order of importance, with the critical ones coming first. At the very beginning, you specify the characteristics of the place for which you select the assortment. Then come the external signs of the plant - how it should look: width, height, decorative parts and other details.

## Tech Stack
### Main:
- Django 3.2.15
- Docker 20.10.17
- Docker-compose 2.10.2
- Nginx 1.19.3
- Gunicorn 20.0.4
- PostgreSQL 13.0

### Additional:
- Pillow 9.4.0
- Python-dotenv 0.21.0

## Запуск проекта локально
1. Before starting the project, make sure you have installed [Docker](https://docs.docker.com/engine/install/).

2. Clone [репозитарий plantsfinder_eng с GitHub](https://hub.docker.com/).
```
git clone git@github.com:Inozem/plantsfinder_eng.git
```
3. Create an .env file in the root directory and fill it with environment variables.
```
DEBUG=''
ALLOWED_HOSTS='localhost 127.0.0.1 web''
DB_ENGINE=django.db.backends.postgresql
DB_NAME=postgres
POSTGRES_USER=Admin
POSTGRES_PASSWORD=Admin
DB_HOST=db
DB_PORT=5432
SECRET_KEY='django-insecure-0q@sllks6!(0@04u-yl8b1i2qn^ktd+txn8ec43+-4t(^paw9b'
```

* DEBUG - this is a variable that turns the debug mode on and off, to enable this mode, substitute the value '1'.
* SECRET_KEY - this is the secret key to correctly install Django. You can use a predefined value or generate your own.
For the second option, you will need to create, activate a virtual environment and install Django:
```
python -m venv venv
venv\Scripts\activate
pip install django
```

Now you can start generating the key:
```
python -c 'from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())'
```

4. To deploy the project, enter the plantsfinder/ folder and run the following command:
```
docker-compose up -d --build
```

5. Once all containers are deployed, make the migrations.
```
docker-compose exec backend python manage.py makemigrations
docker-compose exec backend python manage.py migrate
```

6. Collect static.
```
docker-compose exec backend python manage.py collectstatic --no-input
```

7. Create base fields.
```
docker-compose exec backend python manage.py add_base_fields
```

8. Generate a test database.
```
docker-compose exec backend python manage.py add_test_data
```

9. Before you start testing the functionality of the site directly, log in to the [site](http://localhost/plants/deciduous/) using the login "Anon" and the password "qweqwe" superuser (with this login and password a user is generated when generating a test database), add some new plants in [admin](http://localhost/admin/). Now everything is ready to start testing.

10. To stop containers running, use the following command:
```
docker-compose down -v 
```
