def breakingRecords(scores):
    min = scores[0]
    min_changes = 0
    max = scores[0]
    max_changes = 0
    for s in range(len(scores)):
        if scores[s] < min:
            min = scores[s]
            min_changes += 1
        if scores[s] > max:
            max = scores[s]
            max_changes += 1
    return max_changes, min_changes


score_array = [10, 5, 20, 20, 4, 5, 2, 25, 1]
breakingRecords(score_array)
