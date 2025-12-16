import os
os.system('cls') 
print("\n")

import pandas
import ctypes

# df = pandas.read_csv("antidopings.csv", sep=",", dtype=str)

izvele = int(input("Izvēlies,ko vēlies noskaidrot: \n\n 1. Atfiltrēt un parādīt vielas, kas aizliegtas ārpus sacensībām ar iespēju saglabāt jaunā failā \n\n 2. Atfiltrēt un parādīt vielas, kas aizliegtas sacensību laikā ar iespēju saglabāt jaunā failā \n\n 3. Pēc nosaukuma ievades, jāparāda viela/vielas, ar to īpašībām, kas minētas sarakstā. \n\n 4.  Jāparāda tie sporta veidi, kuros ir reģistrēts īpašs aizliegums"))