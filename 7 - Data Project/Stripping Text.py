import codecs

f = open('Assets/data.txt', 'r')

lines = []

# with open('Assets/data.txt', 'r', encoding='utf-8') as f:
#     for line in f.readlines():
#         line = line.strip().split('.')
#         lines.append(line)
#         print(line)

with open('Assets/data.txt', 'r', encoding='utf-8') as f:
    txt = ''
    for line in f.readlines():
        txt += line.strip()

    for sentence in txt.split('.'):
        lines.append(sentence)

print(lines)
