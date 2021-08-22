'''Aula 19 - Exerc.02
Implementar um programa que calcule o aumento de salário dos funcionários de uma empresa. O
aumento está condicionado ao atual salário de cada funcionário.
Regras:
    para 1.500,00 <= salarioAtual < 1.750,00: aumento igual a 12%;
    para 1.750,00 <= salarioAtual < 2.000,00: aumento igual a 10%;
    para 2.000,00 <= salarioAtual < 3.000,00: aumento igual a 7%;
    para acima de 3.000,00: aumento igual a 5%.

    Calcular o aumento de 3 funcionários;

    A cada cálculo efetuado imprimir as seguintes informações: nome do funcionário, salário atual e
salário com reajuste.

    Devem ser implementadas 2 arquivos (.py):

    Um arquivo contendo uma classe Funcionário que conterá os métodos para calcular o aumento
de salário e o construtor.

    Um arquivo contendo o controle_do_Funcionário, onde serão feitas chamadas para criar
instâncias da classe Funcionário e também acessar os métodos que pertencem a classe
Funcionário.
'''
#Felipe Backes Kettl

from Funcionario import funcionario
from time import sleep

objetos = {}
objetos['Pedro_A'] = funcionario('Pedro_A', 1550)
objetos['Felipe_K'] = funcionario('Felipe_K', 3500)
objetos['Maria_M'] = funcionario('Maria_M', 2400)

while True:
    sleep(0.5)
    print('-'*15, 'MENU', '-'*15)
    print('1 - Cadastrar novo funcionário.')
    print('2 - Checar funcionários cadastrados.')
    print('3 - Reajustar salário')
    print('4 - Sair')
    print('-'*36)
    
    c = input('O que deseja fazer? [1, 2, 3, 4]: ')
    print()

    if c == '4': #Sair
        print('Fim.')
        break

    elif c not in '1234': # Resposta errada
        print('Por favor digite uma resposta válida.')
        

    elif c == '1': #Cadastrar novo
        nome, salario = input('Digite o nome e o salário do funcionário (Use _ para a inicial do segundo nome, Ex: Felipe_B): ').split()
        objetos[nome] = funcionario(nome, salario)
        

    elif c == '2': # Checar banco de dados
        funcionario.checar_funcionarios(funcionario)
        

    elif c == '3': # Reajustar salario
        p = input('Deseja reajustar o sálario de qual funcionário?: ')
        funcionario.reajustar_salario(objetos[p])
        
    print()
   