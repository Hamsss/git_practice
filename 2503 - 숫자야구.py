from itertools import permutations
numbers= list(permutations([1,2,3,4,5,6,7,8,9], 3))

for _ in range(int(input())):
    num, s, b = map(int, input().split())
    str_num = str(num)
    remove_count = 0
    
    for i in range(len(numbers)):
        sc, bc = 0,0
        i -= remove_count
        
        for j in range(3):
            if int(str_num[j]) == numbers[i][j]: sc += 1
            elif int(str_num[j]) in numbers[i]: bc += 1
                
        if sc != s or bc != b:
            numbers.remove(numbers[i])
            remove_count += 1

print(len(numbers))
        