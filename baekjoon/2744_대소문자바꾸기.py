st = input()

for i in st:
    if i.isupper() == True:
        print(i.lower(), end='')

    else:
        print(i.upper(), end='')