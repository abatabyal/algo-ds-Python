def restock(items, target):
    curr_sum = 0
    nos_items = len(items)
    for i in range(nos_items):
        curr_sum = curr_sum + items[i]
        if curr_sum == target:
            return 0
        if curr_sum < target and (i+1) == nos_items:
            return target - curr_sum
        if curr_sum > target and (i+1) <= nos_items:
            return curr_sum - target

items = [174, 156, 167, 138, 187, 111, 196, 140, 100, 156]
target = 1522
print(restock(items, target))
