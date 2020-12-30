arr = [350.34, 230.90, 190.55, 125.30, 180.90]

N = int(input())
for i in range(N):
    a,b,c,d,e = map(int, input().split())
    total = arr[0] * a + arr[1] * b + arr[2]* c + arr[3] * d + arr[4] * e
    print('$%.2f' %total)