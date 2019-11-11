def count_frequency(input1):
    freq_dict = {}
    for i in input1:
        if i in freq_dict:
            freq_dict[i] += 1
        else:
            freq_dict[i] = 1
    chars_list = []
    for k in freq_dict.keys():
        chars_list.append(k)
    chars_list.sort()
    for c in chars_list:
        print(c,freq_dict[c],sep="", end=" ")

count_frequency('geeksforgeeks')
