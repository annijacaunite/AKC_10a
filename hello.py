print("Sveika pasaule!!!")
print(7+6)
print((1+4)*2)
print((738*273)**2)
print("Sveika,Annija!")


print('Sveiks, "labo skolēn"!')
print("hello, \"friend\"")
print("Annija", "Caunīte", sep='?????')

name = input("Kā tevi sauc? ")

name = name.strip().title()

pirmais,otrais = name.split(" ")

print("Sveiks,", name)
print(f"Sveiks, {name}")