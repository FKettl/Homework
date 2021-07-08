'''Aula 07 - Ex 07
URI 1247
'''
#Felipe Backes Kettl


from math import sqrt

 
while True:
  # try:           O try e o except seriam necessários para o problema ser aprovado no Uri, por causa que a ultime linha de entrada no uri é EOF
  # deixei eles como comentário no código só pra referencia, funciona normal sem eles
        d, vf, vg = [int(x) for x in input().split()]
        if (1 <= vf, d, vg <= 100) :
            dg = sqrt(d**2 + 12**2)
            tempof = 12/vf
            tempog = dg/vg
            if tempof < tempog:
                print('N')
            else:
                print('S')
                
        else:
           break
    #except EOFError:
      #  break

