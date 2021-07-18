'''Aula 10 - Exerc.02
URI 2813
'''
#Felipe Backes Kettl

n = int(input())

compradocasa = 0
compradotrab = 0
totaltrab = 0
totalcasa = 0
for x in range(n):
    ida, volta = input().split()
    if ida == 'chuva' and totalcasa == 0:
        compradocasa += 1
        totaltrab +=1
    elif ida == 'chuva':
        totaltrab +=1
        totalcasa -=1
    if volta == 'chuva' and totaltrab == 0:
        compradotrab +=1
        totalcasa +=1
    elif volta == 'chuva':
        totalcasa += 1
        totaltrab -= 1
print(f'{compradocasa} {compradotrab}')
        