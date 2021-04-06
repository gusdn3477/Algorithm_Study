from sys import stdin

N = int(input())
arr = list(map(int, stdin.readline().split()))
arr2 = list(map(int, stdin.readline().split()))
ans = []

for i in range(len(arr)):
    ans.append([arr2[i], arr[i]])

ans.sort()
time = 0
total = 0
for i in range(len(ans)):
    total += ans[i][1] + ans[i][0] * time
    time += 1

print(total)