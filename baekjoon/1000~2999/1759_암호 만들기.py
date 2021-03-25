def backTracking(start, ct, st):
    if ct == L:

        vowel_cnt = 0
        vowel = "aeiou"

        for i in st:
            if i in vowel:
                vowel_cnt += 1

        if vowel_cnt >= 1 and ct - vowel_cnt >= 2:
            for j in st:
                print(j, end='')
            print()

    for i in range(start, len(arr)):

        if arr[i] not in st:
            st += arr[i]
            backTracking(i + 1, ct + 1, st)
            st = st[:len(st) - 1]


L, C = map(int, input().split())
arr = input().split()
arr.sort()
visited = []
st = ''
poc = []
backTracking(0, 0, st)