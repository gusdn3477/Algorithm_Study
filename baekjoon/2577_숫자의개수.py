poc = []
poc.append(int(input()))
poc.append(int(input()))
poc.append(int(input()))

a = str(poc[0] * poc[1] * poc[2])

for i in range(10):
    print(a.count(str(i)))