import os
os.system('cls') 
print("\n")

#uzd
#reksisrej
# suna_vards = "Reksis"
# suna_krasa = "Brūna"

# def riet(vards):
#     print(f"{vards} sāk riet latviski - Vau-vau! ")

# riet(suna_vards)



#uzd
#OOP
#klase - plāns priekš objektiem (piemērs ar savām īpašībām un metodēm)
# class Suns:
#     name = ""
#     suga = ""
#     vecums = 0

#konstruktors - metode, kas izpildās automātiski, kad tiek izveidots objekts no klases
#         suns1.name = name
#         suns1.suga = suga
#         suns1.vecums = vecums
# suns1 = Suns()
# suns1.name = "Reksis"
# suns1.suga = "Vācu aitu suns"
# suns1.vecums = 3

# suns2 = Suns()
# suns2.name = "Makss"
# suns2.suga = "Labradors"
# suns2.vecums = 5

# print(f"Pirmais suns - vārds: {suns1.name}, suga: {suns1.suga}, vecums: {suns1.vecums} gadi")
# print(f"Otrais suns - vārds: {suns2.name}, suga: {suns2.suga}, vecums: {suns2.vecums} gadi")


#uzd
# class Persona:
#     def __init__(self, vards, vecums):
#         self.vards = vards
#         self.vecums = vecums

#     def sveicinaties(self):
#         print(f"Sveiki! Mani sauc {self.vards} un man ir {self.vecums} gadi.")  

# janis = Persona("Jānis", 30)
# peteris = Persona("Pēteris", 25)

# janis.sveicinaties()
# peteris.sveicinaties()


#uzd
#uzd metode - drukāt, klase Printeris
# class Printeris:
#     def drukat(self):
#         print("Drukājam dokumentu...")

# skolas_printeris = Printeris()
# skolas_printeris.drukat()


#uzd
#uzd metode - skaitļi, klase Skaitītājs
# class Skaititajs:
#     def skaitli(self, n):
#         for i in range(1, n + 1):
#             print(i)

# skaititajs1 = Skaititajs()
# sk = int(input("Ievadi skaitli! : "))
# skaititajs1.skaitli(sk)

#uzd
class Dators:
    def __init__(self,  modelis, ram_gb):
        self.modelis = modelis
        self.ram_gb = ram_gb

    def parbadi_speju(self):
        if self.ram_gb >= 16:
            return "Lieliski spējīgs!"
        else:
            return "Der vienkāršiem darbiem."
        
mans_dators = Dators("Dell XPS", 32)
skolnieka_dators = Dators("HP Pavilion", 8)
print(f"Mans dators ir {mans_dators.modelis} ar {mans_dators.ram_gb}GB RAM. {mans_dators.parbadi_speju()}")
print(f"Skolnieka dators ir {skolnieka_dators.modelis} ar {skolnieka_dators.ram_gb}GB RAM. {skolnieka_dators.parbadi_speju()}")



 
        

    
