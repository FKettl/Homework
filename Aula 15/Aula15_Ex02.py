'''Aula 15 - Exerc.02
URI 1184
'''
#Felipe Backes Kettl

metodo = input().upper()
total = 0
count = 0
matriz = []
for i in range(12):
    linha = []
    for j in range(12):
        linha.append(float(input()))
        if (j < i):
           total += linha[j]
           count += 1
if metodo == 'S':
    print(f'{total:.1f}')
elif metodo =='M':
    print(f'{total/count:.1f}')
                
