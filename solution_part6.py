#Please copy the completed function from above into this active code window. Now write a function called get_movie_rating.
#It takes an OMDB dictionary result for one movie and extracts the Rotten Tomatoes rating as an integer.
#For example, if given the OMDB dictionary for “Black Panther”, it would return 97.
#If there is no Rotten Tomatoes rating, return 0.

#Solution:








def get_movie_rating(dct):
    rating = dct['Ratings']
    for dct_item in rating:
        if dct_item['Source'] == 'Rotten Tomatoes':
            return int(dct_item['Value'][:-1])
    return 0


get_movie_rating(get_movie_data("Deadpool 2"))
