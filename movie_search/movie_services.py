"""Collections of function(s) for querying the talkpython movie service"""
import requests.exceptions
import collections

MovieResults = collections.namedtuple(
    'MovieResult',
    "imdb_code, title, duration, director, year, rating, imdb_score, keywords,"
    " genres"
)


def find_movies(search_text):
    """
    Finds movies from the talkpython movie service given
    a search term
    :param search_text: Text that is realated to movie(s) of interest
    :return: List of movies sorted by year (newest to oldest)
    """
    if not search_text or not search_text.strip():
        raise ValueError("Search text is required")

    # Search for the given term, check the status code, raise
    # error if there was an issue, organize the results for use
    url = 'http://movie_service.talkpython.fm/api/search/{}'.format(search_text)

    resp = requests.get(url)
    resp.raise_for_status()

    movie_data = resp.json()
    movies_list = movie_data.get('hits')

    movies = [
        MovieResults(**md)  # Unpack dictionary vs typing everything out
        for md in movies_list
    ]

    # sort movies from newest to oldest
    movies.sort(key=lambda m: -m.year)

    return movies
