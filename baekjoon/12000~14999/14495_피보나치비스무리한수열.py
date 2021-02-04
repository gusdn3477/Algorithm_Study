fibo = [0] * 120
fibo[0] = 0
fibo[1] = 1
fibo[2] = 1
fibo[3] = 1

N = int(input())

for i in range(4, N + 1):
    fibo[i] = fibo[i - 1] + fibo[i - 3]

print(fibo[N])