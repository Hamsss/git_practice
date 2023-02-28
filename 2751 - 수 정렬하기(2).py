# def quick_sort(num):
#     if len(num) <= 1:
#         return num

#     pivot = num[len(num)//2]

#     small_arr, same_arr, big_arr = [], [pivot], []

#     for data in num:
#         if data < pivot:
#             small_arr.append(data)
#         elif data > pivot:
#             big_arr.append(data)

#     return quick_sort(small_arr) + same_arr + quick_sort(big_arr)

# arr = quick_sort(arr)
import sys

N = int(input())
arr = []
for _ in range(N):
    arr.append(int(sys.stdin.readline()))
arr.sort()
for i in arr:
    print(i)