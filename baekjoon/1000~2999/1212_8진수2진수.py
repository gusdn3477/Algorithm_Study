N = input()

N = '0o' + N
N = int(N, 8)

N = format(N,'b')
print(N)