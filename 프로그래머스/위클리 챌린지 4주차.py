def solution(table, languages, preference):
    answer = ''
    ans = []
    for i in table:
        dic = {}
        start = 5
        total = 0
        arr = i.split()
        for j in range(1, len(arr)):
            dic[arr[j]] = start
            start -= 1
        for j in range(len(languages)):
            if languages[j] in dic:
                total += dic[languages[j]] * preference[j]
        ans.append((arr[0], total))
    ans.sort(key = lambda x : (-x[1], x[0]))
    return ans[0][0]