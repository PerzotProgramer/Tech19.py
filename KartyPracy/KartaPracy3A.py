x = 10
gw = "*"
kr = "--"
pi = "||"
#zad1
print("ZADANIE 1")
for i in range(0, x):
    print("*-|",end = "")
print("")

#zad2 pre 1,2,3,4

#zad2 pre 1
for i in range(0, x):
    for j in range(0, i):
        print(gw, end="")
    print("")

#zad2 pre 2
for i in range(x, 0, -1):
    for j in range(i, 0, -1):
        print(gw, end="")
    print("")

#zad2 pre3
for i in range(x+1, 0, -1):
    for j in range(0, i):
        print(" ", end="")
        
    for j in range(0, x-i):
        print(gw, end="")
    print("")

#zad2 pre4
for i in range(0, x):
    for j in range(0, i):
        print(" ", end="")
        
    for j in range(0, x-i):
        print(gw, end="")
    print("")

#zad2
print("ZADANIE 2")
for i in range (1, x):
    print(gw + kr + gw + "*" + pi, end="")
    gw = gw + "**"
print()
#zad3
print("ZADANIE 3")
pi1 = "|"
gw1 = "*"
for i in range(1,x):
    print(gw1+pi1+gw1+kr, end="")
    pi1 += "||"
    kr += "--"
print()
print()

#pre - tab. mnożenia
print("\t\t\tPRE - TABLICZKA MNOŻENIA")
for i in range (1, 11):
    for j in range(1,11):
        print(i*j,end="\t")
    print()

#zad4
print("ZADANIE 4")
for i in range(1,x):
    for j in range(1,x):
        if j == i or j + i == x:
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()