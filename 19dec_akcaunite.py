import os
os.system('cls') 
print("\n")
 
#  #1variants
# def hello(kam):
#     print("hello ", kam)

# name = input("Kā tevi sauc?")
# hello(name) #f-ja tikai izdruka hello

# #2variants
# def hello():
#     print("hello")

# name = input("Kā tevi sauc?")
# hello() 
# print(name)
 
 #velvienspiemers
# def hello(kam="skola"):
#     print("hello ", kam)

# hello()
# name = input("Kā tevi sauc?")
# hello(name)

#velviensvariants
# def main():
#     name = input("kā tevi sauc?")
#     hello(name)

# def hello(kam="skola"):
#     print("hello, ", kam)

# main()

#uzd
def main():
    x = int(input("x - ?"))
    print("x kvadrātā ir", kvadrats(x))

def kvadrats(n):
    return n * n

main()





