import sys
words = []
yes_or_no = []

for _ in range(int(input())):
    key_w = sys.stdin.readline().rstrip()
    if key_w in yes_or_no:
        continue
    yes_or_no.append(key_w)
    value_c = len(key_w)
    words.append([value_c, key_w])
    
words.sort()

for i in range(len(words)):
    sys.stdout.write(f"{words[i][1]}\n")