"""
This file is used to store common functions used in the
TalkPython Jumpstart Course
"""


def print_header(title: str):
    """
    Prints the header/app name for command line apps
    :param title: String for the application name
    """

    if len(title) < 20:
        multiple = 40
        pad = 25
    else:
        multiple = 80
        pad = 50

    dash = '-' * multiple

    print(dash)
    print('{0}'.format(title.upper().rjust(pad)))
    print(dash)
