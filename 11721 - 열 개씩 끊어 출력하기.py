import sys

sentence = sys.stdin.readline()

for i in range(0, len(sentence), 10):
    print(sentence[i:i+10])