#Please copy the completed function from above into this active code window. 
#Next, you will need to write a function that extracts just the list of movie titles from a dictionary returned by get_movies_from_tastedive. 
#Call it extract_movie_titles.

#Solution:

import requests_with_caching
import json


def get_movies_from_tastedive(movie):
    baseurl = 'https://tastedive.com/api/similar'
    param_dict = {}
    param_dict['q'] = movie
    param_dict['limit'] = 5
    param_dict['type'] = 'movies'

    this_page_cache = requests_with_caching.get(baseurl, params=param_dict)
    return json.loads(this_page_cache.text)
    
def extract_movie_titles(extracted_dict):
     return ([i['Name'] for i in extracted_dict['Similar']['Results']])
     
     
extract_movie_titles(get_movies_from_tastedive("Tony Bennett"))
extract_movie_titles(get_movies_from_tastedive("Black Panther"))
