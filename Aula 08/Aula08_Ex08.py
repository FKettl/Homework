'''Aula 08 - Exerc.08
Função URI 2409 com o uso do return
No programa principal, após conhecer a saída retornada pela função
você deve imprimir uma mensagem comunicando ao João se ele deve procurar um outro colchão
ou o que ele escolheu tem o tamanho adequado. Neste caso o parabenize pela compra!
'''
#Felipe Backes Kettl

def colch(a, b, c, h, l):
    passal = -1
    passah = -2
    cond1 = 0
    cond2 = 0
    count = 0
    for x in (a, b, c):
        if x <= h :
            passah = x
            cond1 +=1
        if x <= l :
            passal = x
            cond2 +=1

        if passal == passah:
            count += 1
            passal = -1
            passah = -2

    if count >= 2 :
        return('S')
    elif ((cond2 >= 1) and (cond1 > 1)) or ((cond2 > 1) and (cond1 >= 1)):
        return('S')
    elif (cond2 >= 1) and (cond1 >= 1) and (count == 0):
        return('S')
    else:
        return('N')

while True:
    a, b, c = [int(x) for x in input('Digite as 3 medidas do colchão em cm: ').split()]
    h, l = [int(x) for x in input('Digita a altura e a largura da porta em cm: ').split()]
    if (1 <= a, b, c <= 300) and (1 <= h, l <= 250):
        break

resposta = colch(a, b, c, h, l)
if resposta == 'S':
    print(f'Esse colchão é uma otima escolha. Parabéns!!!')
else:    
    print('Esse colchão não passa pela porta, melhor escolher outro.')
