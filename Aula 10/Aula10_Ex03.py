'''Aula 10 - Exerc.03
URI 1192
'''
#Felipe Backes Kettl

ntest = int(input())

for x in range(ntest):
    n = input()
    n1 = int(n[0])
    n3 = int(n[2])
    if n1 == n3:
        print(n1*n3)
        continue
    if n[1] == n[1].upper():
        print(n3 - n1)
    elif n[1] == n[1].lower():
        print(n1 + n3)
    