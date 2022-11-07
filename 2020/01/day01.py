lista = []
with open("/Users/abdirashid/Dev-Ops/python/aoc/2020/01/day01.txt") as numFile:
    for line in numFile:
        lista.append(int(line))

for i in range(len(lista) - 1):
    for s in range(i +1, len(lista)):
        if lista[i] + lista[s] == 2020:
            print(lista[i] * lista[s])
