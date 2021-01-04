st = input()
st = '0b' + st
a = int(st, 2)
b = oct(a)
print(b[2:])