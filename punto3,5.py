print("Programa que suma los cuadrados de los cien primeros números naturales")
suma=0
for x  in range(1,101):
    cuadrado=int(x**2)
    suma=(suma+cuadrado)
    print(x**2)
    if x==100:
     print(suma)
