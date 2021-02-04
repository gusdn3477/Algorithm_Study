N = int(input())
ct = 0

for i in range(1, N + 1):
    ct += str(i).count('3')
    ct += str(i).count('6')
    ct += str(i).count('9')

print(ct)