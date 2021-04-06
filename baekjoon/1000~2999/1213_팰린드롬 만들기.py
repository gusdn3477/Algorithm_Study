dic = {}
A = input()
ct = 0
flag = 0
for i in A:

    if i not in dic:
        dic[i] = 1

    else:
        dic[i] += 1

for i in dic.values():

    if i % 2 != 0:
        ct += 1

    if ct > 1:
        flag = 1
        break

if flag == 1:
    print("I'm Sorry Hansoo")

else:
    arr = list(dic.items())
    arr.sort()
    st = ''

    # 차례대로 출력
    if ct == 0:
        for i in range(len(arr)):
            st += arr[i][0] * (arr[i][1] // 2)

        for i in range(len(arr) - 1, -1, -1):
            st += arr[i][0] * (arr[i][1] // 2)

    # 짝수 출력 + 홀수 출력 + 짝수 거꾸로
    else:
        for i in range(len(arr)):
            if arr[i][1] % 2 == 1:
                c = arr[i][0]
                d = arr[i][1]
                st += arr[i][0] * (arr[i][1] // 2)

            else:
                st += arr[i][0] * (arr[i][1] // 2)

        st += c

        for i in range(len(arr) - 1, -1, -1):

            if arr[i][1] % 2 == 1:
                c = arr[i][0]
                d = arr[i][1]
                st += arr[i][0] * (arr[i][1] // 2)

            else:
                st += arr[i][0] * (arr[i][1] // 2)

    print(st)