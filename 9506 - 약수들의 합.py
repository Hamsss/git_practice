while 1:
    n = int(input())
    if n == -1:
        break
    
    count = []
    
    for i in range(1, n//2 + 1):
        if n % i == 0:
            count.append(i)
    
    if sum(count) == n:
        print(n , '=' , " + ".join(str(j) for j in count))
    else:
        print(n , "is NOT perfect.")
            