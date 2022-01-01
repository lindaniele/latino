import requests
from bs4 import BeautifulSoup
from re import sub
from latino.constants import LANGUAGES
from latino import urls


class Translated:
    __slots__ = ['grammatica', 'lemma', 'paradigma', 'traduzione', '__link']

    def __init__(self, html_data, lang):
        for i in html_data.find_all('span', class_=['grammatica', 'lemma', 'paradigma']):
            setattr(self, i['class'][0], i.text)

        self.traduzione = ', '.join(sub(r'\(.*\) ', '', span.text) for span in
                                    html_data.find_all('span', class_=LANGUAGES[lang])
                                    ).split(', ')

        self.__link = urls.BASE[lang] + html_data.a['href']

    def table(self) -> dict[str, dict[str, list[str]]]:
        """
        returns the coniugation/declention table of the latin word
        :return: dictionaries representing the table
        """

        table = {}
        soup = BeautifulSoup(requests.get(self.__link).text, 'lxml')

        for i in soup.find_all("tr", bgcolor=["#C40904", "#008000", "#FFFFFF", "#D4D6D6"]):
            if i["bgcolor"] == "#C40904":
                modo = i.text
                table[modo] = {}
            elif i["bgcolor"] == "#008000":
                tempo = i.text
                table[modo][tempo] = []
            else:
                if tempo not in table[modo]:
                    tempo = ""
                    table[modo][tempo] = []
                table[modo][tempo].append(i.text.replace(u'\xa0', u''))
        return table

    def __str__(self):
        return u"Transalted(lemma={lemma}, grammatica={grammatica})".format(
            lemma=self.lemma,
            grammatica=self.grammatica
        )
