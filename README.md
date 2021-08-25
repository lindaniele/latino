# Latino

Latino è una libreria Python per tradurre il latino, scritta da [lindaniele](https://github.com/lindaniele).\
Latino is a python library which helps you translating from latin.

## Installazione | Installation

Usa [pip](https://pip.pypa.io/en/stable/) package manager per installare latino.

```bash
pip install latino
```
||
```bash
pip3 install latino
```

## Utilizzo | Usage

```python
from latino import lat_ita

# restituisce una lista di risultati sotto forma di dizionari
# in questo caso puella ha solo un possibile significato 
# (la lista conterrà quindi un dizionario)
print(lat_ita("puella"))
```
Output:
```python
[
    {
        'grammatica': 'sostantivo femminile  I declinazione',

        'lemma': 'pŭella',

        'paradigma': '[puellă], puellae',  # se c'è

        'traduzione': ['bambina', 'ragazza', 'fanciulla', 
                       'amante', 'donna amata', 'sposa', 
                       'giovane donna', 'figlia', 'schiava']
     }
]
```
#### Altri esempi:
```python
import latino

# traduce da latino a italiano
latino.lat_ita("puella")

# translates from latin to english
latino.lat_eng("puella")

# traduit du latin vers le français
latino.lat_fra("puella")
```
```python
from latino import lat_ita

puella = lat_ita('puella')[0]

paradigma = puella['paradigma']
traduzione = puella['traduzione']
```

## Licenza | License
[MIT](https://choosealicense.com/licenses/mit/)