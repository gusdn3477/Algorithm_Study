def solution(board, moves):
    answer = 0
    stack = []
    for i in moves:
        a = i-1
        t = -1
        for j in range(len(board)):
            if board[j][a] != 0:
                t = board[j][a]
                board[j][a] = 0
                break
        if t == -1:
            continue
        if not stack:
            stack.append(t)
        else:
            if stack[-1] == t:
                stack.pop()
                answer += 2
            else:
                stack.append(t)
    return answer