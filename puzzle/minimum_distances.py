def minimumDistances(a):
    freq_count = {}
    for i in a:
        if i in freq_count:
            freq_count[i] += 1
        else:
            freq_count[i] = 1
    dup_entries_sum = []
    for key, value in freq_count.items():
        if value > 1:
            dup_entries_sum.append(key)
    if dup_entries_sum:
        index_sum = {}
        for i in range(len(a)):
            if a[i] in index_sum:
                index_sum[a[i]] = abs(index_sum[a[i]] - i)
            else:
                index_sum[a[i]] = i
        sum_list = []
        for dup in dup_entries_sum:
            sum_list.append(index_sum[dup])
        min_dist = min(sum_list)
        return min_dist
    else:
        return -1


arr = [7, 1, 3, 4, 1, 7]
print(minimumDistances(arr))