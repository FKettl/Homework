cdgo, qtde = [float(x) for x in input().split()]
if cdgo == 1:
    preco = 4.00    
elif cdgo == 2:
    preco = 4.50
elif cdgo == 3:
    preco = 5.00
elif cdgo == 4:
    preco = 2.00
elif cdgo ==5:
    preco = 1.50
valor = preco * qtde
print(f'Total: R$ {valor:.2f}')