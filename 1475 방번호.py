import sys

number = [0]*10
N = sys.stdin.readline().rstrip()

for i in range(len(N)):
    number[int(N[i])] += 1

number[6] = number[9] = (number[6] + number[9] - 1) // 2 + 1
mex = max(number)

print(mex)


