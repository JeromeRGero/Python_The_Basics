import sys

doneYet = 0

def q():
    global doneYet
    doneYet += 1
    valid = {
        "yes": True,
        "y": True,
        "ye": True,
        "no": False,
        "n": False
    }

    prompt = "#######################################\nContinue? [y/n]: "
    sys.stdout.write(prompt)

    a = 0

    if doneYet == 4:
        quit()

    while a == 0:
        choice = raw_input().lower()
        if a is not None and choice == "":
            return valid["yes"]
        elif choice in valid:
            if valid[choice] == True:
                sys.stdout.write("Continuing!\n")
                return
            else:
                quit()
        else:
            sys.stdout.write("Please respond with 'yes' or 'no' ('y' or 'n') \nContinue? [y/n]: ")



def odd_num():
    for i in range(1, 1000, 2):
        print(i)

def multis_o_five():
    for i in range(5, 1000000, 5):
        print(i)

a = [1, 2, 5, 10, 255, 3]

def sum_o_all(ls):
    total = 0
    for i in ls:
        total += i
    return total

def avg(ls):
    total = 0
    for i in ls:
        total += i
    return total / len(ls)

odd_num()
q()
multis_o_five()
q()
print sum_o_all(a)
q()
print avg(a)
