'''Aula 13 - Exerc.01
URI 1173
'''
#Felipe Backes Kettl

n = int(input())

#vetor = [n*2**i for i in range(10)]
# Serve os dois jeitos, porem o primeiro(linha 8) exige um pouco mais de raciocinio pra chegar nele
vetor = []

for x in range(10):
    vetor.append(n*2**x)
    print(f'N[{x}] = {vetor[x]}')
    
