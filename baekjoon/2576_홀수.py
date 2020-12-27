poc = []

for i in range(7):
    N = int(input())
    if N % 2 == 1:
        poc.append(N)

if not poc:
    print('-1')

else:
    print(sum(poc))
    print(min(poc))