from math import sqrt

 
while True:
    try:
        d, vf, vg = [int(x) for x in input().split()]
        if (1 <= d <= 100) and (1 <= vf <= 100 ) and (1 <= vg <= 100):
            dg = sqrt(d**2 + 12**2)
            tempof = 12/vf
            tempog = dg/vg
            if tempof < tempog:
                print('N')
            else:
                print('S')
                
        else:
           break
    except EOFError:
        break