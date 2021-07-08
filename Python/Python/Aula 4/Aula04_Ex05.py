'''0
Uma empresa de vendas oferece para seus clientes um desconto em função do valor da compra do cliente.
Esse desconto é de 20% se o valor da compra for maior ou igual a R$ 5.000,00 e 15% se for menor.
Faça um programa para imprimir o valor da compra, o desconto obtido por um determinado cliente e o valor da compra com desconto. 
'''
#Felipe Backes Kettl

compra = float(input('Informe o valor total de sua compra: R$ '))

if compra >= 5000:
    print(f'O valor da sua compra: R$ {compra:.2f}')
    print(f'Resulta em um desconto de: R${compra*0.2:.2f}')
    print(f'Total a pagar: R$ {compra*0.8:.2f}')
elif compra < 5000:
    print(f'O valor da sua compra: R$ {compra:.2f}')
    print(f'Resulta em um desconto de: R${compra*0.15:.2f}')
    print(f'Total a pagar: R$ {compra*0.85:.2f}')



