import sys

sentence = {}
for i in range(26):
    sentence[chr(97+i)] = False

while 1:
    word = sys.stdin.readline().rstrip()
    if word == '*': break
    cop = sentence.copy()
    
    for i in range(len(word)):
        if ord('a') <= ord(word[i]) <= ord('z'): cop[word[i]] = True
    
    flag = 1
    key = list(cop.keys())
    for i in key:
        if cop[i] == False: 
            flag = 0
            break

    if flag ==1: print("Y")
    else: print("N")