import os
from flask import Flask,jsonify,abort,request
from dateutil import parser
from models import setup_db, Movie, Actor, Cast
from flask_cors import CORS
from auth.auth import AuthError, requires_auth, AUTH0_DOMAIN, API_AUDIENCE, AUTH0_CLIENT_ID, AUTH0_CALLBACK_URL

#Udacity-Capstone-Casting Agency
def create_app(test_config=None):

    app = Flask(__name__)
    setup_db(app)
    CORS(app)

    @app.route('/')
    def get_greeting():
        # excited = os.environ['EXCITED']
        # greeting = "Hello" 
        # if excited == 'true': 
        #     greeting = greeting + "!!!!! You are doing great in this Udacity project."
        # return greeting
        return { 'Hello!!!' }

    # @app.route('/coolkids')
    # def be_cool():
    #     return "Be cool, man, be coooool! You're almost a FSND grad!"

    @app.route('/movies', methods=['GET'])
    # @requires_auth('get:movies') - payload
    def get_movies():
        movies = Movie.query.all()
        if movies is None:
            formatted_movies = []
        else:
            formatted_movies = [movie.short() for movie in movies]       
        return jsonify({ 'success': True, 'movies': formatted_movies })
    

    @app.route('/actors', methods=['GET'])
    # @requires_auth('get:actors') - payload
    def get_actors():
        actors = Actor.query.all()
        if actors is None:
            formatted_actors = []
        else:
            formatted_actors = [actor.short() for actor in actors]       
        return jsonify({ 'success': True, 'actors': formatted_actors })


    return app

app = create_app()

if __name__ == '__main__':
    app.run()
