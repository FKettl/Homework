'''Exerc.08 - Aula 04
Com base na tabela abaixo, escreva um programa que leia o código de um item e a quantidade deste item.
A seguir, calcule e mostre o valor da conta a pagar.
Codigo        Especificação       preço
1            Cachorro quente      R$ 4.00
2               X-salada          R$ 4.50
3               X-bacon           R$ 5.00
4             Torrada simples     R$ 2.00
5            Refrigerante         R$ 1.50

'''
#Felipe Backes Kettl

cdgo, qtde = [float(x) for x in input().split()]
if cdgo == 1:
    preco = 4.00    
elif cdgo == 2:
    preco = 4.50
elif cdgo == 3:
    preco = 5.00
elif cdgo == 4:
    preco = 2.00
elif cdgo == 5:
    preco = 1.50
valor = preco * qtde

print(f'Total: R$ {valor:.2f}')
