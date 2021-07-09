'''Exerc.03- Aula 04
Elabore um programa que, dada a idade de uma pessoa, informe se esta é criança, adolescente ou adulto. 
Considere as seguintes faixas etárias:
Idade até 12 anos:				Criança
Idade maior que 12 e menor que 18 anos:	Adolescente
Idade maior ou igual a 18 anos:		Adulto
'''
#Felipe Backes Kettl

idade = input('Informe a sua idade: ')

if idade <= 12:
    print(f'Você tem {idade} anos, portanto é considerado criança.')
elif idade < 18:
    print(f'Você tem {idade} anos, portanto é considerado adolescente.')
else:
    print(f'Você tem {idade} anos, portanto é considerado adulto.')