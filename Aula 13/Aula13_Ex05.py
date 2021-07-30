'''Aula 13 - Exerc.05
URI 2399
'''

n = int(input())
mina = []

for x in range(n):
    mina.append(int(input()))
if n > 1:
    tabuleiro = [(mina[x-1]+mina[x]+mina[x+1]) for x in range(1, n-1)]
    tabuleiro.insert(0, mina[0]+mina[1])
    tabuleiro.insert(n-1, mina[n-1]+mina[n-2])
else:
    tabuleiro = [mina[0]]
    
for x in range(n):
    print(tabuleiro[x])

