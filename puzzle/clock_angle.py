def calc_angle(h, m):
    # minute hand angle per minute
    # 360/60 = 6 degree/min
    # hour hand = 360/720 mins = 0.5 degree/min

    if h < 0 or m < 0 or h > 12 or m > 60:
       print('Invalid Input')

    if h == 12:
        h = 0
    if m == 60:
        m = 0

    hour_angle = (h * 60 + m) * 0.5
    minute_angle = 6 * m

    # dif bw angle
    angle = abs(hour_angle - minute_angle)

    angle = min(360 - angle, angle)
    return angle

print(calc_angle(12, 30))