import os
os.system('cls') 
print("\n")
 #cls
# struktureti dati ,piem. - tabula (excel) 
# csv - coma seperate value
# xml lauj saglabat ar parametriem
# jabut viienlidzigam info,kolonnas,par vienu objektu

import pandas
from datetime import datetime
import ctypes

# df - datu fails
df = pandas.read_csv("saraksts.csv", sep=";", dtype=str)

# print(df)
# print(df.to_string())
datums = input("Ievadi datumu")
today = datetime.today().strftime("%d.%m")
# % - divi cipari

df["Dzimšanas datums"] = df["Dzimšanas datums"].str[:5]

bd_skoleni = df[df["Dzimšanas datums"]== today]

print(bd_skoleni)

if not bd_skoleni.empty:
    teksts = "Sveicam dzimšanas dienā!!!\n\n"
    for _, row in bd_skoleni.iterrows():
        teksts += f"{row['Vārds'].upper()}\n{row['Klase'].upper()}\n{row['Deklarētā adrese'].upper()}\n\n"
else:
    teksts = "Šodien nav nevienam dzimšanas diena!!!"

ctypes.windll.user32.MessageBoxW(0,teksts.strip(), "svinam", 1)