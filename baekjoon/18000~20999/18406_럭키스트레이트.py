num = input()
st = num[:len(num) // 2]
st2 = num[len(num) // 2:]

st = list(map(int, st))
st2 = list(map(int, st2))

if sum(st) == sum(st2):
    print("LUCKY")

else:
    print("READY")