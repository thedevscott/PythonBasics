"""Movie Search"""
import requests
import movie_search.movie_services as mvs

from tp_common import print_header


def run_event_loop():
    while True:

        try:
            search = input("What would you like to search for? (X to exit): ")

            if search.lower() == 'x':
                print('Bye')
                break

            results = mvs.find_movies(search)
            print("Found {} results.".format(len(results)))
            [
                print('{} -- {}'.format(r.year, r.title))
                for r in results
            ]

        except ValueError:
            print("Error, search text is required")
        except requests.exceptions.ConnectionError:
            print("Error, unable to establish a connection")
        except Exception as e:
            print("Unexpected error. Details {}".format(e))


def main():
    print_header("Movie Search")
    run_event_loop()


if __name__ == '__main__':
    main()
