
x = [4, 6, 1, 3, 5, 7, 25]
z = [4, "Tom", 1, "Michael", 5, 7, "Jimmy Smith"]


# def draw_stars(ls):
#     for i in ls:
#         myStr = ''
#         num = i
#         while num > 0:
#             myStr += '*'
#             num -= 1
#         print(myStr)

def draw_stars_again(ls):

    for i in range(0, len(ls)):
        myStr = ''
        if isinstance(ls[i], int):
            num = ls[i]
            char = ' '
        else:
            char = ls[i][0]
            char = char.lower()
            num = len(ls[i])

        while num > 0:
            if char == ' ':
                myStr += '*'
                num -= 1
            else:
                myStr += char
                num -= 1
        print(myStr)

# draw_stars(x)
draw_stars_again(z)