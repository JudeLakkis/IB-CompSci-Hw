import codecs

lines = []

with open('Assets/Movies.txt', 'r', encoding='utf-8') as f:
    first_line = f.readline()
    attributes = first_line.strip().split(';')

    f.readline()

    movie_data = []
    c = 0
    for line in f.readlines():
        line = line.strip().split(';')
        movie_data.append(tuple(line))

with open('Assets/Movies.tsv', 'w', encoding='utf-8') as f:
    for movie in movie_data:
        for item in movie:
            yeet = item.replace('\t', ' ')
            f.write(yeet + '\t')
        f.write('\n')


# Dictionaries

by_year = {}
for movie in movie_data:
    year = movie[0]
    if year not in by_year:
        by_year[year] = [movie]
    else:
        by_year[year].append(movie)

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
