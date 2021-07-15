'''Aula 09 - Exerc.03 
URI 1046
'''
#Felipe Backes Kettl

hinic, hfim = [int(x) for x in input().split()]
duração = hfim-hinic
if duração <= 0:
    duração += 24
print(f'O JOGO DUROU {duração} HORA(S)')