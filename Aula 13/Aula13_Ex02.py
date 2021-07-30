'''Aula 13 - Exerc.02
Uri 1471
'''
#Felipe Backes Kettl

 #Profe usei o try e except só pra passa no URI pq eu gosto de ter eles feitos
#while True: #não tem comando pra parar então n da pra usar o while sem usar o try e except, visto que ele só para com erro de EOF
    # try:
n, r = [int(x) for x in input().split()]
foram = [x for x in range(1, n+1)]
voltaram = [int(x) for x in input().split()]
naoVoltaram = [x for x in range(1, n+1) if x not in voltaram]

if not naoVoltaram:
    print('*')

else:
    for j in range(len(naoVoltaram)):
        print(f'{naoVoltaram[j]} ', end='')
    print('')  

    #except EOFError:
     #   break
