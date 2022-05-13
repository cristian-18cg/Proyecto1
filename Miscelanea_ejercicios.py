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
    exit()
 elif menu1==3:
    exit()
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
