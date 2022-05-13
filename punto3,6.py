import os
import time
import platform

def inicio():
 num1=int(input("Digite numero 1: "))
 num2=int(input("Digite numero 2: "))
 if num1>num2:
  print("El primer numero debe ser mayor al segundo")
  time.sleep(2)
  os.system('cls')
  return inicio()
 else:
   while num2>=num1:
       print (num1)
       num1=num1+1

inicio()