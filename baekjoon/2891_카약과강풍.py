N, S, R = map(int, input().split())
injured = list(map(int, input().split()))
more = list(map(int, input().split()))

for i in range(len(more)):

    if more[i] in injured:
        injured.remove(more[i])

    elif more[i] - 1 in injured:
        injured.remove(more[i] - 1)

    elif more[i] + 1 in injured:
        injured.remove(more[i] + 1)

print(len(injured))