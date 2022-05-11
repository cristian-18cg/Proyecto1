from math import pi


print("Programa para halla area y volumen de un cilindro")
altura=float(input("Digite la altura del cilindro: "))
radio=float(input("Digite el radio del cilindro: "))
area=float((2*pi*radio*altura)+(2*pi*(radio**2)))
volumen=float((pi*(radio**2))*altura)
print("El area del cilindro es: ",area ,"\nEl volumen del cilindro es:", volumen)
exit()