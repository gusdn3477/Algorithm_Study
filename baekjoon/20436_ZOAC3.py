consonant = {'q': [0, 0], 'w': [0, 1], 'e': [0, 2], 'r': [0, 3], 't': [0, 4],
             'a': [1, 0], 's': [1, 1], 'd': [1, 2], 'f': [1, 3], 'g': [1, 4],
             'z': [2, 0], 'x': [2, 1], 'c': [2, 2], 'v': [2, 3]}

vowel = {"y": [0, 5], "u": [0, 6], "i": [0, 7], "o": [0, 8], "p": [0, 9],
         "h": [1, 5], "j": [1, 6], "k": [1, 7], "l": [1, 8],
         "b": [2, 4], "n": [2, 5], "m": [2, 6]}

time = 0
left, right = input().split()
st = input()
move = 0

for i in st:

    if i in consonant:
        move += abs(consonant[left][0] - consonant[i][0]) + abs(consonant[left][1] - consonant[i][1])
        move += 1  # 클릭하는 시간
        left = i

    else:
        move += abs(vowel[right][0] - vowel[i][0]) + abs(vowel[right][1] - vowel[i][1])
        move += 1
        right = i

print(move)