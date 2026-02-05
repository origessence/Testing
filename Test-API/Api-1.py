import requests

class TestCreateJoke:

    def __init__(self):
        pass

    url = 'https://api.chucknorris.io/jokes/random'

    def test_create_category_positive(self, category, status_code):

        path_random_joke_category = f"?category={category}"
        url_random_joke_category = self.url + path_random_joke_category
        print(url_random_joke_category)

        result = requests.get(url_random_joke_category)
        print(result.json())

        print(f'Статус-код: {result.status_code}')
        assert result.status_code == status_code, 'ОШИБКА, Статус-код не совпадают'
        print('Статус-код корректен')

        check_joke = result.json()
        joke_value = check_joke.get("value")
        print(joke_value)

        joke_category = check_joke.get("categories")
        print(joke_category)
        assert joke_category[0] == category, 'ОШИБКА, Статус-код не совпадает'
        print('Категория корректна')

        assert_word = 'Chuck'
        assert assert_word in joke_value, 'ОШИБКА, Проверочное слово отсутствует'
        print('Проверочное слово присутствует')
        print("Тест прошел успешно")

    def test_create_category_negative(self, category, status_code):
        path_random_joke_category = f"?category={category}"
        url_random_joke_category = self.url + path_random_joke_category
        print(url_random_joke_category)

        result = requests.get(url_random_joke_category)
        print(result.json())

        print(f'Статус-код: {result.status_code}')
        assert result.status_code == status_code, 'ОШИБКА, Статус-код не совпадают'
        print('Статус-код корректен')

        check_joke = result.json()
        error = check_joke.get("error")
        print(error)
        assert error == 'Not Found', 'ОШИБКА, Поле Error некорректно'
        print('Поле Error корректно')

    def test_all_categories(self):
        url_joke = "https://api.chucknorris.io/jokes/random"
        url_get_categories = "https://api.chucknorris.io/jokes/categories"

        categories  = requests.get(url_get_categories).json()

        for category in categories:
            joke_data = requests.get(url_joke, params={'category': category}).json()
            print(joke_data.get('value'))





random_food_joke = TestCreateJoke()
random_food_joke.test_all_categories()