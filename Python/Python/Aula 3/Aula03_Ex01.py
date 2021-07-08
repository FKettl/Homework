''' Exerc.01- Aula 03
Escreva um programa para aprovar o empréstimo bancário para compra de uma
casa. O programa vai perguntar o valor da casa, o salário do comprador e em
quantos anos ele vai pagar. Calcule o valor da prestação mensal sabendo que ela
não pode exceder 30% do salário ou então o empréstimo será negado '''

valor_casa = float(input('Valor da casa: R$ '))
salario = float(input('Sálario do comprador: R$ '))
tempo = int(input('Tempo, em anos, para pagar: ')) 
valor_prestaçao = valor_casa / (tempo * 12)

if (valor_prestaçao >= (salario * 0.3)):
    print('Empréstimo negado, valor requerido excede o permitido') 
else:
    print('Empréstimo aprovado, obrigado por nos escolher.')