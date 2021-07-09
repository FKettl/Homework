'''Aula 07 - Exerc.10
URI 1099
'''
#Felipe Backes Kettl

n = int(input())
total = 0
for num in range(0, n):
    x, y = [int(i) for i in input().split()]
    if x < y:
        for i in range(x+1, y):
            if (i%2 !=0):
                total += i
    else:
        for i in range(y+1, x):
            if (i%2 !=0):
                total += i
    print(total)        
    total = 0