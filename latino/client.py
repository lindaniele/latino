from bs4 import BeautifulSoup
import requests
from latino import urls
from latino.models import Translated


class Translator:
    def __init__(self, lang="it"):
        self.lang = lang

    def translate(self, text, **kwargs):
        """translates latin text to destination language (italian default)

        :type text: UTF-8 :class:`str`; :class:`unicode`; string sequence (list, tuple, iterator, generator)
        :param text: The latin source text(s) to be translated.
        :return: list of: results or list (when a list is passed)
        """
        if isinstance(text, list):
            result = []
            for item in text:
                translated = self.translate(item, **kwargs)
                result.append(translated)
            return result

        markup = requests.post(
            urls.TRANSLATE[self.lang],
            data={"parola": text}
        ).text

        soup = BeautifulSoup(markup, 'lxml')

        if find := soup.find('div', id='myth'):
            return [Translated(find, self.lang)]

        elif hrefs := soup.find_all('td', {'width': '80%', 'align': 'left'}):
            links = dict.fromkeys(
                href.a['href'] for href in hrefs
            )
            result = []
            for link in links:
                markup = requests.get(urls.BASE[self.lang] + link).text
                find = BeautifulSoup(markup, 'lxml').find('div', id='myth')
                result.append(Translated(find, self.lang))
            return result

        return []
