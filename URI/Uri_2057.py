s, t, f = [int(x) for x in input().split()]

chegada = s+t+f
if chegada >= 24:
    chegada -= 24
elif chegada < 0:
    chegada += 24
print(chegada)
