def find_digits(n):
    digit_list = []
    for i in str(n):
        if int(i) != 0:
            digit_list.append(int(i))
    count = 0
    for d in digit_list:
        if n % d == 0:
            count += 1
    return count

print(find_digits(1012))