#Please copy the completed functions from the two code windows above into this active code window. Next, you’ll write a function, called get_related_titles.
#It takes a list of movie titles as input.
#It gets five related movies for each from TasteDive, extracts the titles for all of them, and combines them all into a single list. 
#Don’t include the same movie twice.

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
    
    
    
def get_related_titles(movies_titles):
    lst = []
    for movie in movies_titles:
        lst.extend(extract_movie_titles(get_movies_from_tastedive(movie)))
    return list(set(lst))


get_related_titles(["Black Panther", "Captain Marvel"])
get_related_titles([])
