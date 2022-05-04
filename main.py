from cmath import pi, sqrt



def pole(*args):
    if len(args) == 1:
        return pi*(pow(float(args[0]), 2))
    elif len(args) == 2:
        return float(args[0]) * float(args[1])
    elif len(args) == 3:
        p = (float(args[0]) + float(args[1]) + float(args[2])) / 2
        return sqrt(p * (p-float(args[0])) * (p-float(args[1])) * (p-float(args[2])))
    else:
        return 0

suma = 0
kontrolka = True
figury = []
n = int(input())

for i in range(n):
    figury = input().split(' ')
    #map(float, figury)
    temp = pole(*figury)
    print(temp)
    if temp == 0:
        kontrolka = False
    suma += temp


if kontrolka == False:
    print("Błąd: można podać maksymalnie 3 liczby")
else:
    print(round(suma.real, 2))

