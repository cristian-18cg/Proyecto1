from math import pi
print("Programa Circunferencia")
radio= float(input("Digite el radio de la circunferencia: "))
longitud= float(2*pi*radio)
area= float(pi*(radio**2))
print("El area del circulo es: ","{:.5f}".format(area),"\nLa longitud del circulo es:", "{:.5f}".format(longitud))
exit()