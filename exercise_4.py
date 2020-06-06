women = ['Ala', 'Ola']
man = ['Piotr', 'Paweł']

name = input("Jak masz na imię?\n")
if name in women:
    print("Żeńskie")
elif name in man:
    print("Męskie")
else:
    print("Nie znamy tego imienia")
    male_female = input("To imię męskie czy żeńskie?\n")
    if male_female == "żeńskie":
        women.append(name)
    elif male_female == "męskie":
        man.append(name)

print("Znane imienia meskie:", man)
print("Znane imienia żeńskie:", women)
