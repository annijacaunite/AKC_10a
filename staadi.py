import os
os.system("cls")
print("\n")
import os
os.system("cls")
print("\n")
dārzeņu_cenas = {
    'tomāti': 0.11,
    'kāposts': 0.09,
    'burkans': 0.35,
    'kartupeļi': 0.15,
    'arbūzs': 0.59,
    'pipari': 0.25,
    'gurķi': 0.19,
    'ķirbis': 0.45,
    'pupas': 0.29,
    'zirņi': 0.19,
    'bietes': 0.25,
    'kabači': 0.55,
    'cukīni': 0.49,
    'kukurūza': 0.39,
    'sīpoli': 0.20,
    'ķiploki': 0.19
}
stādu_izmērs = {
    'tomāti': 0.2,
    'kāposts': 0.2,
    'burkans': 0.3,
    'kartupeļi': 0.1,
    'arbūzs': 0.4,
    'pipari': 0.2,
    'gurķi': 0.2,
    'ķirbis': 0.4,
    'pupas': 0.2,
    'zirņi': 0.2,
    'bietes': 0.2,
    'kabači': 0.3,
    'cukīni': 0.4,
    'kukurūza': 0.2,
    'sīpoli': 0.1,
    'ķiploki': 0.1
}
dārzeni = input("Kādus dārzeņus vēlies iestādīt? Atdaliet tos ar komatiem (piemēram: tomāti, gurķi, kāposts): ").lower().split(',')
zeme = float(input("Cik daudz zemes tev ir (kvadrātmetros)? "))
kopējās_izmaksas_kopā = 0
print("=" * 30)
for dārzenis in dārzeni:
    dārzenis = dārzenis.strip()
    if dārzenis not in dārzeņu_cenas:
        print(f"Šāds dārzenis ({dārzenis}) nav pieejams. Lūdzu, izvēlies citu.")
        continue
   
    platība_per_stādu = stādu_izmērs[dārzenis]
    cena_per_stādu = dārzeņu_cenas[dārzenis]
   
    max_stādi = int(zeme // platība_per_stādu)
    kopējās_izmaksas = max_stādi * cena_per_stādu
   
    print(f"{dārzenis.capitalize()}:")
    print(f"  Maksimālais stādu skaits: {max_stādi}")
    print(f"  Kopējās izmaksas: {kopējās_izmaksas:.2f} EUR")
   
    kopējās_izmaksas_kopā += kopējās_izmaksas
print("=" * 30)
print(f"Kopējās izmaksas par visiem stādiem: {kopējās_izmaksas_kopā:.2f} EUR")
ieteikumi = input("Vai vēlies ieteikumu par stādiem? (jā/nē): ").lower()
if ieteikumi == "jā":
    print("\nIeteikumi par stādiem:")
    print("-" * 30)
    print(f"Uzirdini augsni: Uzrušini augsni, lai saknēm būtu vieglāk iesakņoties. Ideāli būtu uzrušināt līdz 20-30 cm dziļumam.")
    print(f"Uzlabo augsni: Ja augsne ir vāja, bagātini to ar kompostu vai dabīgajiem mēslojumiem, piemēram, kūtsmēsliem.")
    print(f"Atceries sezonu: Pārliecinies, ka stādi tiek stādīti laikā, kad augs var labi iesakņoties un augt.")
    print("-" * 30)
else:
    print("Labi, ieteikumi netiks izvadīti.")