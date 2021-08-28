def solution(scores):
    answer = ''
    LEN = len(scores)
    for i in range(LEN):
        MAX, MIN = 0, 100
        for j in range(LEN):
            MAX = max(MAX, scores[j][i])
            MIN = min(MIN, scores[j][i])
        MAX_CT, MIN_CT = 0, 0
        total = 0
        for j in range(LEN):
            total += scores[j][i]
            if scores[j][i] == MAX:
                MAX_CT += 1
            if scores[j][i] == MIN:
                MIN_CT += 1
        if MAX == scores[i][i] and MAX_CT == 1:
            sco = (total - MAX) / (LEN - 1)
        elif MIN == scores[i][i] and MIN_CT == 1:
            sco = (total - MIN) / (LEN - 1)
        else:
            sco = total / LEN
        if sco >= 90:
            answer += 'A'
        elif sco >= 80:
            answer += 'B'
        elif sco >= 70:
            answer += 'C'
        elif sco >= 50:
            answer += 'D'
        else:
            answer += 'F'
            
    return answer