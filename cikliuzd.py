import os
os.system('cls') 
print("\n")

#1uzd
import math

for n in range(1, 10000):
    summa = 0
    for i in range(1, n):
        if n % i == 0:
            summa = summa + i
    if summa == n :
        print(f"{n} ir perfekts skaitlis")