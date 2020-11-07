# Codescalers Bookstore
## A REST API FOR A VIRTUAL BOOKSTORE
(Django - DRF - MongoDB - Gunicorn - Nginx - Docker)
### Description:
this project is a Rest API for a virtual bookstore, users can add thier books to the bookstore, list all books, search, view book details, and delete.
    
### Code Style:
PEP 8 -- Style Guide for Python Code
## Getting Started

### Prerequisites & Installation:

#### Python 3.9
Follow instructions to install the latest version of python for your platform in the [python docs](https://docs.python.org/3/using/unix.html#getting-and-installing-the-latest-version-of-python)

#### Docker
install [Docker](https://docs.docker.com/install/), if you don't already have it.

#### MongoDB
The MongoDB server in the image listens on the standard MongoDB port, 27017, so connecting via Docker networks will be the same as connecting to a remote mongod.
    
for more info about mongo official Docker images: https://hub.docker.com/_/mongo

#### Virtual Enviornment
i recommend working within a virtual environment whenever using Python for projects. This keeps your dependencies for each project separate and organaized. Instructions for setting up a virual enviornment for your platform can be found in the [python docs](https://packaging.python.org/guides/installing-using-pip-and-virtual-environments/)

#### PIP Dependencies
Once you have your virtual environment setup and running, install dependencies by naviging to the `/bookstore` directory and running:

```bash
pip install -r requirements.dev.txt
```

This will install all of the required packages we selected within the `requirements.dev.txt` file.

##### Key Dependencies
- Django==3.0.5
- djangorestframework==3.12.2
- django-cors-headers==3.5.0
- djongo==1.3.3
- django-filter

note: For production environments, we'll add on Nginx and Gunicorn.

### browsable API:

Visiting the url directly from the browser will display human-friendly HTML output discribe each resource available with **browsable and clickable urls** for easy API browsing by humans.

The browsable API ensures that all the endpoints you create in your API are able to respond both with machine readable (in JSON) and human readable (in HTML) representations.

By default, the API will return the format specified by the headers, which in the case of the browser is HTML. The format can be specified using `?format=` in the request, so you can look at the raw JSON response in a browser by adding `?format=json` to the URL.

### Local Development without docker:
**escape this section, if you want to run the app inside docker container.**

- install MongoDB Community Edition and make sure it is running on defualt port
- run:
```bash
python manage.py migrate
python manage.py runserver
```
- visit http://127.0.0.1:8000/ for api overview

#### tests:    
- to run tests
```bash
python manage.py test
```

#### import mock data:
i wrote small script to import books mock data from csv file to db, to import it run this command
```bash
python manage.py shell < import_mock_data.py
```
this done automatically when you work with docker developmnet container, see below.

### Local Development with docker:
**this for development purposes so no nginx, .. to run in production with Gunicorn - Nginx, please see Production section.**

- Build the image:
```bash
docker-compose build
```
- Once the images are built (web, mongo, mongo expree), run the containers:
```bash
docker-compose up -d
```
- Navigate to http://localhost:8000/ to view the web service.

note: you can access mongo-express by visit http://localhost:8081

- if you need to check the logs, run:
```bash
docker-compose -f docker-compose.yml logs -f
```
- Spin down the development containers:
```bash
docker-compose down -v
```

#### tests:
while the containers running, execute this command to run the tests:
```bash
docker-compose -f docker-compose.yml exec web python manage.py test
```

## Production
for production environments, we use Gunicorn, a production-grade WSGI server, and Nginx to act as a reverse proxy for Gunicorn to handle client requests as well as serve up static files.

Review [Using NGINX and NGINX Plus as an Application Gateway with uWSGI and Django](https://docs.nginx.com/nginx/admin-guide/web-server/app-gateway-uwsgi-django/) for more info on configuring Nginx to work with Django.

to run the production containers (web, mongo, and nginx):

```bash
docker-compose -f docker-compose.prod.yml up -d --build
```

then visit http://localhost

#### import mock data:
importing mock data in production is unlikly, but if you want to import mock data to production db as in the development mode, please uncomment this line in `entrypoint.prod.sh` then rebuild, but this will delete any books data in the production db.
```bash
#python manage.py shell < import_mock_data.py
```
**warnning: make sure to comment this line after running it, else every time the production containers will run it will delete all books and import the mock data.**

if you need to check the logs, run:
```bash
docker-compose -f docker-compose.prod.yml logs -f
```

Spin down the production containers:
```bash
docker-compose -f docker-compose.prod.yml down -v
```

## API Reference
#### GET: Get all Books using paginated API
##### {{URL}}/api/books

- Example Request:
```bash
curl --location --request GET '{{URL}}/api/books'
```

- Example Response:
```bash
{"count":1000,"next":"http://127.0.0.1:8000/api/books/?page=2","previous":null,"results":[{"id":1,"isbn":"454220598-3","title":"The Two Policemen","author_last_name":"Raimondo","author_first_name":"Snelle","page_count":28,"description":"elementum pellentesque quisque porta volutpat erat quisque erat eros viverra eget congue eget semper rutrum nulla nunc purus phasellus in felis donec semper sapien a libero nam dui proin leo odio porttitor id consequat in consequat ut nulla sed"}, ...]}
```
- Status Code:
200

- PARAMS:
    - page                int : the page number
    - search              str : isbn or book title
    - author_first_name   str
    - author_last_name    str
    - ordering            str : one of this options [isbn, title, author_first_name, author_last_name] , add minus sign before the option for descending order`

#### GET: Get Book by ID
##### {{URL}}/api/books/1

- Example Request:
```bash
curl --location --request GET '{{URL}}/api/books/1'
```

- Example Response:
```bash
{"id":1,"isbn":"454220598-3","title":"The Two Policemen","author_last_name":"Raimondo","author_first_name":"Snelle","page_count":28,"description":"elementum pellentesque quisque porta volutpat erat quisque erat eros viverra eget congue eget semper rutrum nulla nunc purus phasellus in felis donec semper sapien a libero nam dui proin leo odio porttitor id consequat in consequat ut nulla sed"}
```
- Status Code:
200

#### POST: Create Book
##### {{URL}}/api/books/

- Example Request:
```bash
curl --location --request POST '{{URL}}/api/books/' \
--header 'Content-Type: application/json' \
--data-raw '{
    "title": "Mr Hyde",
    "description": "testdesc",
    "isbn": "1234567891234",
    "author_last_name": "jakson",
    "author_first_name": "mike",
    "page_count": 213
}'
```
- Example Response:
```bash
{"id":1001,"isbn":"1234567891234","title":"Mr Hyde","author_last_name":"jakson","author_first_name":"mike","page_count":213,"description":"testdesc"}
```
- Status Code:
201

#### PUT: Update Book
##### {{URL}}/api/books/1/

- Example Request:
```bash
curl --location --request PUT '{{URL}}/api/books/1/' \
--header 'Content-Type: application/json' \
--data-raw '{
    "title": "Mr Hyde",
    "description": "some desc",
    "isbn": "1231231231231",
    "author_last_name": "jakson",
    "author_first_name": "mike",
    "page_count": 220
}'
```
- Example Response:
```bash
{"id":1,"isbn":"1231231231231","title":"Mr Hyde","author_last_name":"jakson","author_first_name":"mike","page_count":220,"description":"some desc"}
```
- Status Code:
200

#### PATCH: Partly Update Book
##### {{URL}}/api/books/1/

- Example Request:
```bash
curl --location --request PATCH '{{URL}}/api/books/1/' \
--header 'Content-Type: application/json' \
--data-raw '{
    "description": "new desc"
}'
```
- Example Response:
```bash
{"id":1,"isbn":"454220598-3","title":"The Two Policemen","author_last_name":"Raimondo","author_first_name":"Snelle","page_count":28,"description":"new desc"}
```
- Status Code:
200

#### DEL: Delete Book
##### {{URL}}/api/books/1/

- Example Request:
```bash
curl --location --request DELETE '{{URL}}/api/books/1' \
--data-raw ''
```
- No Response Body

- Status Code:
204

## Authors
- sameh abouelsaad

## Acknowledgements
- https://github.com/nesdis/djongo
- https://www.django-rest-framework.org/tutorial/quickstart/
- https://docs.docker.com/compose/django/
- https://hub.docker.com/_/mongo
- https://www.docker.com/blog/how-to-use-the-official-nginx-docker-image/
- https://testdriven.io/blog/dockerizing-django-with-postgres-gunicorn-and-nginx/#nginx

