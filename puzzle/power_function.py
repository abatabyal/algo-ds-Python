def power_div_conq(x, y):
    if y == 0:
        return 1
    elif int(y % 2) == 0:
        return (power_div_conq(x, int(y / 2)) * power_div_conq(x, int(y / 2)))
    else:
        return (x * power_div_conq(x, int(y / 2)) * power_div_conq(x, int(y / 2)))

def power_dp(x, y):

    temp = int
    if y == 0:
        return 1
    temp = power_dp(x, y/2)
    if int(y % 2) == 0:
        return temp * temp
    else:
        return x * temp * temp

print(power_div_conq(2, 2))
print(power_dp(2, 2))