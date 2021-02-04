from collections import deque


def BFS(x):
    queue = deque()
    queue.append(x)
    arr[x] = 1

    while queue:

        a = queue.popleft()

        if a == G:
            return

        for i in range(2):
            dx = a + move[i]

            if dx <= 0 or dx > F:
                continue

            if arr[dx] == 0:
                arr[dx] = arr[a] + 1
                queue.append(dx)

    return False


F, S, G, U, D = map(int, input().split())
arr = [0] * (1000001)
move = [U, D * -1]

if BFS(S) == False:
    print('use the stairs')

else:
    print(arr[G] - 1)