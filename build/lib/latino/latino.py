from bs4 import BeautifulSoup
import requests
from re import sub


def latin(link, lang) -> list[dict]:
    # Request and search translation on online dictionary Olivetti
    soup = BeautifulSoup(requests.get(link).text, 'lxml')

    # If there's only one definition
    if find := soup.find('div', id='myth'):
        result = {i['class'][0]: i.text for i in find.find_all('span', class_=['grammatica', 'lemma', 'paradigma'])}
        result['traduzione'] = ', '.join(sub(r'\(.*\) ', '', span.text) for span in find.find_all('span', class_=lang)).split(', ')
        return [result]

    # If there are multiple definitions
    elif hrefs := soup.find_all('td', {'width': '80%', 'align': 'left'}):
        links = set(f"https://{link.split('/')[2]}/" + href.a['href'] for href in hrefs)
        return [latin(link, lang)[0] for link in links]

    # If there are None
    return []


def lat_ita(word: str) -> list[dict]:
    """
    Translates word from latin to italian.

    :param word: word to be translated
    :return: a list of results (dictionaries) which values are: 'lemma', 'paradigma' (if there is any), 'grammatica', 'traduzione'
    """
    link = f'https://www.dizionario-latino.com/dizionario-latino-italiano.php?parola={word}'
    return latin(link, 'italiano')


def lat_eng(word: str) -> list[dict]:
    """
    Translates word from latin to english.

    :param word: word to be translated
    :return: a list of results (dictionaries) which values are: 'lemma', 'paradigma' (if there is any), 'grammatica', 'traduzione'
    """
    link = f'https://www.online-latin-dictionary.com/latin-english-dictionary.php?parola={word}'
    return latin(link, 'english')


def lat_fra(word: str) -> list[dict]:
    """
    Translates word from latin to french.

    :param word: word to be translated
    :return: a list of results (dictionaries) which values are: 'lemma', 'paradigma' (if there is any), 'grammatica', 'traduzione'
    """
    link = f'https://www.grand-dictionnaire-latin.com/dictionnaire-latin-francais.php?parola={word}'
    return latin(link, 'francais')
