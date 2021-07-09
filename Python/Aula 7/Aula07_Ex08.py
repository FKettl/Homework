'''Aula 07 - Exerc.08
URI 1150
'''
#Felipe Backes Kettl

x = int(input())
z = int(input())
total = 0
count = 0
while z <= x:
    z = int(input())
else:  
    for i in range(x, z+1):
        total += i
        count += 1
        if total > z:
            print(count)
            break