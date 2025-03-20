import os
os.system('cls') 
print("\n")

#1uzd
parole = input("Ievadi paroli")
print(parole)
if len(parole) < 9:
    print("Parolei jābūt vismaz 9 simboli")
if burti != parole:
    print("Parolei jāsatur vismaz 1 lielais burts")




#2uzd
#visigadigariegadinesanacaman
import math
gads = int(input("Ievadi gadu "))
if gads % 400 or 4:
    print("Tas ir garais gads")
elif gads % 100:
    print("Tas ir īsais gads")

#pameginajuvelsavadakbetnesanaca
# gads = input("Ievadi gadu")
# if gads // 400 or 4:
#      print("Tas ir garais gads")
# else:
#      print("Tas ir īsais gads")

# gads = int(input("Ievadi gadu "))










 #3uzd

vecums = int(input("Cik gadi?: "))
if vecums < 7:
     print("Biļete ir bez maksas")
elif vecums >= 7 and vecums <18:
     print("Biļete maksā 5 eiro")
elif vecums >18 and vecums >65:
     print("Biļete maksā 10 eiro")
elif vecums <65:
     print("Biļete maksā 3 eiro")

#4uzd
import math
x = int(input("Ievadi skaitli : "))
if x<0:
    print("Skaitlis ir negatīvs")
elif x==0:
    print("Skaitlis ir 0")
elif x>0:
    print("Skaitlis ir pozitīvs")
if x%2:
    print("Skaitlis ir nepāra")
else:
    print("Skaitlis ir pāra")

#papilduzd
#nepaspejunesanaca
import math
number = float(input("Ievadi skaitli: "))
print(f"Skaitlis noapaļots līdz diviem cipariem aiz komata: {round(number, 2)}")





