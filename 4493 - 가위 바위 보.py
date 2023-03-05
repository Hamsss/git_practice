import sys

for _ in range(int(input())):
    p1_count, p2_count = 0,0
    for _ in range(int(input())):
        result = sys.stdin.readline().strip()
        if result in ["R S","S P","P R"]:
            p1_count += 1
        elif result in ["R P","S R","P S"]:
            p2_count += 1
            
    if p1_count > p2_count:
        print("Player 1")
    elif p1_count < p2_count:
        print("Player 2")
    else:
        print("TIE")