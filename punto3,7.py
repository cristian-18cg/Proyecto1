import os
import time
import platform

def inicio():
 num2=0
 while True:
    num1=int(input("Digite numero a sumar: "))
    if num1 == 0:
        print("Fin")
        exit() 
    else:
     num2=num2+num1
     print(num2)
inicio()