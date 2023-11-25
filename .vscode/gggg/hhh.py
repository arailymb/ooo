#task 1
def readfile(filename):
    file = open(filename, 'r', encoding='utf-8')
    print(file.read())

readfile(r"C:\Users\Admin\Documents\ooo\.vscode\gggg\lll.txt")

#task 2
import random
def readrandom(filename):
    file = open(filename, 'r', encoding='utf-8')
    lines = file.readlines()
    print (random.choice(lines))

readrandom(r"C:\Users\Admin\Documents\ooo\.vscode\gggg\lll.txt")

#task 3
def countup(filename):
    file = open(filename, 'r', encoding='utf-8')
    filecontent = file.read()
    uppercount = 0

    for i in filecontent:
        if(i.isupper()):
            uppercount += 1

    print (uppercount)

countup(r"C:\Users\Admin\Documents\ooo\.vscode\gggg\lll.txt")

#task 4
def countnod(filename):
    file = open(filename, 'r', encoding='utf-8')
    filecontent = file.readlines()
    c = 0

    for i in filecontent:
        if not i[0] == 'D' :
            c = c + 1

    print (c)

countnod(r"C:\Users\Admin\Documents\ooo\.vscode\gggg\lll.txt")

#task 5
def countendf(filename):
    file = open(filename, 'r', encoding='utf-8')
    filecontent = file.readlines()
    c = 0

    for i in filecontent:
        if i.lower().endswith('f'):
            c = c + 1

    print (c)

countendf(r"C:\Users\Admin\Documents\ooo\.vscode\gggg\lll.txt")

#task 6
def countallnone(filename):
    file = open(filename, 'r', encoding='utf-8')
    filecontent = file.readlines()
    c = 0
    d = 0

    for i in filecontent:
        if i.lower() == 'all':
            c = c + 1
        if i.lower() == 'none':
            d = d + 1
    print (c, d)

countallnone(r"C:\Users\Admin\Documents\ooo\.vscode\gggg\lll.txt")

#task 7
from collections import Counter
def countfreq(filename):
    file = open(filename, 'r', encoding='utf-8')
    filecontent = file.read().split()
    wordfreq = Counter(filecontent)

    print (wordfreq)

countfreq(r"C:\Users\Admin\Documents\ooo\.vscode\gggg\lll.txt")

#task 8
def countlong(filename):
    file = open(filename, 'r', encoding='utf-8')
    filecontent = file.read().split()
    longest_word = max(filecontent, key=len)
    return longest_word

countlong(r"C:\Users\Admin\Documents\ooo\.vscode\gggg\lll.txt")

#task 9
def bwithj(filename):
    file = open(filename, 'r', encoding='utf-8')
    filecontent = file.read()
    correctcontent = filecontent.replace('B', 'J')
    return correctcontent

bwithj(r"C:\Users\Admin\Documents\ooo\.vscode\gggg\lll.txt")


#task 10
def aandb(filename):
    with open(filename, 'r') as file:
        content = file.read()
        count_A = content.lower().count('a')
        count_B = content.lower().count('b')
        return f'a={count_A}, b={count_B}'
    
aandb(r"C:\Users\Admin\Documents\ooo\.vscode\gggg\lll.txt")


