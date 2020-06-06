a = 9
b = 2
c = 3

if b < a > c:    # a is highest of all numbers
    if b > c:
        print(a,b,c)
    else:
        print(a,c,b)
elif a < b > c:  # b is highest of all numbers
    if a > c:
        print(b,a,c)
    else:
        print(b,c,a)
else:            # c is highest of all numbers
    if a > b:
        print(c,a,b)
    else:
        print(c,b,a)