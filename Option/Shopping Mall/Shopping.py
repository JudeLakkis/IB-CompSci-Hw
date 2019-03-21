# Importing Area
from random import randint
from Shopping_Functions import minimum_lane

# Constants & Variables
PEOPLE = 30
TIME = 24
MAX_LANE = 5

# Lists
# [Lane Number, Number of People, Time since last customer]
lane = [[i, 0, 0] for i in range(5)]


# Main
for i in range(TIME):
	minimum_lane()




    if j[1] < maximum_lane_length:
        if people > 0:
            j[1] += 1
            people -= 1
