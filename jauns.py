import os
os.system('cls') #attīra termināla logu pašā sākumā
print("\n") #ieliek tukšu rindiņu pirms izdrukas

# x = int(input("Kāda ir x vērtība? "))
# y = int(input("Kāda ir y vērtība? "))

# if x != y:
#     print("x nav vienāds ar y") #ja nestrādā if,var elif,vai else
# else:
#     print("x ir vienāds ar y") #divi == salīdzina

# punkti = int(input("Punkti: "))

# if punkti >=90 and punkti <= 100:
#     print("Vērtējums: 10")
# elif punkti >=80 and punkti < 90:
#     print("Vērtējums: 9")
# elif punkti >=70 and punkti < 80:
#     print("Vērtējums: 8")
# elif punkti >=60 and punkti < 70:
#     print("Vērtējums: 7")
# else:
#     print("Vērtējums: n/v")

import math
a = int(input("koeficents a: "))
b = int(input("koeficents b: "))
c = int(input("koeficents c: "))

D = b**2-4*a*c
print(D)

if D < 0:
    print("sakņu nav")
elif D == 0:
    print("viena sakne")
else:
    print("divas saknes")
