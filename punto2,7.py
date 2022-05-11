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