N = int(input())
poc = []
for i in range(N):

    poc = list(map(int, input().split()))
    save = []
    for i in poc:
        if i % 2 == 0:
            save.append(i)

    print(sum(save), min(save))
