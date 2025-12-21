import os
import math

class Kalkulators:
  
    
    def saskaitisana(self, sk1, sk2):
        return sk1 + sk2
    
    def atnemsana(self, sk1, sk2):
        return sk1 - sk2
    
    def reizinana(self, sk1, sk2):
        return sk1 * sk2
    
    def dalisana(self, sk1, sk2):
        if sk2 == 0:
            return "Dalīšana ar nulli nav iespējama!"
        return sk1 / sk2
    
    def sakuma_izvelne(self):
        while True:
            print("KALKULATORS")
            print("1. Saskaitīšana")
            print("2. Atņemšana")
            print("3. Reizināšana")
            print("4. Dalīšana")
            print("5. Iziet")
            
            try:
                izvele = input("Izvēlies 1-5 ")
                
                if izvele == "5":
                    print("Paldies, ka izmantoji kalkulatoru!")
                    break
                
                sk1 = float(input("Ievadi pirmo skaitli: "))
                sk2 = float(input("Ievadi otro skaitli: "))
                
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
                    print("Lūdzu ievadiet ciparu no 1 līdz 5.")
                    continue
                
                atkartot = input("Vēlies atkārtot operāciju? (ja/ne): ").lower()
                if atkartot != "ja":
                    break
            
            except ValueError:
                print("Kļūda: Lūdzu ievadiet derīgus skaitļus.")


class ZinatniskaisKalkulators(Kalkulators):
    
    
    def kvadratsakne(self, skaitlis):
        
        if skaitlis < 0:
            return "Nevar aprēķināt negatīva skaitļa kvadrātsakni!"
        return math.sqrt(skaitlis)
    
    def sakuma_izvelne(self):
        while True:
            print("ZINĀTNISKAIS KALKULATORS")
            print("1. Saskaitīšana")
            print("2. Atņemšana")
            print("3. Reizināšana")
            print("4. Dalīšana")
            print("5. Kvadrātsakne")
            print("6. Iziet")

            
            try:
                izvele = input("Izvēlies : 1-6 ")
                
                if izvele == "6":
                    print("Paldies, ka izmantoji zinātnisko kalkulatoru!")
                    break
                
                if izvele == "5":
                    skaitlis = float(input("Ievadi skaitli: "))
                    rezultats = self.kvadratsakne(skaitlis)
                    print(f"Rezultāts: √{skaitlis} = {rezultats}")
                else:
                    sk1 = float(input("Ievadi pirmo skaitli: "))
                    sk2 = float(input("Ievadi otro skaitli: "))
                    
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
                        print("Lūdzu ievadiet ciparu no 1 līdz 6.")
                        continue
                
                atkartot = input("Vēlies atkārtot  (ja/ne): ").lower()
                if atkartot != "ja":
                    break
            
            except ValueError:
                print("Lūdzu ievadi derīgus skaitļus.")