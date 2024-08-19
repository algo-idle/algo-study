from sys import *

test = stdin.readline().rstrip()
remove_word = stdin.readline().rstrip()
flag = True

while flag:
    if remove_word in test:
        test = test.replace(remove_word,'')    
        flag = True
    else:
        flag = False

if test:
    print(test)
else:
    print("FRULA")

