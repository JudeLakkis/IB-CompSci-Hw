import codecs

lines = []

# Loading data from text file

# Open the Movies.txt file to be read with utf-8 encoding
with open('Assets/Movies.txt', 'r', encoding='utf-8') as f:
    first_line = f.readline()
    # Strip the attributes line and split them at every ;
    attributes = first_line.strip().split(';')

    # Skip a line
    f.readline()

    # Create a list with all the stripped movie data in it for later
    movie_data = []
    c = 0
    for line in f.readlines():
        line = line.strip().split(';')
        movie_data.append(tuple(line))


# Saving to TSV file

# Turn the movie data list into a tsv file
with open('Assets/Movies.tsv', 'w', encoding='utf-8') as f:
    for movie in movie_data:
        for item in movie:
            yeet = item.replace('\t', ' ')
            f.write(yeet + '\t')
        f.write('\n')
