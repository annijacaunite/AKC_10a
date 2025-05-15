import os
os.system('cls') 
print("\n")

import csv

# with open("saraksts.csv", "r", encoding='iso-8859-1') as file:
#     reader = csv.DictReader(file)
#     # next(reader)
#     for row in reader:
#         # kolonna= row["saprotam?k? valoda"]
#         # print(kolonna)
#         print(row["saprotam?k? valoda"])

# with open("saraksts.csv", "r", encoding='iso-8859-1') as file:
#     reader = csv.DictReader(file)
    # python = 0
    # scratch = 0 
    # html = 0
    # var ari python, scratch, html = 0, 0, 0
#     for row in reader:
#         rinda = row["saprotam?k? valoda"]
#         if rinda == "Python":
#             python +=1
#         elif rinda == "Scratch":
#             scratch +=1
#         elif rinda == "HTML+CSS+JS":
#             html +=1
# print(f"Python-u mīl {python}")
# print(f"Scratchu-u mīl {scratch}")
# print(f"HTML+CSS+JS mīl {html}")
with open("saraksts.csv", "r", encoding='cp1252') as file:
    reader = csv.DictReader(file)
    viss_saraksts = {} #tuksa vardnica = {}
    for row in reader:
        rinda = row["saprotam?k? valoda"]
        if rinda  in viss_saraksts:
            viss_saraksts[rinda] += 1
        else:
            viss_saraksts[rinda] = 1
for rinda in sorted(viss_saraksts, key=viss_saraksts.get, reverse=True):
    print(f"{rinda}: {viss_saraksts[rinda]}")