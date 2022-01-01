# Latino

Latino è una libreria python che traduce dal latino usando il [Dizionario Latino](https://www.dizionario-latino.com/).

Latino is a python library that translates latin text by making requests to the [Online Latin Dictionary](https://www.dizionario-latino.com/).

Written for Python 3.8+.


```bash
pip install latino
```


## latino.Translator
You have to create an instance of _Translator_ to use this API

**Parameters:**
- **lang** - language to be translated to 
- ~~**settings**~~ (available from the next releases)

**translate**(text, **kwargs)\
Translate text from latin to destination language
* **Parameters:**
  * **text** (str; string sequence) - The latin source text(s) to be translated.
* **Return type:** list[Translated]
* **Return type:** list[list[Translated]] (when a list is passed)

Basic usage:
```python
>>> from latino import Translator
>>> translator = Translator()  # lang="it" (italian default)

>>> # translator.translate returns a list of all possible translations
>>> puella = translator.translate("puella")[0]  # let's get the first result

>>> puella.lemma
pŭella

>>> puella.grammatica
sostantivo femminile  I declinazione

>>> puella.paradigma # might not exist
[puellă], puellae

>>> puella.traduzione
['bambina', 'ragazza', 'fanciulla', 
 'amante', 'donna amata', 'sposa', 
 'giovane donna', 'figlia', 'schiava']

>>> puella.table()
{'FEMMINILE': {'PLURALE': ['Nom.puellae',
                           'Gen.puellārum',
                           'Dat.puellis',
                           'Acc.puellas',
                           'Abl.puellis',
                           'Voc.puellae'],
               'SINGOLARE': ['Nom.puellă',
                             'Gen.puellae',
                             'Dat.puellae',
                             'Acc.puellam',
                             'Abl.puellā',
                             'Voc.puellă']}}
```
##
```python
from latino import Translator

# Translator() takes as arg a lang between "it"/"en"/"fr"
tr = Translator("en") 

# Gonna print possible meanings for "es"
for translated in tr.translate("es"):
    print(translated.traduzione[0])
```
    to eat
    to be
##
```python
from latino import Translator
translator = Translator("fr") 

text = "pulchram puellam sum"
# any string sequence such as list can also be taken as argument!
for i in translator.translate(text.split()):
    print(i[0].paradigma)
```
    [pulcher], pulchră, pulchrum
    [puellă], puellae
    [sum], es, esse, fui

## latino.models

### latino.models.**Translated**

**Members:**
* **grammatica** - grammar
* **lemma** - lemma
* **paradigma** - paradigm
* **traduzione** - list of translations

**table()**\
Returns the Declension table or the Conjugation table 

## latino.LANGUAGES
```python
# languages which can be translated from
LANGUAGES = {
    'it': 'italiano', 
    'en': 'english', 
    'fr': 'francais'
 }
```
## Licenza | License
[MIT](https://choosealicense.com/licenses/mit/)