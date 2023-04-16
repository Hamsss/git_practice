import sys
meeting_time = []
for _ in range(int(input())): 
    meeting_time.append(list(map(int, sys.stdin.readline().split())))

meeting_time.sort(key = lambda x: x[0])
meeting_time.sort(key = lambda x: x[1])

count = 1
begin = meeting_time[0][1]
for i in range(1,len(meeting_time)):
    if meeting_time[i][0] >= begin:
        begin = meeting_time[i][1]
        count += 1
        
print(count)