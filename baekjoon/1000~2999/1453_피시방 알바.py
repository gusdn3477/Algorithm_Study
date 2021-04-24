N = int(input())
arr = list(map(int, input().split()))
arr2 = list(set(arr))

print(len(arr) - len(arr2))