import os
from flask import Flask,jsonify,abort,request
from dateutil import parser
from models import setup_db, Movie, Actor, Cast
from flask_cors import CORS
from auth.auth import AuthError, requires_auth,AUTH0_DOMAIN, API_AUDIENCE, AUTH0_CLIENT_ID, AUTH0_CALLBACK_URL

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

    #CORS headers
    @app.after_request
    def after_request(response):
        response.headers.add('Access-Control-Allow-Headers', 'Content-Type, Authorization')
        response.headers.add('Access-Control-Allow-Methods', 'GET, POST, PATCH, DELETE, OPTIONS')
        return response

    @app.route('/')
    def index():
        return{"Hello World!!"}

    @app.route('/auth')
    def authenticate():
        return jsonify({ 'auth-url': f'https://{AUTH0_DOMAIN}/authorize?audience={API_AUDIENCE}&response_type=token&client_id={AUTH0_CLIENT_ID}&redirect_uri={AUTH0_CALLBACK_URL}' })    

    # Get movies
    @app.route('/movies', methods=['GET'])
    @requires_auth('get:movies')  
    def get_movies(payload):
        movies = Movie.query.all()
        if movies is None:
            formatted_movies = []
        else:
            formatted_movies = [movie.short() for movie in movies]       
        return jsonify(
            { 'success': True, 
             'movies': formatted_movies 
            })
    
    # Get actors
    @app.route('/actors', methods=['GET'])
    @requires_auth('get:actors')  
    def get_actors(payload):
        actors = Actor.query.all()
        if actors is None:
            formatted_actors = []
        else:
            formatted_actors = [actor.short() for actor in actors]       
        return jsonify(
            { 'success': True, 
             'actors': formatted_actors
            })
    
    #POST new movie
    @app.route('/movies', methods=['POST'])
    @requires_auth('post:movies') 
    def create_movie(payload):
        body = request.get_json()
        try:
            title = body.get('title', None)
            date = body.get('release_date', None)
            release_date = parser.parse(date).date()
            movie = Movie(title = title, release_date = release_date)  
            movie.insert()     
            
            new_movie = Movie.query.filter(Movie.id == movie.id).one_or_none()
            if new_movie is None:
                abort(404)     
            return jsonify(
                { 'success': True, 
                 'movies': [new_movie.format()] 
                })
        except:
            abort(422)

    #POST new actor
    @app.route('/actors', methods=['POST'])
    @requires_auth('post:actors') 
    def create_actor(payload):
        body = request.get_json()
        try:
            name = body.get('name', None)
            age = body.get('age', None)
            gender = body.get('gender', None)
            actor = Actor(name = name, age = age, gender = gender)  
            actor.insert()
            
            new_actor = Actor.query.filter(Actor.id == actor.id).one_or_none()
            
            if new_actor is None:
                abort(404)     
            return jsonify(
                { 'success': True, 
                 'actors': [new_actor.format()] 
                 })
        except:
            abort(422)
    
    #Delete given movie
    @app.route('/movies/<int:id>', methods= ['DELETE'])
    @requires_auth('delete:movies')
    def delete_movie(payload, id):
     try:
          movie = Movie.query.filter(Movie.id == id).one_or_none()
          if movie is None:
               abort(404)
          else:
             movie.delete()
             return jsonify(
                 { 'success': True,
                   'delete': id})
     except:
          abort(422)  

    #Delete given actor
    @app.route('/actors/<int:id>', methods= ['DELETE'])
    @requires_auth('delete:actors')
    def delete_actor(payload, id):
     try:
          actor = Actor.query.filter(Actor.id == id).one_or_none()
          if actor is None:
               abort(404)
          else:
             actor.delete()
             return jsonify(
                 { 'success': True, 
                  'delete': id})
     except:
          abort(422)  

    #Edit movie
    @app.route('/movies/<int:id>', methods=['PATCH'])
    @requires_auth('patch:movies')
    def edit_movie(payload, id):
     try:
          movie = Movie.query.filter(Movie.id == id).one_or_none()
          if movie is None:
               abort(404)
          else:
             body = request.get_json()
             title = body.get('title', None)
             date = body.get('release_date', None)
             release_date = parser.parse(date).date()

             movie.title = title
             movie.release_date =  release_date
             movie.update()

             updated_movie = Movie.query.filter(Movie.id == movie.id).one_or_none() 
             if updated_movie is None:
                abort(404)       
             return jsonify(
                 { 'success': True, 
                  'movies': [updated_movie.format()] 
                  })
     except:
          abort(422)

    #Edit Actors
    @app.route('/actors/<int:id>', methods=['PATCH'])
    @requires_auth('patch:actors')
    def edit_actor(payload, id):
     try:
          actor = Actor.query.filter(Actor.id == id).one_or_none()
          if actor is None:
               abort(404)
          else:
             body = request.get_json()
             name = body.get('name', None)
             age = body.get('age', None)
             gender = body.get('gender', None)

             actor.name = name
             actor.age =  age
             actor.gender = gender
             actor.update()

             updated_actor = Actor.query.filter(Actor.id == actor.id).one_or_none() 
             if updated_actor is None:
                abort(404)       
             return jsonify(
                 { 'success': True, 
                  'actors': [updated_actor.format()] 
                  })
     except:
          abort(422)

    # Error handlers
    @app.errorhandler(400)
    def bad_request(error):
        return jsonify(
            { "success": False,  
             "error": 400, 
             "message": "Bad Request" }), 400

    @app.errorhandler(401)
    def unauthorized_error(error):
        return jsonify(
            { "success": False, 
             "error": 401, 
             "message": "Unauthorized Access" }), 401

    @app.errorhandler(404)
    def not_found_error(error):
        return jsonify(
            { "success": False, 
             "error": 404, 
             "message": "Not Found" }), 404

    @app.errorhandler(500)
    def internal_error(error):
        return jsonify(
            { "success": False, 
             "error": 500, "message": "Internal Server Error" }), 500

    return app

app = create_app()

if __name__ == '__main__':
    app.run()
