a = int(input("Podaj długość boku "))
b = int(input("Podaj długość boku "))
c = int(input("Podaj długość boku "))

if a + b > c and a + c > b and b + c > a:
    print("Można utworzyć trójkąt")
    if b < a > c:
        a = c
        c = a
        if a**2 + b**2== c**2:
            print("Trójkąt pitagorejski")
    if a < b > c:
        b = c
        c = b
        if a ** 2 + b ** 2 == c ** 2:
            print("Trójkąt pitagorejski")
    if a ** 2 + b ** 2 == c ** 2:
        print("Trójkąt pitagorejski")
    else:
        print("Trójkąt niepitagorejski")
else:
    print("Nie można utworzyć trójkąta")
