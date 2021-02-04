submit = [i for i in range(1, 31)]

for i in range(28):
    N = int(input())
    submit.remove(N)

for i in range(len(submit)):
    print(submit[i])