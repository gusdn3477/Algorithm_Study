def solution(n):
    answer = 0

    start = 1

    while start <= n:

        total = 0
        start_tmp = start
        while total <= n:

            total += start_tmp
            start_tmp += 1

            if total == n:
                answer += 1

        start += 1

    return answer