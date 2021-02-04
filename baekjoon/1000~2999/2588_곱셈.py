def recursive(A, B):
    if B <= 0:
        return

    print(A * (B % 10))
    recursive(A, B // 10)


A = int(input())
B = int(input())

recursive(A, B)
print(A * B)