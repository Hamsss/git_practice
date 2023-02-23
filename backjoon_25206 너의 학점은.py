subject_count = 0
sbj_sum = 0
mine_score = 0

grade_graph = {'A+':4.5, 'A0':4.0, 'B+':3.5, 'B0':3.0, 
               'C+':2.5, 'C0':2.0, 'D+':1.5,'D0':1.0, 'F':0.0}

while subject_count != 20:
    sub, score, grade = map(str, input().split())
    
    if grade == 'P':
        subject_count += 1
        continue
    
    mine_score += float(score) * grade_graph.get(grade)
    
    sbj_sum += float(score)
    subject_count += 1
    
print(mine_score / sbj_sum)