import sys
timeline = [0] * 1000
check = []
numbers = []

for _ in range(int(input())):
    start, end = map(int, sys.stdin.readline().split())
    check.append([start,end])
    for i in range(start,end):
        timeline[i] += 1

for s,e in check:
    checking = timeline.copy()
    for i in range(s,e):
        checking[i] -= 1
    numbers.append(1000 - checking.count(0))

print(max(numbers))
    
    
    
    
    
    