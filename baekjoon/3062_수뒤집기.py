N = int(input())

for i in range(N):
    num = input()
    num_reverse = num[::-1]
    total = str(int(num) + int(num_reverse))

    if total == total[::-1]:
        print('YES')

    else:
        print('NO')