import sys

def checkerboard():
    for i in range(0, 8):
        if i % 2 == 0:
            print("* * * * ")
        else:
            print(" * * * *")

def q():
    a = 0
    while a == 0:
        sys.stdout.write("Continue? [y/n] : ")
        choice = raw_input().lower()
        if 'y' in choice:
            print("Continuing!\n")
            return
        elif 'n' in choice:
            print("Kk, exiting program!")
            quit()
        else:
            print("Please enter yes, y, n, or no!\n")

def odd_even():
    for i in range(1, 2000):
        if i%2 == 0:
            x = str(i)
            print("Number is {}. This is an even number.".format(x))
        else:
            x = str(i)
            print("Number is {}. This is an odd number.".format(x))

a = [2,4,10,16]

def multi(ls):
    for i in enumerate(ls):
        # I know the next statement is really really weird,
        # but I am just testing the waters here.
        ls[i[0]] *= 5
    return ls

def challenge(ls, fun):
    fun(ls)
    nls = []
    for mi in ls:
        i = mi
        z = []
        while i > 0:
            z.append(1)
            i -= 1
        nls.append(z)
    return nls


x = [1, 3, 2]

odd_even()
q()
print multi(a)
q()
print challenge(x, multi)
print("Thank you for playing!")
q()
