from app import db
from werkzeug.security import (generate_password_hash,
                               check_password_hash)
from  app import login
from flask_login import UserMixin
import requests, json
from hashlib import md5

@login.user_loader
def user_load(id):
    return User.query.get(int(id))

class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key = True, index = True, unique = True)
    username = db.Column(db.String(32), unique = True)
    email = db.Column(db.String(200), unique = True)
    password_hash = db.Column(db.String(128))

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

    def __repr__(self):
        return "<User: {}>".format(self.username)
    def avatar(self, size = 128):
        digest = md5(self.email.lower().encode('utf-8')).hexdigest()
        return 'https://www.gravatar.com/avatar/{}?d=identicon&s={}'.format(
            digest, size)



class Movie:
    def __init__(self, title, year = None):
        self.url = "http://www.omdbapi.com/?t={}&y={}&apikey=72016fef"
        self.title = title
        self.year = year
    def get(self):
        if self.title == None:
            return {"data": "No data is found"}
        else:
            return json.loads(requests.get(self.url.format(self.title, self.year)).text)
        return ""
    """
    Func:
        Name: get_actors()
        Args: Takes no arguments, returns a list of all actors 
    """
    def actors(self):
        return self.get()['Actors'].split(',')
    """
    Returns a url of a movie poster
    """
    def poster(self):
        return self.get()['Poster']

    """
    Returns a string showing a the movie plot
    """
    def plot(self):
        return self.get()['Plot']

    """
    Returns a number of langauges spoken in the movies
    """
    def languages(self):
        return self.get()['Language'].split(',')

    """
    Return the rating of only one site
    """
    def rating(self):
        return self.get()['imdbRating']

    """
    Return a string of the appropriate genre(s)
    """
    def genre(self):
        return self.get()['Genre']

    def get_rating(self):
        percent = (float(self.rating())/10) * 100
        return percent















