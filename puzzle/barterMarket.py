def bmarket(n, m, x, y):
    fiction_books = 0
    comic_books = n
    for i in range(1, comic_books):
        # if coins are more or equal to coins needed
        # + one comic book
        if m >= x and n >= 1:
            fiction_books += 1
            m = m - x
            n = n - 1
        # if coins(m) are less than x(fiction book price)
        # and comic books(n) is more than 1
        if m < x and n >= 2 and (m+y) >= x:
            m = m + y
            n = n - 1
            fiction_books += 1
            m = m - x
            n = n - 1
    return fiction_books

#print(bmarket(393, 896, 787, 920))
print(bmarket(4, 8, 4, 3))

