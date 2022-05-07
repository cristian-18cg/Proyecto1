print("Programa para comparar tres numeros")
numero1=0 
numero2=0
numero3=0
mayor=0
numero1=float(input("Digite el numero 1: "))
numero2=float(input("Digite el numero 2: "))
numero3=float(input("Digite el numero 3: "))
if numero1 > numero2 and numero1 > numero3:
    mayor=float(numero1)
    if  numero2>numero3:
        print("El numero mayor es: ",mayor,"\nEl numero menor es: ",numero3)
    else:
        print("El numero mayor es: ",mayor,"\nEl numero menor es: ",numero2)    
elif numero2>numero1 and numero2>numero3 :
    mayor=float(numero2)
    if  numero1>numero3:
        print("El numero mayor es: ",mayor,"\nEl numero menor es: ",numero3)
    else:
        print("El numero mayor es: ",mayor,"\nEl numero menor es: ",numero1)
elif numero3>numero2 and numero3>numero1:
    mayor=float(numero3)
    if  numero2>numero1:
        print("El numero mayor es: ",mayor,"\nEl numero menor es: ",numero1)
    else:
        print("El numero mayor es: ",mayor,"\nEl numero menor es: ",numero2)        
else:
    if numero2 == numero1 and numero2 == numero3:
     print("los numeros son iguales")


    
