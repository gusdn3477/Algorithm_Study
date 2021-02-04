L, R, A = map(int, input().split())

while A > 0:

    if L < R:
        L += 1
        A -= 1

    else:
        R += 1
        A -= 1

if L > R:
    print(L + R - (L - R))

elif L < R:
    print(L + R - (R - L))

else:
    print(L + R)