import os
os.system('cls') 
print("\n")

while True: 
        try: 
            dala= input("Daļa: ") 
            x, y = dala.split("/") 
            x = int(x) 
            y = int(y) 
            
            if y == 0: 
                print("Daļā nevar būt 0")
                continue
            if x > y: 
                 print("Daļas skaitītājs nevar būt lielāks par saucēju")
            
            percentage = round((x / y) * 100) 
            
            if percentage <= 1: 
                print("E") 
            elif percentage >= 99: 
                print("F") 
            else: 
                print(f"{percentage}%") 
            
            break 
        except (ValueError, ZeroDivisionError): 
                
                continue