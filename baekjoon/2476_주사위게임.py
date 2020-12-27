N = int(input())
poc = []
money = []
for i in range(N):
    poc.append(list(map(int, input().split())))

for i in range(N):

    if poc[i][0] == poc[i][1] and poc[i][1] == poc[i][2]:
        money.append(10000 + poc[i][0] * 1000)

    elif poc[i][0] == poc[i][1]:
        money.append(1000 + 100 * poc[i][0])

    elif poc[i][0] == poc[i][2]:
        money.append(1000 + 100 * poc[i][0])

    elif poc[i][1] == poc[i][2]:
        money.append(1000 + 100 * poc[i][1])

    else:
        money.append(100 * max(poc[i]))

print(max(money))