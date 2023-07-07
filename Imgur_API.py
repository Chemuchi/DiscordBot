import random

import requests

from tokenp import *


def random_words():
    words = ['trap', 'mate', 'instrument', 'chemical', 'cart', 'assignment', 'slope', 'marriage', 'theater', 'consumer',
             'behavior', 'curiosity', 'context', 'suffering', 'suggestion', 'deception', 'masterpiece', 'joint', 'tissue',
             'flexibility', 'performance', 'pest', 'migration', 'gap', 'manner', 'lane', 'circumstance', 'laboratory',
             'strength', 'sociology', 'shoulder', 'occasion', 'intelligence', 'gaze', 'hazard', 'admission', 'refund',
             'fee', 'registration', 'competition', 'entry', 'proportion', 'tail', 'victim', 'seed', 'province', 'means',
             'nest', 'phenomenon', 'makeup', 'strategy', 'rejection', 'passion', 'talent', 'cliff', 'composition', 'vision',
             'composer', 'appointment', 'request',
             'disapproval', 'trick', 'confidence', 'drought', 'evidence', 'force',
             'capacity',
             'nuance',
             'cue',
             'motive',
             'depression',
             'source',
             'donor',
             'nutrient',
             'fiber',
             'tribe',
             'shelter',
             'crew',
             'track', 'barrier', 'analogy', 'optimum', 'publication', 'radiation', 'galaxy', 'enthusiasm', 'prime minister',
             'landscape', 'misconception', 'population']
    r_word = random.choice(words)
    return r_word




def search_imgur(query):
    headers = {'Authorization': 'Client-ID ' + ImgurClientID()}

    params = {'q': query}
    response = requests.get('https://api.imgur.com/3/gallery/search', headers=headers, params=params)
    data = response.json()
    return data['data']


def get_random_image(query):
    images = search_imgur(query)
    image = random.choice(images)
    return image['link']
