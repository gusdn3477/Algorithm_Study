N = input()

if len(N) == 1:
    print('◝(⑅•ᴗ•⑅)◜..°♡ 뀌요미!!')

else:
    a = ord(N[1]) - ord(N[0])
    flag = 0

    for i in range(2, len(N)):
        if ord(N[i]) - ord(N[i - 1]) != a:
            flag = 1

    if flag == 0:
        print('◝(⑅•ᴗ•⑅)◜..°♡ 뀌요미!!')

    else:
        print('흥칫뿡!! <(￣ ﹌ ￣)>')