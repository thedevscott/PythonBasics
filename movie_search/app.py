"""Movie Search"""
import requests
import collections

from tp_common import print_header


def run_event_loop():
    while True:

        search = input("What would you like to search for? E[x]it: ")

        if search.lower() == 'x':
            print('Bye')
            break

        url = 'http://movie_service.talkpython.fm/api/search/{}'.format(search)

        resp = requests.get(url)
        resp.raise_for_status()
        movie_data = resp.json()
        movies = movie_data.get('hits')

        print(movies)


def main():
    print_header("Movie Search")
    run_event_loop()


if __name__ == '__main__':
    main()
