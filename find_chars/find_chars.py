




word_list = ['hello','world','my','name','is','Anna']
char = 'o'

def find_chars(ls, c):
    newLs = []
    for main_i in  ls:
        for i in main_i:
            if i == c:
                newLs.append(main_i)
    print(newLs)

find_chars(word_list, char)