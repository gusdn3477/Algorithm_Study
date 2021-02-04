N = int(input())

for i in range(N):
    poc = list(map(int, input().split()))
    poc.sort()
    poc = poc[1:4]

    if poc[2] - poc[0] >= 4:
        print('KIN')

    else:
        print(sum(poc))