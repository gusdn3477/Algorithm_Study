def solution(answers):
    answer = []

    first = [1, 2, 3, 4, 5]
    second = [2, 1, 2, 3, 2, 4, 2, 5]
    third = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]

    dic = {1: 0, 2: 0, 3: 0}

    for i in range(len(answers)):

        if first[i % len(first)] == answers[i]:
            dic[1] += 1

        if second[i % len(second)] == answers[i]:
            dic[2] += 1

        if third[i % len(third)] == answers[i]:
            dic[3] += 1

    m = max(dic[1], dic[2], dic[3])

    for i in range(1, 4):
        if m == dic[i]:
            answer.append(i)

    return answer