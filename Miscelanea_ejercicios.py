from operator import truediv
import os
import time
import platform
def inicio():
 def operadores():
  os.system('cls')
  print("Operadores\n  1. Calcular el área de un triángulo.\n  2.Ingresar dos números por teclado y sumarlos.\n  3. Ingresar un número y visualizar el número elevado al cuadrado\n  4. Escribir un algoritmo que convierta de euros a dólares.\n 5. Escribir un algoritmo que pida el lado de un cuadrado y muestre el valor del área y del perímtro. ")
 operadores()

 def condicionales():
  os.system('cls')
  print("hola")
 condicionales()

 def ciclos():
  os.system('cls')
  print("hola")
 ciclos()


 os.system('cls')
 print ("Miscelanea ejercicios python")
 menu1=int(input("1. Operadores \n2. Condicionales \n3. Ciclos\n99. Salir \nDigite una opcion:"))
 if menu1==1:
    return operadores()
 elif menu1==2:
    return condicionales()
 elif menu1==3:
    return ciclos()
 elif menu1==99:
     print("Fin del programa")
     exit()  
 else:
     print("Digite una opcion valida")
     time.sleep(2)
     return inicio()      
inicio()
