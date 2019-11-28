def sockMerchant(n, ar):
    sock_color_dict = {}
    for c in ar:
        if c in sock_color_dict:
            sock_color_dict[c] += 1
        else:
            sock_color_dict[c] = 1

    pair_count = 0
    for p in sock_color_dict:
        if sock_color_dict[p] >= 2:
            pair_count += sock_color_dict[p]//2
    print(pair_count)

arr = [1,2,1,2,1,3,2]
n = len(arr)
sockMerchant(n, arr)