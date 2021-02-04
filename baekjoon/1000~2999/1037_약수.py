N = int(input())
poc = list(map(int, input().split()))

poc.sort()
print(poc[0] * poc[-1])