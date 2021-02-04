A, B, C, X, Y = map(int, input().split())
total = 0
total2 = 0

if C * 2 >= A + B:
    total += A * X + B * Y

else:
    total += C * 2 * min(X, Y)
    if X > Y:
        total += A * (X - Y)

    elif X < Y:
        total += B * (Y - X)

    total2 = C * 2 * max(X, Y)
    total = min(total, total2)

print(total)