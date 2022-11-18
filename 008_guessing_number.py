import math
import random

r1= int(input("Enter your lower bound: ")) # Lower bound
r2 = int(input("Enter your upper bound: ")) # Upper bound
print("Your range is from",r1,"to",r2)

x = random.randint(r1,r2) # randint to generate random number between given range
y = math.log(r2-r1+1,2)
# print(x)
print("You have only",round(y),"chances to guess the current number")
counter = 0 # To count number of guesses

while counter < y:
    counter+=1
    
    guess = int(input("Guess the number: "))

    if x == guess:
        print("Congratulations, you did it on",counter,"try")
        break
    elif x > guess:
        print("Try Again! You guessed too small!")
    elif x < guess:
        print("Try Again! You guessed too high!")
        
if counter>=y:
    print('\nThe number is %d'%x)
    print('\n\tBetter luck next time!')
