import os
os.system('cls') 
print("\n")



#viensnorisinajuiem

ievade = input("ievadi numuru")
numuri = ievade.split(',')

for numurs in numuri:
    numurs = numurs.strip()

    if len(numurs) < 4 or '-' not in numurs:
        print(f"{numurs}: Numura zīme nav derīga.")
        continue

    burti, cipari = numurs.split('-')

    if len(burti) != 2 or not all(burts.isalpha() and burts in "ABCDEFGHIJKLMNOPRSTUVZ" for burts in burti.upper()):
        print(f"{numurs}: Numura zīme nav derīga.")
        continue

    if not cipari.isdigit() or not (1 <= int(cipari) <= 9999):
        print(f"{numurs}:Numura zīme nav derīga.")
        continue

print(f"{numurs}: Numura zīme ir derīga.")

