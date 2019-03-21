# Functions for the Shopping Model


def minimum_lane(x):
    # Takes 2D array and finds the smallest item in the 1st index
    check = []
    for i in x:
        check.append(i[1])
        lane = check.index(min(check))
    return lane, min(check), check
