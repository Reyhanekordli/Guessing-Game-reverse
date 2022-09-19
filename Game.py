import random
cguess = random.randint(1,99)
print(cguess)
k = 1
b = 99
c = 0
while (c != 1):
    answer = input("")
    if answer == "k":
        n = cguess
        b = n
        cguess = random.randint(k + 1,cguess - 1)
        c = 0
        print(cguess)
    if answer == "b":
        n = cguess
        k = n
        cguess = random.randint(cguess + 1,b - 1)
        c = 0
        print(cguess)
    if answer == "d":
        c = 1
