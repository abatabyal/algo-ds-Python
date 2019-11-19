def efficientJanitor(weight):
    weight.sort(reverse=True)
    total_sum = sum(weight)
    trips = 0
    curr_sum = 0
    i = 0
    while total_sum >= 0:
        if curr_sum + weight[i] <= 3.0:
            curr_sum = curr_sum + weight[i]
        elif curr_sum == 3.0:
            trips += 1
            total_sum = total_sum - curr_sum
            curr_sum = weight[i]
            i += 1
        else:
            trips += 1
            total_sum = total_sum - curr_sum
            curr_sum = weight[i]
            i += 1
    return trips

wt = [1.01, 1.01, 1.4, 2.4]
print(efficientJanitor(wt))

# weight.sort(reverse=True)
#     total_sum = sum(weight)
#     trips = 0
#     curr_sum = 0
#     for i in range(len(weight)):
#         if curr_sum + weight[i] <= 3.0:
#             curr_sum = curr_sum + weight[i]
#         else:
#             trips += 1
#             total_sum = total_sum - curr_sum
#             curr_sum = weight[i]
#     return trips + 1