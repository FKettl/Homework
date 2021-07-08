quadrados = 0
for x in range(1, 10000000000):
   n = int(input())
   if n == 0:
       break
   for i in range(n, 0, -1):
       quadrados += i**2
   print(f'{quadrados}')
   quadrados = 0