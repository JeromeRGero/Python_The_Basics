import sys

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


def figure_out(ls):
    for g in ls:
        if isinstance(g, int):
            if g >= 100:
                print("Thats a BIG number!\n")
            else:
                print("Small... so very small.\n")
        elif isinstance(g, str):
            if len(g) >= 50:
                print("Long sentance...")
            else:
                print("Short and to the point! I like it.\n")
        elif isinstance(g, list):
            if len(g) >= 10:
                print("That is a lot of data!")
            else:
                print("A short list, but still a list!")
        else:
            print ("What???\n")


def symetr(a, b):
    if a == b:
        print("They is am are the same similar symetra")
    else:
        print("Naaaaaahhhh!!!")

cat = [1, "d o g", 3, [2, 2, 2]]

dog = [1, "c a t", 3, [2, 2, 2]]

figure_out(cat)
print("\n\n\n")
symetr(cat, dog)