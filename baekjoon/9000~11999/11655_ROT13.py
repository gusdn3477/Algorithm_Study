alpha_small = 'abcdefghijklmnopqrstuvwxyz'
alpha_big = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

S = input()
for i in range(len(S)):
    if S[i] in alpha_small:
        a = alpha_small.index(S[i])
        idx = (a + 13) % 26
        print(alpha_small[idx], end='')

    elif S[i] in alpha_big:
        a = alpha_big.index(S[i])
        idx = (a + 13) % 26
        print(alpha_big[idx], end='')

    else:
        print(S[i], end='')