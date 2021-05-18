from copy import copy

num = list(map(int, input().split()))
alpha = list(input())
alpha2 = copy(alpha)
num.sort()
alpha.sort()
dic = {}

for i in range(3):
    dic[alpha[i]] = num[i]

for i in range(len(alpha2)):
    print(dic[alpha2[i]], end=' ')