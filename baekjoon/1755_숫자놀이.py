diction = ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
make = []
N, M = map(int, input().split())

for i in range(N, M + 1):

    st = ''
    a = str(i)

    for j in range(len(a)):
        st += diction[int(a[j])]

    make.append((st, int(a)))

make.sort()

ct = 0
for i in range(len(make)):

    ct += 1
    print(make[i][1], end=' ')
    if ct % 10 == 0:
        print()