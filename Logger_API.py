
import urllib.parse
import urllib.request
import json

BASE_URL = "https://www.giantbomb.com/api"
API_KEY = "0d710e3bcc9a40c5d8f67bd785df5f9e85b7fce5"


def build_search_game(g_name: "String") -> "String":
    url = BASE_URL + "/search/?" + urllib.parse.urlencode([('api_key', API_KEY), ('format', 'json'),
                                                           ('query', g_name), ('resources', 'game')])
    return url


def get_game_page(g_name: "String") -> json:
    url = build_search_game(g_name)
    response = None
    try:
        response = urllib.request.urlopen(url)
        j_text = response.read().decode(encoding='utf-8')
        return json.loads(j_text)

    finally:
        if response is not None:
            response.close()


def print_names(j_text: json):
    results = jtext['results']
    print()
    for x in results:
        print(x['name'])

jtext = get_game_page(input("Enter the game you would like to search for: "))
print_names(jtext)