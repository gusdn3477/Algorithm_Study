def solution(priorities, location):
    answer = 0
    arr = []

    for i in range(len(priorities)):
        arr.append((i, priorities[i]))

    while True:
        a = arr.pop(0)
        flag = 0
        for i in range(len(arr)):
            if a[1] < arr[i][1]:
                flag = 1
                arr.append(a)
                break

        if flag == 0:
            answer += 1

            if a[0] == location:
                return answer