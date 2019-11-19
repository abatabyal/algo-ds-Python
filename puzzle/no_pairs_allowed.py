def noAdjacentDup(x):
    s = list(x)
    count = 0
    n = len(s)
    for i in range(1, n):
        # If any two adjacent characters are equal
        if (s[i] == s[i - 1]):
            s[i] = "a"  # Initialize it to 'a'
            # Traverse the loop until it is different
            # from the left and right letter.
            while (s[i] == s[i - 1] or (i + 1 < n and s[i] == s[i + 1])):
                s[i] = chr(ord(s[i]) + 1)
            i += 1
            count += 1
    return count
s = "abaaaba"
print(noAdjacentDup(s))

