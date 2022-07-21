# Django Portal GG

This is a game community portal framework that is meant to help small gaming organizations build a user registration and management system around allready existing services such as Discord, Twitch and Steam. The idea is to make administration of self hosted gaming servers easier by providing automation for whitelists and player management.

## Features

* Django 4
* Python 3.10
* User registration via [django-allauth](https://github.com/pennersr/django-allauth)
* Completed templates for user registration (including email templates)
* Templates uses Bootstrap 4.0 and Font Awesome 5
* Docker Compose for development and production (using [Gunicorn](http://gunicorn.org/) and [nginx](https://nginx.org/en/) on production)
* HTTPS by default (using [Let's Encrypt](https://letsencrypt.org))
* Integrate with [Mailgun](https://www.mailgun.com/) for sending email

## User Registration

Currently support login by using email and social accounts

Templates for user registration includes

* Login page
* Sign up page
* Email template for signup
* Password recovery page (send recovery email to set a new password)
* Email template for password recovery
* User profile page
* Edit profile page
* Account settings page (change email, change password)
* Email template for changing email (always requires users to verify email)
* Social account settings page (connect/disconnect with social accounts)

Also, django-allauth was customized to serve better user experience on registration
 
* Automatically merge account if users have an existing account that signed up using different methods
* Always requires users logged in from social account to set a password (users will be able to recover their account using password recovery page)
* Automatically logged user in when confirm **email**

## Deployment

Configure the env files in ./env, then pick either a production or development deployment.

### Development Deployment

First, install [Docker](https://www.docker.com/community-edition) and Docker Compose. Then from the project directory, build the Docker images:

    $ docker-compose -f dev-compose.yml build

Then you can start Docker containers

    $ docker-compose -f dev-compose.yml up

Open `http://127.0.0.1:8000` to see this web application. You can also login to Django admin using `admin` and `admin` as username and password respectively.

### Production Deployment

1. Pull code to server
2. Copy content from `./env/prod.env` to production server
2. Build docker images from `docker-compose -f prod-compose.yml build`
3. Run migration and createsuperuser
4. Start Docker containers using `docker-compose -f prod-compose.yml up -d`
5. Let's Encrypt certificate will be generated automatically after a few minutes