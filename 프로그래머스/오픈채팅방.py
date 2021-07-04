def solution(record):
    answer = []
    ans = []
    dic = {}
    for i in range(len(record)):
        answer.append(record[i].split())
    for i in range(len(answer)):
        if answer[i][0] == "Enter":
            dic[answer[i][1]] = answer[i][2]
        elif answer[i][0] == "Change":
            dic[answer[i][1]] = answer[i][2]
    for i in range(len(answer)):
        if answer[i][0] == "Enter":
            st = dic[answer[i][1]] + '님이 들어왔습니다.'
            ans.append(st)
        elif answer[i][0] == "Leave":
            st = dic[answer[i][1]] + '님이 나갔습니다.'
            ans.append(st)
    return ans