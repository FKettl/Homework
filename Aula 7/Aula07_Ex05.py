'''Aula 07 - Exerc.05
Implementar um programa que calcule o aumento de salário dos funcionários de uma empresa.
O aumento está condicionado ao atual salário de cada funcionário.
Regras:
- para 1.500,00 <= salarioAtual < 1.750,00: aumento igual a 12%;
- para 1.750,00 <= salarioAtual < 2.000,00: aumento igual a 10%;
- para 2.000,00 <= salarioAtual < 3.000,00: aumento igual a 7%;
- para acima de 3.000,00: aumento igual a 5%.
Calcular o aumento de no mínimo 3 funcionários;
A cada cálculo efetuado mostrar um relatório com as seguintes informações: nome do funcionário, salário atual e salário com reajuste
'''
#Felipe Backes Kettl





while True:
    nome, salario = input('Digite o nome do funcionario e o salário que ele recebe: ').split()
    salario = float(salario)
    reajuste = 0
    if salario >= 1500.00 and salario < 1750.00:
        reajuste = salario*1.12
    elif salario < 2000.00 and salario >= 1750.00:
        reajuste = salario*1.1
    elif salario < 3000.00 and salario >= 2000.00:
        reajuste = salario*1.07
    elif salario >= 3000.00:
        reajuste = salario*1.05
    else:
        reajuste = salario
    print(f'O(A) {nome} possui um salário de {salario} atualmente, e ficara com {reajuste} após o reajuste.')
    continuar = input('Deseja calcular de outro funcionário? [S/N] ').upper().split()
    if continuar == 'N':
        break
    elif continuar == 'S':
        continue
