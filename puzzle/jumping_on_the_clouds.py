def jumping_on_the_clouds(clouds):
    n = len(clouds)
    jumps = 0
    j = 0
    while j != n-1:
        if j < n-2 and clouds[j] != 1 and clouds[j+2] != 1:
            jumps += 1
            j += 2
        elif j < n-1 and clouds[j] != 1 and clouds[j+1] != 1:
            jumps += 1
            j += 1
        else:
            j += 1
    return jumps

clouds = [0,0,0,1,0,0]
print(jumping_on_the_clouds(clouds))