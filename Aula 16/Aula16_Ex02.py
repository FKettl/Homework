'''Exercício 2:
#Ordenando Dicionário
Crie um programa em que 4 jogadores joguem 1 dado e tenham valores aleatórios.
Guarde esses resultados em um dicionário.
No final, coloque este dicionário em ordem, sabendo que o vencedor tirou o maior
número do dado. '''
#Felipe Backes Kettl

from random import randint


jogo = {}
ordenado = {}

jogo['Jogador 1'] = randint(1, 6)
jogo['Jogador 2'] = randint(1, 6)
jogo['Jogador 3'] = randint(1, 6)
jogo['Jogador 4'] = randint(1, 6)

print(sorted(jogo.items(), key=lambda x:x[1], reverse= True))
