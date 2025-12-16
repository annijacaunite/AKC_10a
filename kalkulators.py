import os
import math

os.system('cls')
print("\n")

class Kalkulators:  # vecākklase
    def saskaitisana(self, sk1, sk2):  # definē saskaitīšanu
        return sk1 + sk2

    def atnemsana(self, sk1, sk2):  # definē atņemšanu
        return sk1 - sk2

    def reizinana(self, sk1, sk2):  # definē reizināšanu
        return sk1 * sk2

    def dalisana(self, sk1, sk2):  # definē dalīšanu
        if sk2 == 0:  # ja skaitlis = ar 0
            return "Dalīšana ar nulli nav iespējama!"  
        return sk1 / sk2

def sakuma_izvelne():
    while True:
        print("KALKULATORS")
        print("1. Saskaitīšana")
        print("2. Atņemšana")
        print("3. Reizināšana")
        print("4. Dalīšana")
        print("5. Iziet")
def sakuma_izvelne():
    kalkulators = Kalkulators()
    while True:
        try:
            print("KALKULATORS")
            print("1. Saskaitīšana")
            print("2. Atņemšana")
            print("3. Reizināšana")
            print("4. Dalīšana")
            print("5. Iziet")
            izvele = input("Izvēlieties 1-5: ")
            if izvele == "5":
                print("Paldies, ka izmantojāt kalkulatoru!")
                break
            sk1 = float(input("Ievadi pirmo skaitli: "))
            sk2 = float(input("Ievadi otro skaitli: "))

            if izvele == "1":
                rezultats = kalkulators.saskaitisana(sk1, sk2)
                print(f"Rezultāts: {sk1} + {sk2} = {rezultats}")
            elif izvele == "2":
                rezultats = kalkulators.atnemsana(sk1, sk2)
                print(f"Rezultāts: {sk1} - {sk2} = {rezultats}")
            elif izvele == "3":
                rezultats = kalkulators.reizinana(sk1, sk2)
                print(f"Rezultāts: {sk1} × {sk2} = {rezultats}")
            elif izvele == "4":
                rezultats = kalkulators.dalisana(sk1, sk2)
                print(f"Rezultāts: {sk1} ÷ {sk2} = {rezultats}")
            else:
                print("Nederīga izvēle. Lūdzu ievadiet ciparu no 1 līdz 5.")
                continue
            atkartot = input("\nVēlaties atkārtot operāciju? (j/n): ").lower()
            if atkartot != "j":
                break
        except ValueError:
            print("Lūdzu ievadiet derīgu skaitli!")

    def kvadratsakne(self, skaitlis):  # definē kvadrātsakni
        if skaitlis < 0:
            return "Kļūda: Nevar aprēķināt negatīva skaitļa kvadrātsakni!"
        return math.sqrt(skaitlis)

    def sakuma_izvelne(self):  # polimorfisms
        while True:
            print("ZINĀTNISKAIS KALKULATORS")
            print("1. Saskaitīšana")
            print("2. Atņemšana")
            print("3. Reizināšana")
            print("4. Dalīšana")
            print("5. Kvadrātsakne")
            print("6. Iziet")
            try:
                izvele = input("Izvēlieties 1-6: ")
                if izvele == "6":
                    print("Paldies, ka izmantojāt zinātnisko kalkulatoru!")
                    break
                elif izvele == "5":
                    skaitlis = float(input("Ievadi skaitli: "))
                    rezultats = self.kvadratsakne(skaitlis)
                    print(f"Rezultāts: √{skaitlis} = {rezultats}")
                else:
                    sk1 = float(input("Ievadiet pirmo skaitli: "))
                    sk2 = float(input("Ievadiet otro skaitli: "))
                    if izvele == "1":
                        rezultats = self.saskaitisana(sk1, sk2)
                        print(f"Rezultāts: {sk1} + {sk2} = {rezultats}")
                    elif izvele == "2":
                        rezultats = self.atnemsana(sk1, sk2)
                        print(f"Rezultāts: {sk1} - {sk2} = {rezultats}")
                    elif izvele == "3":
                        rezultats = self.reizinana(sk1, sk2)
                        print(f"Rezultāts: {sk1} × {sk2} = {rezultats}")
                    elif izvele == "4":
                        rezultats = self.dalisana(sk1, sk2)
                        print(f"Rezultāts: {sk1} ÷ {sk2} = {rezultats}")
                    else:
                        print("Lūdzu ievadi ciparu no 1 līdz 6.")
                        continue
                atkartot = input("\nVēlaties atkārtot operāciju? (j/n): ").lower()
                if atkartot != "j":
                    break
            except ValueError:
                print("Lūdzu ievadiet derīgu skaitli!")
