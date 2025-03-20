import os
os.system('cls') 
print("\n")


import requests
from bs4 import BeautifulSoup
from plyer import notification

url = "https://www.myfitness.lv/occupancy/"

def get_results_data(url):
    try:
        r = requests.get(url, timeout=10)
        r.raise_for_status() #parbauda,vai veiksmigs pieprasijums
        return r.text
    except requests.exceptions.RequestException as e:
        print(f"Kļūda: {e}")
        return None
    
htmldata = get_results_data(url)

if htmldata:
    soup = BeautifulSoup(htmldata, "html.parser")
    # print(soup.prettify())
    procenti_elem = soup.find("div", {"class": "location"})
    location_elem = soup.find("span", {"data-testid": ""})
    

    procenti = procenti_elem.text if procenti_elem else "Nav datu"
    location = location_elem.text if location_elem else "Nav datu"
   

    result = f"Kluba kapacitāte: {procenti}"

    notification.notify(
        title = "Kluba informācija",
        message = result,
        timeout = 10
    )
else:
    notification.notify(
        title = "Kļūda",
        message = "Nekas nav zināms!!!",
        timeout = 10
    )


