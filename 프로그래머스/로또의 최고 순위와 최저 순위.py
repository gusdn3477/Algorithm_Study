def solution(lottos, win_nums):
    answer = []
    ok = 0
    t = lottos.count(0)
    for i in lottos:
        if i == 0:
            continue
        if i in win_nums:
            ok += 1
    MIN = ok
    MAX = t + ok
    MAX = 7 - MAX
    MIN = 7 - MIN
    if MAX > 6:
        MAX = 6
    if MIN > 6:
        MIN = 6
    return [MAX,MIN]