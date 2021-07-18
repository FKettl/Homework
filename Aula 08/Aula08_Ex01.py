'''Aula 08 - Exerc.01
criar uma função que resolve o URI 1048 sem usar o return 
'''
#Felipe Backes Kettl

def calcsal(salario):
    if 0 < salario <= 400.00:
        reajuste = salario*0.15
        novosalario = salario + reajuste
        percentual = 15
        print(f'Novo salario: {novosalario:.2f}')
        print(f'Reajuste ganho: {reajuste:.2f}')
        print(f'Em percentual: {percentual} %')

    elif 400.01 <= salario <= 800.00:
        reajuste = salario*0.12
        novosalario = salario + reajuste
        percentual = 12
        print(f'Novo salario: {novosalario:.2f}')
        print(f'Reajuste ganho: {reajuste:.2f}')
        print(f'Em percentual: {percentual} %')

    elif 800.01 <= salario <= 1200.00:
        reajuste = salario*0.1
        novosalario = salario + reajuste
        percentual = 10
        print(f'Novo salario: {novosalario:.2f}')
        print(f'Reajuste ganho: {reajuste:.2f}')
        print(f'Em percentual: {percentual} %')

    elif 1200.01 <= salario <= 2000.00:
        reajuste = salario*0.07
        novosalario = salario + reajuste
        percentual = 7
        print(f'Novo salario: {novosalario:.2f}')
        print(f'Reajuste ganho: {reajuste:.2f}')
        print(f'Em percentual: {percentual} %')

    elif salario > 2000.00:
        reajuste = salario*0.04
        novosalario = salario + reajuste
        percentual = 4
        print(f'Novo salario: {novosalario:.2f}')
        print(f'Reajuste ganho: {reajuste:.2f}')
        print(f'Em percentual: {percentual} %')

salario = float(input('Qual o sálario: R$ '))
calcsal(salario)
