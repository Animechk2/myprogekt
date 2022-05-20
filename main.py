# import math
# import pyowm
a = 1
p = 0
c = 0


def start():
    b = 1
    while (b == 1):
        print("vuberete destvie 1) pogoda 2) kalkulator")
        p = int(input())
        if (p == 1 or p == 2):
            b == 0
            return p
        else:
            print("vubirete pravilnoe deystvie")
            return p


def kalkulator():
    print("plus-1")
    print("minus-2")
    print("umnogut-3")
    print("podilit-4")
    print("kvadrat-5")
    print("korin-6")
    c = int(input())
    if (c > 7 and c < 0):
        print("vuberite predlogunoe deystvie")
    return c


def deystvie(c):
    r = 0
    if (c == 1):
        a = int(input("vedite pervoe chislo"))
        b = int(input("vedite vtoroe chislo"))
        print(a + b)

    if (c == 2):
        a = int(input("vedite pervoe chislo"))
        b = int(input("vedite vtoroe chislo"))
        print(a - b)

    if (c == 3):
        a = int(input("vedite pervoe chislo"))
        b = int(input("vedite vtoroe chislo"))
        print(a * b)

    if (c == 4):
        a = int(input("vedite pervoe chislo"))
        b = int(input("vedite vtoroe chislo"))
        print(a / b)

    if (c == 5):
        a = int(input("vedite pervoe chislo kotoroe vathvesti v kvadrat: "))
        print(a ** 2)

    # c == 6
    # a = int(input("vedite pervoe chislo kotorogo vucheslit korin"))
    # print(str(math.sqrt(a)))


def finish():
    print("1) prodolgut 2)thavershut")
    x = int(input())
    if (x >= 3):
        print("vuberite pravilnoe deistvie")

    if (x == 2):
        a = 2
    else:
        a = 1
    return a


while (a == 1):
    p = start()
    if (p == 2):
        c = kalkulator()
    deystvie(c)
    a = finish()