#!/usr/bin/python

import sys

file_name = "python.txt"
file_finish = ","
try:
    #open file stream
    file = open(file_name, "w")
except IOError:
    print("Este o eroare la deschidera filei: ", file_name)
    sys.exit()
    
print("Enter '",  file_finish, )
