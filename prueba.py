
import os
import time
import platform

menu1=0
def inicio():
 def operadores():
  if menu1==1:
   def punto_1():
      print("Programa para calcular el area de un triangulo")
      base=int(input("Digite la base: "))
      altura=int(input("Digite la altura: "))
      area=int((base*altura)/2)
      print("el area del triangulo es: ", area)
      exit()
   punto_1() 
   def punto_2():
    print("Programa para sumar dos numeros")
    numero1=int(input("Digite numero 1: "))
    numero2=int(input("Digite numero 2: "))
    suma=int(numero1+numero2)
    print("La suma de los dos numeros es: ",suma)
    exit()
   punto_2()
   def punto_3():
      exit()
   punto_3()
   def punto_4():
      exit()
   punto_4()
   def punto_5():
      exit()
   punto_5()
   def punto_6():
      exit()
   punto_6()
   def punto_7():
      exit()
   punto_7()
   def punto_8():
      exit()
   punto_8()
   os.system('cls')
   menu2=int(input("Operadores\n  1. Area de un triángulo.\n  2. Ingresar dos números por teclado y sumarlos.\n  3. Area y perímetro de un cuadrado. \n  6.Area y el volúmen de un cilindro. \n  7. Circurferencia. \n 8. Promedio de tres (3) números ingresados por teclado.\n 9. Volver al menu inicion \n99. Salir"))
   if menu2==1:return punto_1()
   elif menu2==2:return punto_2()
   elif menu2==3:return punto_3()
   elif menu2==4:return punto_4()
   elif menu2==5:return punto_5()
   elif menu2==6:return punto_6()
   elif menu2==7:return punto_7()
   elif menu2==8:return punto_8()    
   elif menu2==9:return inicio()
   elif menu2==99:
     time.sleep(2)
     print("Fin del programa")
     exit()  
   else:
     print("Digite una opcion valida")
     time.sleep(2)
     return operadores()       
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
     time.sleep(2)
     exit()  
 else:
     print("Digite una opcion valida")
     time.sleep(2)
     return inicio()      
inicio()
