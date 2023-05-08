import os
import unittest
import json
from flask_sqlalchemy import SQLAlchemy
from app import create_app
from models import setup_db, Movie, Actor
from settings import TEST_DB_NAME, TEST_DB_USER, TEST_DB_PASSWORD


class CastingAgencyTestCase(unittest.TestCase):
    """This class represents the Casting Agency test case"""

    def setUp(self):
        """Define test variables and initialize app."""
        self.app = create_app()
        self.client = self.app.test_client
        # self.database_name = "trivia_test"
        # self.database_path = "postgres://postgres/postgres".format('localhost:5432', self.database_name)
        self.database_name= TEST_DB_NAME
        self.database_path = 'postgresql://{}:{}@{}/{}'.format(TEST_DB_USER,TEST_DB_PASSWORD,'localhost:5432', self.database_name)
        setup_db(self.app, self.database_path)

        # binds the app to the current context
        with self.app.app_context():
            self.db = SQLAlchemy()
            self.db.init_app(self.app)
            # create all tables
            self.db.create_all()

        self.new_movie={
            {
                "release_date": "02/02/2023",
                "title": "New-Movie"
            }   
        }  

        self.new_actor={
            {
                "age":"30",
                "gender":"Female",
                "name":"New-Actor"
            }   
        }
    
    def tearDown(self):
        """Executed after reach test"""
        pass

    # Testcase for movies

    def test_get_movies(self):
        response=self.client().get('/movies')
        data=json.loads(response.data)
        self.assertEqual(response.status_code,200)
        self.assertEqual(data["success"],True)

    def test_get_movies_not_allowed(self):
        response= self.client().post('/movies')  
        data=json.loads(response.data)
        self.assertEqual(response.status_code,405)
        self.assertEqual(data["success"],False)    

    # Testcase for actors

    def test_get_actors(self):
        response=self.client().get('/actors')
        data=json.loads(response.data)
        self.assertEqual(response.status_code,200)
        self.assertEqual(data["success"],True)

    def test_get_actors_not_allowed(self):
        response= self.client().post('/actors')  
        data=json.loads(response.data)
        self.assertEqual(response.status_code,405)
        self.assertEqual(data["success"],False)      
    
    # Testcase for new movie
    def test_create_new_movie(self):
        response=self.client().post('/movies',json=self.new_movie)
        data=json.loads(response.data)
        self.assertEqual(response.status_code,200)
        self.assertEqual(data['success'],True) 

       # Testcase for new actor
    def test_create_new_actor(self):
        response=self.client().post('/actors',json=self.new_actor)
        data=json.loads(response.data)
        self.assertEqual(response.status_code,200)
        self.assertEqual(data['success'],True)     

    # Testcase to delete movie
    def test_delete_question(self):
        response=self.client().delete('/movies/1')
        data=json.loads(response.data)
        question=Movie.query.filter(Movie.id==1).one_or_none()
        self.assertEqual(response.status_code,200)
        self.assertEqual(data['success'],True)     

    # Testcase to delete ator
    def test_delete_actor(self):
        response=self.client().delete('/actors/1')
        data=json.loads(response.data)
        question=Actor.query.filter(Actor.id==1).one_or_none()
        self.assertEqual(response.status_code,200)
        self.assertEqual(data['success'],True)       

# Make the tests conveniently executable
if __name__ == "__main__":
    unittest.main()