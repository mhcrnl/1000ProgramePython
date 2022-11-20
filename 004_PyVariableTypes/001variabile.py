#!/usr/bin/python
# primul program python variabile
    #STANDARD DATA TYPES: -Numbers
    #                                       -String
    #                                       -List = []
    #                                       -Tuple = ()
    #                                       -Dictionary = {'cheie':'valoare' , ...} 
    # del  -sterge variabila din memorie
    # * operatorul de repetitie
    # + operatorul de concatenare
dor = 100
km = 123.45
double = 23.34
nume = "Mihai Cornel"

print(dor)
print(km)
print(double)
#String
print(nume)
print (nume[0])
print(nume[0:7])
print(nume[5:8])
print(nume * 3)
print(nume * 3+" vasile ")
a=b=c=1
print (a); print(b); print(c)
a, b, c = 23,  56.67,  "Vasile"
print (a); print(b); print(c)
del a
#print(a)
#list []
lista=["abac",  "dero",  546.78,  234,  "cer",  'sau']
altaLista = ['Andei',  678,  90j]
print(lista)
print(lista[1])
print(lista[1:])
print(lista[1:] * 2)
print(lista + altaLista)
#Tuples = ()
tuples = (345,  345,  'varza') 
print(tuples)
#?Dictionary = {'cheie':'valoare'}
myDict = {'nume':'Cornel',  'prenume':'Mihai'}
print(myDict.keys())
print(myDict.values())
print(myDict['nume'])
a = "34"
print(a)
a = int(a)
print(a)
# input introduce valorile sub forma de string
# linia de mai jos asteapta input de la utilizator
input("Apasati orice tasta enter pt. a inchide: ")
