#!/usr/bin/python3

import random
import sys

print("Introduceti numele DVS.:")
name = input()

secretNumber = random.randint(1, 20)

print("Salut, " + name +" , ghiceste un numar intre 1 si 20")

for guessesTaken in range(1,7):
    guess = int(input())

    if guess < secretNumber:
        print("Numarul tau este prea mic. Incearca din nou!")
    elif guess > secretNumber:
        print("Numarul tau este prea mare. Incearca din nou!")
    elif guess == secretNumber:
        print("Corect! Ati reusit dupa "+str(guessesTaken)+" incercari.")

        sys.exit()

print("Regret, ati avut " +str(guessesTaken)+" incercari. Doriti sa continuati? da sau nu:")

answer = str(input())
if answer == "da":
    print("Numarul a fost: " +str(secretNumber)+" !")
else:
    print("Asta este!")


