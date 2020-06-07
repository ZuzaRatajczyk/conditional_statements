a = int(input("Podaj długość boku: "))
b = int(input("Podaj długość boku: "))
c = int(input("Podaj długość boku: "))

tringle = [a,b,c]
tringle.sort() #sortuje liczby od najmniejszej do największej
a = tringle[0]
b = tringle[1]
c = tringle[2]

if a + b > c and a + c > b and b + c > a:
    print("Można utworzyć trójkąt")
    if a**2 + b**2 == c**2:
        print("Trójkąt pitagorejski")
        if a/3 == b/4 == c/5:
            print("Trójkąt egipski")
    else:
        print("Trójkąt niepitagorejski")
else:
    print("Nie można utworzyć trójkątu")
