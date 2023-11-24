import json
import random
import time


def movie_with_id(_,info,_id):
    with open('{}/data/movies.json'.format("."), "r") as file:
        movies = json.load(file)
        for movie in movies['movies']:
            if movie['id'] == _id:
                return movie


def update_movie_rate(_,info,_id,_rate):
    newmovies = {}
    newmovie = {}
    with open('{}/data/movies.json'.format("."), "r") as rfile:
        movies = json.load(rfile)
        for movie in movies['movies']:
            if movie['id'] == _id:
                movie['rating'] = _rate
                newmovie = movie
                newmovies = movies
    with open('{}/data/movies.json'.format("."), "w") as wfile:
        json.dump(newmovies, wfile)
    return newmovie

def resolve_actors_in_movie(movie, info):
    with open('{}/data/actors.json'.format("."), "r") as file:
        data = json.load(file)
        actors = [actor for actor in data['actors'] if movie['id'] in actor['films']]
        return actors

def get_all(_, info):
    with open('{}/data/movies.json'.format("."), "r") as rfile:
        movies = json.load(rfile)["movies"]
        return movies

def movie_by_title(_,info,_title):
    with open('{}/data/movies.json'.format("."), "r") as file:
        movies = json.load(file)
        data = []
        for movie in movies['movies']:
            if movie['title'] == _title:
                data.append(movie)
        return data

def del_movie(_, info, _movieid):
    with open('{}/data/movie.json'.format("."), "r") as file:
        movies = json.load(file)


    movies = [movie for movie in movies if str(movie["id"]) != str(_movieid)]


    with open('{}/data/movie.json'.format("."), "w") as file:
        json.dump(movies, file, indent=4)


def add_movie(_, info, _id, title, director, rating, actors):
    new_movie = {
        "id": _id,
        "title": title,
        "director": director,
        "rating": rating,
        "actors": actors
    }

    with open('{}/data/movie.json'.format("."), "r+") as file:
        movies_data = json.load(file)
        movies_data['movies'].append(new_movie)

        file.seek(0)
        json.dump(movies_data, file)

    return new_movie
