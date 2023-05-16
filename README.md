# Casting Agency 

## Requirements

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

## Postman Collection - Imported from postman and uploaded to GitHub

# API Documentation

GET - /movies - List of movies
GET - /actors - List of actors

POST -/movies - Add new movie
POST - /actors - Add new actor

PATCH - /movies/id - Edit given movie
PATCH - /actors/id - Edit given actor

DELETE - /movies/id - Delete given movie
DELETE - /actors/id - Delete given actor