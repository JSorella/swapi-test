import requests


class Swapi(object):

    def __init__(self):
        self.url_base = 'https://swapi.co/api/'

    def get_film(self, number):

        path = (self.url_base + 'films/{}').format(number)
        response = requests.get(path)

        return response.json()
