from bisect import bisect_left

while True:

    try:
        N = int(input())
        arr = list(map(int, input().split()))
        dp = []
        dp.append(arr[0])

        for i in range(1, len(arr)):
            idx = bisect_left(dp, arr[i])

            if idx == len(dp):
                dp.append(arr[i])

            else:
                dp[idx] = arr[i]

        print(len(dp))

    except:
        break