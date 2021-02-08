N = int(input())
time = 0
start = 1

while N > 0:

    if start > N:
        start = 1

    N -= start

    start += 1
    time += 1

print(time)