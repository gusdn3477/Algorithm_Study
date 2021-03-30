from collections import deque

N = int(input())
queue = deque()
num = "0123456789"
arr = []

for i in range(N):
    a = input()

    for j in a:
        if j in num:
            queue.append(j)

        else:
            if queue:
                st = ''
                while queue:
                    st += queue.popleft()

                arr.append(int(st))

    st = ''
    if queue:
        while queue:
            st += queue.popleft()

        arr.append(int(st))

arr.sort()

for i in arr:
    print(i)