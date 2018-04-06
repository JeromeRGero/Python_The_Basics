import random
import math

# x = 1
# lsNum = [90, 80, 70, 60, 50]
# lsGrade = ['A', 'B', 'C', 'D', 'F']
#
# while x < 11:
#     r_num = int(math.floor(random.random() * 40 + 61))
#     a = 0
#     for i in range(0, len(lsNum)):
#         if a == 0 and lsNum[i] <= r_num:
#             str(r_num)
#             grade = lsGrade[i]
#             print("Score: {}; Your grade is {}".format(r_num, grade))
#             a += 1
#     x += 1
#
#


print("Start the program...")

def toss():
    throw = 1
    heads = 0
    tails = 0

    while throw <= 5000:
        coin = int(random.random()*2 + 1)
        if coin > 1:
            heads += 1
            print("Attempt #{}: Throwing a coin... It's heads! ... Got {} heads so far and {} tails.".format(throw, heads, tails))
        else:
            tails += 1
            print("Attempt #{}: Throwing a coin... It's tails! ... Got {} heads so far and {} tails.".format(throw, heads, tails))
        throw += 1
        coin += 1

toss()
print("End of progrm. Bye!")