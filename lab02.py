d = float(input())
vA = float(input())
vB = float(input())

t = d/(vA + vB) #h
s = vA * t #km

print(format((t * 60),'.2f'), "min")
print(format(s, '.2f'), "km")
