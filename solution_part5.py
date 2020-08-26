#Please copy the completed function from above into this active code window. Now write a function called get_movie_rating.
#It takes an OMDB dictionary result for one movie and extracts the Rotten Tomatoes rating as an integer.
#For example, if given the OMDB dictionary for “Black Panther”, it would return 97.
#If there is no Rotten Tomatoes rating, return 0.

#Solution:


import requests_with_caching
import json


def get_movie_data(title):
    baseurl1 = 'http://www.omdbapi.com/'
    param_dict1 = {}
    param_dict1['t'] = title
    param_dict1['r'] = 'json'
    this_page_cache = requests_with_caching.get(baseurl1, params=param_dict1)

    return json.loads(this_page_cache.text)

def get_movie_rating(dct):
    rating = dct['Ratings']
    for dct_item in rating:
        if dct_item['Source'] == 'Rotten Tomatoes':
            return int(dct_item['Value'][:-1])
    return 0


get_movie_rating(get_movie_data("Deadpool 2"))
