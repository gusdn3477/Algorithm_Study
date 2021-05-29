def find_parent(parent, a):
    if a != parent[a]:
        a = find_parent(parent, parent[a])

    return parent[a]


def union(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)

    if a < b:
        parent[b] = a

    else:
        parent[a] = b


def solution(n, costs):
    answer = 0
    parent = [0] * n

    for i in range(n):
        parent[i] = i

    costs = sorted(costs, key=lambda x: x[2])

    for i in range(len(costs)):
        a, b, c = costs[i]

        a = find_parent(parent, a)
        b = find_parent(parent, b)

        if a != b:
            union(parent, a, b)
            answer += c

    return answer