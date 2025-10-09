import os
os.system('cls') 
print("\n")

print("Sveika, 11.klase!")

while True:

    try:
        x = int(input("cik sunim gadu? "))
    

    except ValueError:
        print("ievadītais vecums nav skaitlis")
    else:
        break
        
print (f"vecums ir {x} ")



