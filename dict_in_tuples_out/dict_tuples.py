
my_dict = {
  "Speros": "(555) 555-5555",
  "Michael": "(999) 999-9999",
  "Jay": "(777) 777-7777"
}
#   function output
# [("Speros", "(555) 555-5555"), ("Michael", "(999) 999-9999"), ("Jay", "(777) 777-7777")]


def dict_tuples(dict):
    myLs = []
    making = 0
    for key in dict:
        if making == 0:
            tup1 = (key, dict[key])
            making += 1
        elif making == 1:
            tup2 = (key, dict[key])
            making += 1
        else:
            tup3 = (key, dict[key])
    tup4 = tup3 + tup2 + tup1
    print tup4


#  dict_tuples(my_dict)

name = ["Anna", "Eli", "Pariece", "Brendan", "Amy", "Shane", "Oscar"]
favorite_animal = ["horse", "cat", "spider", "giraffe", "ticks", "dolphins", "llamas"]

def making_christmas(ls1, ls2):
    dict = {}
    soup = 0
    start = 'n'
    if len(name) <> len(favorite_animal):
        if len(name) > len(favorite_animal):
            soup = len(favorite_animal)
            start = 'f'
        else:
            soup = len(name)
    else:
        soup = len(name)

    for i in range(0, soup):
        dict[name[i]] = favorite_animal[i]
    print dict

making_christmas(name, favorite_animal)