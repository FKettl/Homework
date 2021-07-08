numero = int(input())
caiu = 0
for x in range(numero):
    latas, copos = [int(x) for x in input().split()]
    if latas > copos:
        caiu += copos

print(caiu)