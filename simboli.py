#otraisuzd
divi = input("ieraksti kaut ko")
divi = divi.lower()
divi = divi.upper()
print(divi.lower())
print(divi.upper())
 
 #jaunsuzd
vards = input("ieraksti kaut ko")
viens = input("ieraksti simbolu")
print("vards,viens")

#parbaudeuzd
#pirmaisuzd
string = input("Ievadi simnolu virkni: ")
print(f"Simbolu virknes garums: {len(string)}")
#figurfunkcija- {},len-garums,string-mainiga vertiba

#otrais uzd
string = input("Ievadi simnolu virkni: ")
print(f"Simbolu virknes garums: {len(string)}")

print(f"Virkne ar lielajiem burtiem: {string.upper()}")
print(f"Virkne ar mazajiem burtiem: {string.lower()}")

#tresaisuzd
symbol = input("Ievadi simbolu,ko lietot tukšo vietu aizvietošanai: ")
print(f"Aizvietotas atstarpes: {string.replace(' ', symbol)}")

#ceturtaisuzd
word_to_check = "Python"
print(f"Vai virkne satur vārdu '{word_to_check}'? {'Python'in string}")
#string-mainiga nosaukums

print(f"Pirmie pieci simboli: {string[2:5]}")
print(f"Pēdējie trīs simboli:{string[-3:]}")

#sestaisuzd
number = float(input("Ievadi skaitli: "))
print(f"Skaitlis noapaļots līdz diviem cipariem aiz komata: {round(number, 2)}")

#septitaisuzd
integer = int(input("Ievadi veselu skaitli: "))
print(f"Skaitlis kā decimāldaļa: {float(integer)}")

#nezinukurzuzd
number - int(input("Ievadi lielu skaitli: "))
print(f"Skaitlis ar tūkstošu atdalītāju: {large_number:,}".replace(','))

#devitaisuzd

print(f"Skaitlis binārajā sistēmā:{bin(integer)[2:]}")
print(f"Skaitlis oktālajā sistēmā:{oct(integer)[2:]}")
print(f"Skaitlis heksadecimālajā sistēmā:{hex(integer)[2:]}")

#desmitaisuzd
negative_number = int(input("Ievadi negatīvu skaitli: "))
print(f"Absolūtā vērtība: {abs(negative_number)}")
