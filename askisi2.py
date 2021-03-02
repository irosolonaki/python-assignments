import random
from random import randint

def fib(n):
    if n == 0:
        return 0
    elif n ==1:
        return 1
    elif n > 1:
        return fib(n-1) + fib(n-2)
    
n = int(input("Δώστε έναν αριθμό: "))
number = fib(n)
print("Ο όρος ακολουθίας fibonacci που του αντιστοιχεί ειναι:", number)
boolean = True
if (number < 2):
    boolean = False
if (number==2 or number==3):
    boolean = True
if number>3:
    for i in range(0,20):      
        a = randint(2, n-1)
        if (pow(a,n-1,n) != 1):
            boolean = False
if boolean == True:
    print("Είναι πρώτος")
else:
    print("Δεν είναι πρώτος")

