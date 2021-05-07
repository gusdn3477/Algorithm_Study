def solution(arr):
    dp = [[0 for i in range(j)] for j in range(1, len(arr) + 1)]
    dp[0][0] = arr[0][0]

    for i in range(1, len(arr)):
        for j in range(len(arr[i])):
            if j == 0:
                dp[i][j] = dp[i - 1][j] + arr[i][j]

            elif j == len(dp[i]) - 1:
                dp[i][j] = dp[i - 1][j - 1] + arr[i][j]

            else:
                dp[i][j] = max(dp[i - 1][j - 1] + arr[i][j], dp[i - 1][j] + arr[i][j])

    answer = max(dp[len(dp) - 1])
    return answer