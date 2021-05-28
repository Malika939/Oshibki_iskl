a = 1
sets = set()
while  a < 6:
    b = int(input('enter num: '))
    a += 1
    sets.add(b)
print(min(sets))