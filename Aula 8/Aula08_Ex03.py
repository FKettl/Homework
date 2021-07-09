'''Aula 08 - Exerc.03
função do URI 1150 sem o uso do return
'''
#Felipe Backes Kettl

def ultz(x, z): 
    count = 0
    total = 0
    for i in range(x, z+1):
        total += i
        count += 1
        if total > z:
            print(count)
            break

x = int(input())
z = int(input())

while z <= x:
    z = int(input())
else:
    ultz(x, z)


