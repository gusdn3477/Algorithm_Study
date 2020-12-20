N = int(input())

for j in range(1,N+1):
    M = input()
    poc = ''
    for i in M: 
        poc += i
        if poc == M[len(poc):len(poc)+len(poc)]:
            print('#'+str(j), len(poc))
            break
