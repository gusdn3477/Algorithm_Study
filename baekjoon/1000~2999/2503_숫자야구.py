N = int(input())
arr = []
ans = 0
ct = 0
for i in range(N):
    a, s, b = input().split()
    s = int(s)
    b = int(b)
    arr.append((a, (s, b)))

for i in range(123, 988):
    m = str(i)
    ans = 0

    if m[0] == m[1] or m[1] == m[2] or m[0] == m[2] or '0' in m:
        continue

    for z in range(len(arr)):

        strike = 0
        ball = 0

        if m[0] == arr[z][0][0]:
            strike += 1

        if m[1] == arr[z][0][1]:
            strike += 1

        if m[2] == arr[z][0][2]:
            strike += 1

        if m[0] != arr[z][0][0] and (m[0] == arr[z][0][1] or m[0] == arr[z][0][2]):
            ball += 1

        if m[1] != arr[z][0][1] and (m[1] == arr[z][0][0] or m[1] == arr[z][0][2]):
            ball += 1

        if m[2] != arr[z][0][2] and (m[2] == arr[z][0][0] or m[2] == arr[z][0][1]):
            ball += 1

        if strike == arr[z][1][0] and ball == arr[z][1][1]:
            ans += 1

    if ans == len(arr):
        ct += 1

print(ct)