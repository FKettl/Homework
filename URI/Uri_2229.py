count = 1
while True:
    n = int(input())
    quadradinhos = (2**n +1)**2
    if 0 <= n <= 15:
        print(f'Teste {count}')
        print(f'{quadradinhos}')
        print('')
        count +=1
    elif n == -1:
        break