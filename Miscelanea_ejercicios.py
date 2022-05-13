import os
import time
import platform
from math import pi
from tkinter import E
def inicio():
 os.system('cls')
 print ("Miscelanea ejercicios python")
 menu1=int(input("1. Operadores \n2. Condicionales \n3. Ciclos\n99. Salir \nDigite una opcion:"))
 if menu1==1:
  def menu_2(): 
    os.system('cls')
    menu2=int(input("Operadores\n  1. Area de un triángulo.\n  2. Ingresar dos números por teclado y sumarlos.\n  3. Cuadrado de un numero\n  4. Conversor Euro a Dolar \n  5. Area y perímetro de un cuadrado. \n  6. Area y el volúmen de un cilindro. \n  7. Circurferencia. \n  8. Promedio de tres (3) números ingresados por teclado.\n  9. Volver al menu inicio \n  99. Salir \nDigite una opcion:"))
    if menu2==1:
      os.system('cls')
      print("Programa para calcular el area de un triangulo")
      base=int(input("Digite la base: "))
      altura=int(input("Digite la altura: "))
      area=int((base*altura)/2)
      print("el area del triangulo es: ", area)
      time.sleep(3)
      return menu_2() 
    elif menu2==2:
      os.system('cls')
      print("Programa para sumar dos numeros")
      numero1=int(input("Digite numero 1: "))
      numero2=int(input("Digite numero 2: "))
      suma=int(numero1+numero2)
      print("La suma de los dos numeros es: ",suma)
      time.sleep(3)
      return menu_2()
    elif menu2==3:
      os.system('cls')
      print("Programa para mostrar el cuadrado de un numero ")
      numero1=float(input("Digite el numero: "))
      resultado=float(0)
      resultado=float(numero1**2)
      print("La potencia del numero es: ",resultado)
      time.sleep(3)
      return menu_2() 
    elif menu2==4:
      os.system('cls')
      print("Programa conversor euros a dolares")
      numero1=float(input("Digite los euros: "))
      conversor=0
      conversor=float(numero1*1.0502)
      print("Son: ",conversor ,"USD")
      time.sleep(3)
      return menu_2()
    elif menu2==5:
      os.system('cls')
      print("Programa cuadrado")
      numero1=float(input("Digite uno de los lados del cuadrado: "))
      perimetro=0
      area=0
      perimetro=float(numero1*4)
      area=float(numero1*numero1)
      print("El area del cuadrado es: ",area ,"\nEl perimetro del cuadrado es: ", perimetro)
      time.sleep(3)
      return menu_2() 
    elif menu2==6:
      os.system('cls')
      print("Programa para halla area y volumen de un cilindro")
      altura=float(input("Digite la altura del cilindro: "))
      radio=float(input("Digite el radio del cilindro: "))
      area=float((2*pi*radio*altura)+(2*pi*(radio**2)))
      volumen=float((pi*(radio**2))*altura)
      print("El area del cilindro es: ",area ,"\nEl volumen del cilindro es:", volumen)
      time.sleep(3)
      return menu_2() 
    elif menu2==7:
      os.system('cls')
      print("Programa Circunferencia")
      radio= float(input("Digite el radio de la circunferencia: "))
      longitud= float(2*pi*radio)
      area= float(pi*(radio**2))
      print("El area del circulo es: ","{:.5f}".format(area),"\nLa longitud del circulo es:", "{:.5f}".format(longitud))
      time.sleep(3)
      return menu_2()
    elif menu2==8:
      os.system('cls')
      print("Programa promedio")
      numero1=float(input("Digite el numero 1: "))
      numero2= float(input("Digite el numero 2: "))
      numero3= float(input("Digite el numero 3: "))
      promedio= float((numero1+numero2+numero3)/3)
      print("El promedio de los 3 numeros es: ","{:.5f}".format(promedio))
      time.sleep(3)
      return menu_2()
    elif menu2==9:
      return inicio()
    elif menu2==99:
      os.system('cls')
      print("Fin del programa...")
      time.sleep(2)
      os.system('cls')  
      exit()    
    else:
       print("Digite una opcion valida ")
       time.sleep(2)
       return menu_2()
  menu_2()
 elif menu1==2:
    def menu_condicionales(): 
     os.system('cls')
     menu3=int(input("Condicionales\n  1. Numero positivo o negativo.\n  2. Cual numero es mayor y cual menor.\n  3. Mayor y menor de 3 numeros\n  4. Dados dos números A y B, sumarlos si A es menor que B o sino restarlos. \n  5. Dados dos números A y B encontrar el cociente entre A y B. \n  6. A y B sumarlos si al menos uno de ellos es negativo, en caso contrario multiplicarlos.  \n  7. Año biciesto. \n  8. Volver al menu inicio \n  99. Salir \nDigite una opcion:"))
     if menu3== 1:
        os.system('cls')
        print("Programa para evaluar signo del numero")
        numero1=0
        numero1=float(input("Digite el numero: "))
        if numero1 >= 1:
            print("el numero es positivo")
        elif numero1 == 0:
            print("el numero es neutro")
        else:
            print("el numero es negativo")
        time.sleep(2)
        return menu_condicionales()
     elif menu3==2:
       os.system('cls') 
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
       time.sleep(2)
       return menu_condicionales()     
     elif menu3==3:
         os.system('cls')
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
         time.sleep(2)
         return menu_condicionales()
     elif menu3==4:
        os.system('cls')
        A=float(input("Digite A: "))
        B=float(input("Digite B: "))
        if A<B:
         suma=float(A+B)
         print("la suma de A:",A," + ","B:",B," es:",suma)
        else:
         resta=float(A-B)
         print("la resta de A:",A," - ","B:",B," es:",resta)
        time.sleep(2)
        return menu_condicionales()
     elif menu3==5:
        os.system('cls') 
        print("Programa para encontrar el cociente entre A y B")
        A=float(input("Digite A: "))
        B=float(input("Digite B: "))
        if B==0:
         print("La definicion no es posible")
        else:
         cociente=float(A/B)
         print("El cociente de A: ",A," entre B: ",B," Es: ",cociente)
        time.sleep(2)
        return menu_condicionales()
     elif menu3==6:
        os.system('cls') 
        a=float(input("Digite A: "))
        b=float(input("Digite B: "))
        if a<0 or b<0:
            suma=float(a+b)
            print("El resultado de a:",a," + b:",b ,"es:",suma)
        else:
            mult=float(a*b)
            print("El resultado de a:",a," * b:",b ,"es:",mult) 
        time.sleep(2)
        return menu_condicionales()
     elif menu3==7:
        os.system('cls')
        print("Programa para saber si es un año bisiesto")
        año=int(input("Digite el año: "))
        if año<1582:
         print("No entra en el calendario gregoriano")
        else:
        
         if año%4==0:
            if año%100==0: 
                if año%400==0:
                 print(año," Si es un año biciesto")
                else: 
                 print(año," No es un año biciesto")
            else:
                print(año," Si es un año biciesto")       
         else:
            print(año," No es un año biciesto") 
        time.sleep(2)
        return menu_condicionales()
     elif menu3==8:    
         return inicio()
     elif menu3==99:
      os.system('cls')
      print("Fin del programa...")
      time.sleep(2)
      os.system('cls')  
      exit()    
     else:
       print("Digite una opcion valida ")
       time.sleep(2)
       return menu_condicionales()
    menu_condicionales()
 elif menu1==3:
    def menu_ciclos(): 
     os.system('cls')
     menu4=int(input("Ciclos\n  1. Múltiplos de 3 que hay entre 1 y 100.\n  2. Números impares entre 0 y 100.\n  3. Números pares del 1 al 100.\n  4. Cuadrados de los números del 1 al 30. \n  5. Suma los cuadrados de los cien primeros números naturales. \n  6. Números comprendidos entre ellos en secuencia ascendente.  \n  7. Sumar todos los números que se digitan por teclado mientras no sea cero. \n  8. Volver al menu inicio \n  99. Salir \nDigite una opcion:"))
     if menu4==1:
        os.system('cls') 
        print("Programa que imprime multiplos de 3 del 1 al 100")
        for x  in range(1,101):
         if x%3==0:
            print(x)
        time.sleep(2)
        return menu_ciclos ()
     elif menu4==2:
        os.system('cls')
        print("Programa que imprime numeros primos del 0 al 100")
        for x  in range(0,101):
         if x%2==1:
             print(x)
        time.sleep(2)
        return menu_ciclos () 
     elif menu4==3:
        os.system('cls')
        print("Programa que imprime numeros pares del 1 al 100")
        for x  in range(1,101):
         if x%2==0:
            print(x)
        time.sleep(2)
        return menu_ciclos () 
     elif menu4==4:
        os.system('cls')
        print("Programa que imprime los cuadrados del 1 al 30")
        for x  in range(1,31):
         print(x**2)
        time.sleep(2)
        return menu_ciclos () 
     elif menu4==5:
        os.system('cls')
        print("Programa que suma los cuadrados de los cien primeros números naturales")
        suma=0
        for x  in range(1,101):
            cuadrado=int(x**2)
            suma=(suma+cuadrado)
            print(x**2)
            if x==100:
             print(suma) 
        time.sleep(2)
        return menu_ciclos () 
     elif menu4==6:
         os.system('cls')
         def pnto():
          num1=int(input("Digite numero 1: "))
          num2=int(input("Digite numero 2: "))
          if num1>num2:
           print("El primer numero debe ser mayor al segundo")
           time.sleep(2)
           os.system('cls')
           return menu_ciclos()  
          else:
            while num2>=num1:
                print (num1)
                num1=num1+1
         pnto()
         time.sleep(2)
         return menu_ciclos ()
     elif menu4==7:
        os.system('cls')
        num2=0
        while True:
           num1=int(input("Digite numero a sumar: "))
           if num1 == 0:
            print("Fin")
            time.sleep(2)
            return menu_ciclos() 
           else:
            num2=num2+num1
            print(num2)
        
     elif menu4==8:
        return inicio()
     elif menu4==99:
        os.system('cls')
        print("Fin del programa...")
        time.sleep(2)
        os.system('cls')  
        exit()     
     else:
        print("Digite una opcion valida ")
        time.sleep(2)
        return menu_ciclos()           

    menu_ciclos()    
 elif menu1==99:
     os.system('cls')
     print("Fin del programa...")
     time.sleep(2)
     os.system('cls')
     exit()  
 else:
     print("Digite una opcion valida")
     time.sleep(2)
     return inicio()      
inicio()

