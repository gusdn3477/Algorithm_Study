from collections import defaultdict

dic = defaultdict(int)
N = int(input())
ans = []

for i in range(N):
    a = input()
    dic[a[0]] += 1

for j in dic:
    
    if dic[j] >= 5:
        ans.append(j)

ans.sort()

if not ans:
    print("PREDAJA")

else:
    for i in ans:
        print(i,end='')