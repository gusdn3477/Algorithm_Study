st = []
max_len = 0

for i in range(5):
    a = input()
    max_len = max(max_len, len(a))
    st.append(a)

for i in range(max_len):
    for j in range(5):
        try:
            print(st[j][i], end='')
        except:
            continue