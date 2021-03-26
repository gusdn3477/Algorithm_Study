N = int(input())
book = {}

for i in range(N):

    t = input()
    if t not in book:
        book[t] = 1

    else:
        book[t] += 1

book_modified = list(book.items())
book_modified = sorted(book_modified, key=lambda x: (-x[1], x[0]))
print(book_modified[0][0])