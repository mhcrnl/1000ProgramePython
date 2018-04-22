#!/usr/bin/python

var =100
if var:
    print ("Aceasta expresie este evaluata ca adevarata!");
    print (var)
else:
    print ("Aceata expresie este evaluata ca falsa!")
    print (var)
    
#evaluarea unei noi valori 0 = false
varFals = 0
if varFals:
    print("Aceasta expresie este evaluata ca adevarata!")
    print(varFals)
else:
    print("Aceasta expresie este evaluata ca falsa!")
    print(varFals)
   
# Python nu are switch/case dar poate fi utilizat elif
variabila = 4
if variabila == 2:
    print("Mai incearca sa ghicesti")
elif variabila ==3:
    print("Mai poti incerca chiar daca nu vezi acest mesaj")
elif variabila == 4:
    print("Ai ghicit chiar este:")
    print(variabila)
else:
    print("Nu te lasa!")
        
# nested if..elif ...else sunt posibile

# while declaratia
numara = 9
while numara > 0:
    print("Am inceput numaratoarea #: ", numara)
    numara = numara -1
    
# constructia while ...else
cont = 0
while cont < 5:
    print("Mai aveti in cont:",  cont, "lei.")
    cont=cont+1
else:
    print("EXECUTIE ELSE : Aveti in cont 5 lei.")
print("La revedere, programul s-a incheiat.")
