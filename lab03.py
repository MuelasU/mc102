dAB = float(input())
vA = float(input())
vB = float(input())
xD = float(input())
L = float(input())

tAiD = xD / vA #h
tBiD = (dAB - xD) / vB #h
tBfD = (dAB + (L * 10**(-3)) - xD) / vB #h

print(format(tAiD * 60, '.2f'), "min")
print(tAiD < tBfD) #há colisão
