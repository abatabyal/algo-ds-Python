import sys
def merge_range(a):
    b = list(map(list, a))
    b.sort(key=lambda x:x[0])
    print(b)
    m = []
    s = -1000
    max = -1000
    for i in range(len(b)):
        x = b[i]
        if x[0] > max:
            if i != 0:
                m.append([s,max])
            max = x[1]
            s = x[0]
        else:
            if x[1] > max:
                max = x[1]
    if max != -1000 and [s,max] not in m:
        m.append([s, max])
    res = list(map(tuple,m))
    print(res)


a = [(2,3), (3,5),(7,9),(8,10)]
merge_range(a)