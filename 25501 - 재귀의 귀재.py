import sys

def recursion(s, l, r):
    global i
    i += 1
    if l >= r: return 1
    elif s[l] != s[r]: return 0
    else: return recursion(s, l+1, r-1)
def isPalindrome(s):
    return recursion(s, 0, len(s)-1)

list = []

for _ in range(int(input())):
    i = 0
    list.append([isPalindrome(sys.stdin.readline().strip()), i])

for i in range(len(list)):
    sys.stdout.write(f"{list[i][0]} {list[i][1]}\n")