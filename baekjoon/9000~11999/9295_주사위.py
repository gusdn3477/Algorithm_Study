N = int(input())

for i in range(1, N + 1):
    a, b = map(int, input().split())

    st = f'Case {i}: {a + b}'
    print(st)