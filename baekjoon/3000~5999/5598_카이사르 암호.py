before = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
after = "DEFGHIJKLMNOPQRSTUVWXYZABC"

a = input()
for i in a:
    idx = after.find(i)
    print(before[idx],end='')