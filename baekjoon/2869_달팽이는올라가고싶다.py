from math import ceil

A,B,V = map(int, input().split())
start = 0
day = 0

a = (V-B)/(A-B)
print(ceil(a))