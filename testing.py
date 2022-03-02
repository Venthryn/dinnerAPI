
def getKey(d, val):
    return [i for i, v in d.items() if v == val]


d = {
    1:'a',
    2:'b',
    3:'c'
}

l = [
    'a',
    'c'
]

n = []

for i in l:
    n.append(getKey(d, i))


print(n)