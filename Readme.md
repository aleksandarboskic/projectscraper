# Project scraper

## Notes

This project is my test project for specific use-case. Combines technologies as Django REST framework, Celery, RabbitMQ, PostgreSQL database and Docker.

## Description

This is Django-based REST API service for financial news. The service have two parts: 
* REST API service 
* scraping service.

A REST API is primarily used for fetching data, and a scraping service collects and store data from the Yahoo Finance site. 

The Scraper service uses Yahoo RSS feed for collecting data (https://feeds.finance.yahoo.com/rss/2.0/headline?s=AAPL&region=US&lang=en-US, getting data for AAPL symbol Apple Inc).

Scraper service scheduler is implemented with celery extension https://github.com/celery/django-celery-beat

## Features

- Django Rest Framework is used to implement the REST API service. 
- News are fetched per symbol. 
- REST service implements pagination. 
- Celery is used for async tasks and periodic scraping.
- RDBMS is PostgreSQL.
- News are collected using parameter in .env file, right now there is 4 symbols AAPL, TWTR, GC=F(GOLD), INTC
- Services are running in Docker containers
- Project have 3 unit tests as a example use

## Running project

Project can be downloaded from repository and executing command:

   ` docker-compose up --build `

For running unit tests you can execute command:

   ` docker-compose run scraper sh -c "python manage.py test"`
