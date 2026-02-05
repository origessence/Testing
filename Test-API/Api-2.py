import requests


class TestApiTwo:

    url_random = "https://api.chucknorris.io/jokes/random"
    url_categories = "https://api.chucknorris.io/jokes/categories"

    def __init__(self):
        pass

    def get_api_joke(self):

        category_name = input()

        req = requests.get(self.url_categories).json()

        if category_name in req:
            print(requests.get(self.url_random, params={'category' : category_name}).json().get('value'))
        else:
            print("Ошибка")

test = TestApiTwo()
test.get_api_joke()