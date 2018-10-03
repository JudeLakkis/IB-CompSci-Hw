from math import sqrt
string = 'aeiou'


# def vowels(string):
#     print([string.count(vowel) for vowel in 'aeiou'])
#     print(' a  e  i  o  u')
#     vowel = 'aeiou'
#     if vowel in string:
#         print('All in')
#     else:
#         print("nope")


vowel_list = ['a', 'e', 'i', 'o', 'u']
count = 0
for i in range(len(vowel_list)):
    if vowel_list[i] in string:
        count += 1

if count == 5:
    print('Boom!')
elif count < 5 and count > 0:
    print("yash")
else:
    print('nope')


# Part 2
a = 10
b = 2
# print('Yes') if a < b else print('No!')


# Part 3
def maths_thing(value):
    if sqrt(value) > 10 or sqrt(value) < 5:
        print('Whee')
    elif sqrt(value) == 10:
        print('Is a 10')


maths_thing(36)
