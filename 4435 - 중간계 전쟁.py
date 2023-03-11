for i in range(int(input())):
    gandal = list(map(int, input().split()))
    sauron = list(map(int, input().split()))
    
    gnadal_sum = gandal[0] + gandal[1] * 2 + (gandal[2] + gandal[3]) * 3 + gandal[4] * 4 + gandal[5] * 10
    sauron_sum = sauron[0] + (sauron[1] + sauron[2] + sauron[3]) * 2 + sauron[4] * 3 + sauron[5] * 5 + sauron[6] * 10
    
    if gnadal_sum > sauron_sum:
        print(f"Battle {i+1}: Good triumphs over Evil")
    elif gnadal_sum < sauron_sum:
        print(f"Battle {i+1}: Evil eradicates all trace of Good")
    else:
        print(f"Battle {i+1}: No victor on this battle field")