from Data_Project import *
import pickle

# Dictionaries
# Saving at least four different dictionaries

by_year = {}
for movie in movie_data:
    year = movie[0]
    if year not in by_year:
        by_year[year] = [movie]
    else:
        by_year[year].append(movie)

by_length = {}
for movie in movie_data:
    length = movie[1]
    if length not in by_length:
        by_length[length] = [movie]
    else:
        by_length[length].append(movie)

by_genre = {}
for movie in movie_data:
    genre = movie[3]
    if genre not in by_genre:
        by_genre[genre] = [movie]
    else:
        by_genre[genre].append(movie)

by_actor = {}
for movie in movie_data:
    actor = movie[4]
    if actor not in by_actor:
        by_actor[actor] = [movie]
    else:
        by_actor[actor].append(movie)

by_actress = {}
for movie in movie_data:
    actress = movie[5]
    if actress not in by_actress:
        by_actress[actress] = [movie]
    else:
        by_actress[actress].append(movie)

by_director = {}
for movie in movie_data:
    director = movie[6]
    if director not in by_director:
        by_director[director] = [movie]
    else:
        by_director[director].append(movie)

by_rating = {}
for movie in movie_data:
    rating = movie[7]
    if rating not in by_rating:
        by_rating = [movie]
    else:
        by_rating[rating].append(movie)

# by_awards = {}
# for movie in movie_data:
#     awards = movie[7]
#     if awards not in by_awards:
#         by_awards = [movie]
#     else:
#         by_awards[awards].append(movie)

pickle.dump(by_year, open('by_year.p', 'wb'))
pickle.dump(by_director, open('by_director.p', 'wb'))
