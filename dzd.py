import os
os.system('cls') 
print("\n")

#jebkurs datums
import pandas
from datetime import datetime
import ctypes

df = pandas.read_csv("saraksts.csv", sep=";", dtype=str)


datums = input("Ievadiet datumu ")
# today = datetime.today().strftime("%d.%m")


df["Dzimšanas datums"] = df["Dzimšanas datums"].str[:5]

bd_skoleni = df[df["Dzimšanas datums"]== datums]

print(bd_skoleni)

if not bd_skoleni.empty:
    teksts = "Sveicam dzimšanas dienā!!!\n\n"
    for _, row in bd_skoleni.iterrows():
        teksts += f"{row['Vārds'].upper()}\n{row['Klase'].upper()}\n{row['Deklarētā adrese'].upper()}\n\n"
else:
    teksts = "Šodien nav nevienam dzimšanas diena!!!"

ctypes.windll.user32.MessageBoxW(0,teksts.strip(), "svinam", 1)

#ritdiena
import pandas
from datetime import datetime, timedelta
import ctypes

df = pandas.read_csv("saraksts.csv", sep=";", dtype=str)

today = datetime.now()
tommorow = today + timedelta(1)
diena = tommorow.strftime("%d.%m")


df["Dzimšanas datums"] = df["Dzimšanas datums"].str[:5]

bd_skoleni = df[df["Dzimšanas datums"]== diena]

print(bd_skoleni)

if not bd_skoleni.empty:
    teksts = "Sveicam dzimšanas dienā!!!\n\n"
    for _, row in bd_skoleni.iterrows():
        teksts += f"{row['Vārds'].upper()}\n{row['Klase'].upper()}\n{row['Deklarētā adrese'].upper()}\n\n"
else:
    teksts = "Šodien nav nevienam dzimšanas diena!!!"

ctypes.windll.user32.MessageBoxW(0,teksts.strip(), "svinam", 1)