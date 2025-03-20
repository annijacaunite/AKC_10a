import os
os.system('cls') 
print("\n")

skolens = ["Viktorija", "Artūrs", "Džošua", "Roberts"]
# print(skolens)

# print(skolens[0])
# print(skolens[1])

# for sk in skolens:
#     print(sk)

# skola = "25.vidusskola"
# for burts in skola:
#     print(burts)

# for i in range(len(skolens)):
#     print(i + 1,skolens[i]) #range-ipilda darbibas tik,cik ir

#divdimensiju_saraksts = vardnica
#zenītu artilērija

# skolotajs = ["Gustava", "Ungure", "Deksne", "Gladčenko"]
# macibu_prieksmets = ["matemātika", "matemātika", "matemātika", "fizika"]
# #macibuPrieksmets=camelcase macibu_prieksmets=snakecase

# skolotajs = {
#     "Gustava": "matemātika", 
#     "Ungure": "matemātika", 
#     "Deksne": "matemātika", 
#     "Gladčenko": "fizika", 
# }

# print(skolotajs["Deksne"])
# print(skolotajs["Gladčenko"])

# for skol in skolotajs:
#     print(skol, skolotajs[skol], sep=" māca ")

#kautkasneiet
# skolotajs = [
#     {"uzvards": "Gustava", "macību priekšmets" : "matemātika", "kabinets": "27. "}
#     {"uzvards": "Ungure", "macību priekšmets" : "matemātika", "kabinets": "205. "}
#     {"uzvards": "Deksne", "macību priekšmets" : "matemātika", "kabinets": None }
#     {"uzvards": "Gladčenko", "macību priekšmets" : "matemātika", "kabinets": "206. "}
# ]

# for skol in skolotajs:
#     print(skol["uzvards"], skol["macību priekšmets"], skol ["kabinets"], sep=",")


platums = int(input("platums- "))
augstums = int(input("augstums- "))

for i in range(augstums):
    for j in range(platums):
        print("@", end="")
    print()