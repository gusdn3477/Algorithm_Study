N, K = map(int, input().split())
cnt = 0
for hour in range(N + 1):
    for minute in range(60):
        for second in range(60):

            hour_ = str(hour)
            minute_ = str(minute)
            second_ = str(second)

            if len(hour_) < 2:
                hour_ = '0' + hour_

            if len(minute_) < 2:
                minute_ = '0' + minute_

            if len(second_) < 2:
                second_ = '0' + second_

            if hour_.count(str(K)) > 0 or minute_.count(str(K)) > 0 or second_.count(str(K)) > 0:
                cnt += 1

print(cnt)