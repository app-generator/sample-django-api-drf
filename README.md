
# [Django API Server Sample](https://docs.appseed.us/samples/django/api-server-sample)

Simple starter built with Python / Django Rest / SQLite3 and JWT Auth. The authentication flow is based on **json web tokens**. Forked from [Django API Server](https://github.com/app-generator/api-server-django). For complete documentation, please access: [Django API Server Sample](https://docs.appseed.us/samples/django/api-server-sample).

<br />

> Features:

- Simple, intuitive codebase - built for beginners (can be extended with ease) 
- Django / Django REST / SQLite3 - a simple, easy to use backend
- Authentication with JWT (JWT login, JWT logout)
- Testing, Docker
- Forked and extended from [Django API Server](https://github.com/app-generator/api-server-django) with more features
    - `api/transactions/create` - create transaction
    - `api/transactions/edit/id`- edit transaction
    - `api/transactions/delete/id` - delete transaction
    - `api/transactions/get/id` - get specific transaction 
    - `api/transactions/get` - get all transactions     

<br />

> Can be used with other UI projects for a complete **fullstack** experience  

- [React Berry Dashboard](https://github.com/app-generator/react-berry-admin-template) - open-source sample
- [React Datta Dashboard](https://github.com/app-generator/react-datta-able-dashboard) - open-source sample
- [React Datta Dashboard PRO](https://appseed.us/product/react-node-js-datta-able-pro) - commercial fullstack product

<br />

> Support: 

- Github (issues tracker), Email: **support @ appseed.us** 
- **Discord**: [LIVE Support](https://discord.gg/fZC6hup) (registered AppSeed Users) 

<br />

![Django API Server - Open-source Django Starter provided by AppSeed.](https://user-images.githubusercontent.com/51070104/126252341-6961a681-767b-4aca-a95f-140da5af5f81.png) 

<br />

## Requirements

- Django==3.2.5
- djangorestframework==3.12.4
- PyJWT==2.1.0
- django-cors-headers==3.7.0 

<br />

## How to use the code

**Clone the sources**

```bash
$ git clone https://github.com/app-generator/api-server-django-sample.git
$ cd api-server-django-sample
```

**Create a virtual environment**

```bash
$ virtualenv -p python3 venv
$ source venv/bin/activate
```

**Install dependencies** using pip

```bash
$ pip install -r requirements.txt
```

**Start the API server** 

```bash
$ python manage.py migrate
$ python manage.py runserver
```

The API server will start using the default port `8000`.


<br />

### [Docker](https://www.docker.com/) execution
---

> Get the code

```bash
$ git clone https://github.com/app-generator/api-server-django.git
$ cd api-server-django
```

> Start the app in Docker

```bash
$ docker-compose up -d --build
```

Visit `http://localhost:5000` in your browser. The API server will be running.


<br />

## API

For a fast set up, use this POSTMAN file: [api_sample](https://github.com/app-generator/api-unified-definition/blob/main/api.postman_collection.json)

> **Register** - `api/users/signup`

```
POST api/users/signup
Content-Type: application/json

{
    "username":"test",
    "password":"pass", 
    "email":"test@appseed.us"
}
```

<br />

> **Login** - `api/users/login`

```
POST /api/users/login
Content-Type: application/json

{
    "password":"pass", 
    "email":"test@appseed.us"
}
```

<br />

> **Logout** - `api/users/logout`

```
POST api/users/logout
Content-Type: application/json
authorization: JWT_TOKEN (returned by Login request)

{
    "token":"JWT_TOKEN"
}
```

<br />

---
[Django API Server Sample](https://docs.appseed.us/samples/django/api-server-sample) - Provided by AppSeed [App Generator](https://appseed.us)
