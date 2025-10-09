import os
os.system('cls') 
print("\n")

#skaitliskvadrata
def main():
    x = int(input(" x? "))
    print("skaitlis kvadrātā ir ", square(x))

def square(n):
    return n * n

if __name__ == "__main__":
    main()


