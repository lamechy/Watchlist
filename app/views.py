from flask import render_template
from app import app
from .request import get_movies

@app.route('/')
def index():
    '''
    View root page function that returns the index page and its data
    '''
    # Getting popular movies
    popular_movies = get_movies('popular')
    upcoming_movie = get_movies('upcoming')
    now_showing_movie = get_movies('now_playing')
    title = 'Home -Welcome to The Best Movie Review Website Online'
    return render_template('index.html', title = title, popular = popular_movies,  upcoming = upcoming_movie, now_showing = now_showing_movie)
