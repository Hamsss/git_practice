import sys
from collections import Counter

N,M,B = map(int,input().split())
ground = []
for _ in range(N): 
    ground += map(int, sys.stdin.readline().split())

sum_m,count,time,height = sum(ground),dict(Counter(ground)),sys.maxsize,0

for i in range(min(ground), max(ground) + 1):
    if sum_m + B >= i * N * M:
        time_count = 0
        # 블럭이 올라가있는 층을 for문을 통해 모두 돌아보자.
        # 해당층보다 많으면 없애고 적으면 블록을 더해보자
        for key in count:
            if key < i: time_count += (i - key) * count[key]
            elif key > i: time_count += (key - i) * count[key] * 2
        if time >= time_count:
            time = time_count
            height = i

print(time, height)  
    
    
