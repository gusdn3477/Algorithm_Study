N = int(input())
arr = []
ct = 1
for i in range(N):
    arr.append(int(input()))
    
#왼쪽에서 본 경우
start = arr[0]
for i in range(1,len(arr)):
    
    if arr[i] > start:
        start = arr[i]
        ct += 1
        
print(ct)
ct = 1

#오른쪽에서 본 경우
start = arr[-1]
for i in range(len(arr)-1,-1,-1):
    
    if arr[i] > start:
        start = arr[i]
        ct += 1
        
print(ct)