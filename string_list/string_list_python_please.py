

words = "It's thanksgiving day. It's my birthday,too!"

word = "day"

print words.replace("day", "month")

x = [2,54,-2,7,12,98]

def the_min(g):
    return min(g)


def the_max(g):
    return max(g)

print the_max(x)

print the_min(x)

y = ["hello",2,54,-2,7,12,98,"world"]

print y[0:1]

print y[len(y)-1:len(y)]

print y[0]

print y[len(y)-1]

def f_l(g):
    newList = []
    newList.append(g[0])
    newList.append(g[len(g)-1])
    return newList

print f_l(y)

z = [19,2,54,-2,7,12,98,32,10,-3,6]

def newList(g):
    g.sort()
    first = []
    last = [0]
    for i in range(0, len(g)-1):
        if i < len(g)/2:
            first.append(g[i])
        else:
            last.append(g[i])
    last[0] = first
    print (last)

newList(z)