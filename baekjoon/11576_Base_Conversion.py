N, M = map(int, input().split())
length = int(input())
num = list(map(int, input().split()))

num = list(reversed(num))
total = 0

for i in range(len(num)):
    total += num[i] * (N ** i)

new_list = []

while total > 0:
    new_list.append(total % M)
    total = total // M

new_list = list(reversed(new_list))
for i in range(len(new_list)):
    print(new_list[i], end=' ')