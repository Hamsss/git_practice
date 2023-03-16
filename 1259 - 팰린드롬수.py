while 1:
    num = int(input())
    if num == 0 : break
    flag = 0
    str_num = ''.join(reversed(str(num)))
    
    if num == int(str_num):
        print("yes")
    else:
        print("no")