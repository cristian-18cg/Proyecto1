print("Programa para comparar dos numeros")
numero1=0 
numero2=0
numero1=float(input("Digite el numero 1: "))
numero2=float(input("Digite el numero 2: "))
if numero1 > numero2:
    print("El numero ",numero1, "es mayor","\nEl numero ",numero2, "es menor")
elif numero1 == numero2:
    print("El numero 1: ",numero1, " y el numero 2: ",numero2, "son iguales")
else:
    print("El numero ",numero2, "es mayor","\nEl numero ",numero1, "es menor" )
    