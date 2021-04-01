N = int(input())
queue = []
queue2 = []
flag = 0

for i in range(N):
    queue.append(input())

for i in range(N - 1):
    queue2.append(input())

queue.sort()
queue2.sort()

for i in range(len(queue2)):
    if queue[i] != queue2[i]:
        print(queue[i])
        flag = 1
        break

if flag == 0:
    print(queue[-1])