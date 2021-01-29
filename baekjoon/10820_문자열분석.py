small = "abcdefghijklmnopqrstuvwxyz"
big = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
num = '0123456789'

while True:

    try:
        a = input()
        small_ct = 0
        big_ct = 0
        blank_ct = 0
        num_ct = 0
        for i in range(len(a)):
            if a[i] in small:
                small_ct += 1

            if a[i] in big:
                big_ct += 1

            if a[i] == ' ':
                blank_ct += 1

            if a[i] in num:
                num_ct += 1

        print(small_ct, big_ct, num_ct, blank_ct)

    except:
        break