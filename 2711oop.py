import os
os.system('cls') 
print("\n")

class Transportlidzeklis:
    def __init__(self, marka, gads):
        self.marka = marka
        self.gads = gads
    def info(self):
        print(f"Marka{self.marka}, izlaiduma gads{self.gads}.")

    