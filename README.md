# Casting Agency 

## Introduction

The Casting Agency models a company that is responsible for creating movies and managing and assigning actors to those movies. You are an Executive Producer within the company and are creating a system to simplify and streamline your process.

Models:
1.Movies with attributes title and release date
2.Actors with attributes name, age and gender

Endpoints:
1.GET /actors and /movies
2.DELETE /actors/ and /movies/
3.POST /actors and /movies and
4.PATCH /actors/ and /movies/

Roles:
1.Casting Assistant - Can view actors and movies
2.Casting Director - All permissions a Casting Assistant has and…Add or delete an actor from the database , Modify actors or movies
3.Executive Producer - All permissions a Casting Director has and…Add or delete a movie from the database

## Render Link - https://casting-agency-deployment.onrender.com/

## Auth Setup - https://casting-agency-deployment.onrender.com/auth

## Installation Instructions

1. Install Python 3.7
2. Install PIP Dependencies 
3. Install Postgres Database 

## Testing Instructions

1. Execute tests from test_app.py

## Postman Collection - Imported from postman and uploaded to GitHub

# API Documentation

Please note that host refers to - https://casting-agency-deployment.onrender.com

## Auth
https://casting-agency-deployment.onrender.com/auth


## GET - https://casting-agency-deployment.onrender.com/movies

- Gets list of movies
- Request Body : None
- Response :
    {
    "movies": [
        {
            "release_date": "Sat, 04 Feb 2023 00:00:00 GMT",
            "title": "03-Movie"
        },
        {
            "release_date": "Sun, 05 Feb 2023 00:00:00 GMT",
            "title": "04-Movie"
        },
        {
            "release_date": "Sun, 05 Feb 2023 00:00:00 GMT",
            "title": "04-Movie"
        },
        {
            "release_date": "Thu, 23 Feb 2023 00:00:00 GMT",
            "title": "movie-02-updated"
        }
    ],
    "success": true
    }



## GET - https://casting-agency-deployment.onrender.com/actors
- Gets list of movies
- Request Body : None
- Response :
    {
    "actors": [
        {
            "age": 21,
            "gender": "Female",
            "name": "02-actor"
        }
    ],
    "success": true
    }

## POST - https://casting-agency-deployment.onrender.com/movies
- Add a new movies
- Request Body : 
    {
   "release_date":"02/05/2023",
   "title":"07-Movie"
    }
- Response :
    {
    "movies": [
        {
            "id": 7,
            "release_date": "Sun, 05 Feb 2023 00:00:00 GMT",
            "title": "07-Movie"
        }
    ],
    "success": true
    }


## POST - https://casting-agency-deployment.onrender.com/actors
- Add new actor
- Request Body :
    {
   "age":21,
   "name":"02-actor",
   "gender":"Female"
    }
- Response :
    {
    "actors": [
        {
            "age": 21,
            "gender": "Female",
            "id": 2,
            "name": "02-actor"
        }
    ],
    "success": true
}


## PATCH - https://casting-agency-deployment.onrender.com/movies/id
- Edit a given amovie
- Request Body:
    {
   "title":"movie-02-updated",
   "release_date":"02/23/2023"
    }
- Response :
    {
    "movies": [
        {
            "id": 6,
            "release_date": "Thu, 23 Feb 2023 00:00:00 GMT",
            "title": "movie-02-updated"
        }
    ],
    "success": true
    }    

## PATCH - https://casting-agency-deployment.onrender.com/actors/id
- Edit a given actor
- Request Body:
   {
   "age":12,
   "name":"11-actor",
   "gender":"Female"
    }
- Response :
    {
    "actors": [
        {
            "age": 12,
            "gender": "Female",
            "id": 2,
            "name": "11-actor"
        }
    ],
    "success": true
    }


## DELETE - https://casting-agency-deployment.onrender.com/movies/id
- Delete a given movie
- Request Body: None
- Response :
    {
    "delete": 6,
    "success": true
    }

## DELETE - https://casting-agency-deployment.onrender.com/actors/id
- Delete a given actor
- Request Body : None
- Resposne:
    {
    "delete": 2,
    "success": true
    }