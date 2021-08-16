'''Aula 17 - Exerc. 01
URI 1281
'''
#Felipe Backes Kettl


idas = int(input())
for x in range(idas):
    feira = {}
    comprado = 0
    tabela = int(input())
    for x in range(tabela):
        fruta, preço = input().split()
        preço = float(preço)
        feira[f'{fruta}'] = preço
    compras = int(input())
    for x in range(compras):
        fruta, qtd = input().split()
        qtd = int(qtd)
        if fruta in feira.keys():
            comprado += feira[f'{fruta}']*qtd
    print(f'R$ {comprado:.2f}')
    