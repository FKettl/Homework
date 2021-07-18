'''Aula 08 - Exerc.04
Função para URI 1154 sem o uso do return
'''
#Felipe Backes Kettl

def calc_idade():
    count = 1
    total = 0
    while True:
        idade = float(input())
        if idade < 0 :
            print(f'{media:.2f}')
            break
        total +=idade
        media = total/count
        count += 1

calc_idade()