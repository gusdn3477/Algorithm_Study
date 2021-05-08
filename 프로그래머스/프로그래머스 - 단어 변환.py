from collections import deque


def BFS(begin, target, words):
    queue = deque()
    queue.append((begin, 0))
    visited = [0] * len(words)

    while queue:

        a = queue.popleft()
        if a[0] == target:
            return a[1]

        for i in range(len(words)):
            ct = 0
            for j in range(len(words[i])):
                if a[0][j] == words[i][j]:
                    ct += 1

            if ct == len(words[i]) - 1 and visited[i] == 0:
                visited[i] = 1
                queue.append((words[i], a[1] + 1))

    return 0


def solution(begin, target, words):
    answer = BFS(begin, target, words)
    return answer