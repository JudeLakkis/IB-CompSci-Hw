from random import randint, uniform
import string
# Extension Task 1


def wierd_random(a, b):
    value_flag = 0

    # This checks if a or b has a type value of Int
    if str(a).isdigit() is True and str(b).isdigit() is True:
        print('Int Value:')
        value_flag = 1
    else:
        # This try/except/else checks if the value raises a ValueError for a float
        try:
            float(a) and float(b)
        except ValueError:
            # This checks if the value is a string or not
            if str(a).isalpha() is True and str(b).isalpha() is True:
                print('String Value:')
                value_flag = 3
        else:
            print('Float Value:')
            value_flag = 2

    # Flags: 1 = Int, 2 = Float, 3 = String
    if value_flag == 1:
        print(randint(a, b))
    elif value_flag == 2:
        print("%.2f" % uniform(a, b))
    elif value_flag == 3:
        var1, var2 = string.ascii_lowercase.index(a), string.ascii_lowercase.index(b)
        print(string.ascii_lowercase[randint(var1, var2)])


value = 'a'
wierd_random(1, 10)
wierd_random(-4.3, 100.4)
wierd_random('a', 'e')
