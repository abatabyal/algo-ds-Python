def repeatedString(s, n):
    str_len = len(s)
    a_count = 0
    a_index = []
    for i in range(str_len):
        if s[i] == 'a':
            a_count += 1
            a_index.append(i + 1)
    complete_repeat, add_chars = divmod(n, str_len)
    total_a = a_count * complete_repeat
    if add_chars > 0:
        for idx in a_index:
            if add_chars >= idx:
                total_a += 1
    return total_a

s = "abcac"
n = 10
print(repeatedString(s, n))