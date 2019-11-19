def climbingLeaderboard(scores, alice):
    #calculate ranking for existing scores
    ranks = [None] * len(scores)
    score_dict = {}
    for s in range(1, len(scores) + 1):
        if s == 1:
            ranks[0] = 1
        else:
            if scores[s-2] == scores[s-1]:
                ranks[s-1] = ranks[s-2]
            else:
                ranks[s - 1] = ranks[s - 2] + 1
        score_dict[scores[s - 1]] = ranks[s - 1]
    #calculate rank for each of alice's game
    for a in alice:
        closest_score = (closest_binary_search(scores, a))
        if a == closest_score:
            print(score_dict[closest_score])
        elif a < closest_score:
            print(score_dict[closest_score] + 1)
        elif a > closest_score:
            if score_dict[closest_score] == 1:
                print(1)
            else:
                print(score_dict[closest_score] - 1)

def closest_binary_search(arr, target):
    n = len(arr)
    arr.sort()
    if target <= arr[0]:
        return arr[0]
    if target >= arr[-1]:
        return arr[-1]

    #binary search
    i = 0; j = n; mid = 0
    while i < j:
        mid = (i + j)//2
        if arr[mid] == target:
            return arr[mid]

        if target < arr[mid]:
            if mid > 0 and target > arr[mid - 1]:
                return get_closest(arr[mid-1], arr[mid], target)
            j = mid

        else:
            if mid < n - 1 and target < arr[mid + 1]:
                return get_closest(arr[mid], arr[mid+1], target)
            i = mid + 1
    return  arr[mid]

def get_closest(val1, val2, target):
    if target - val1 >= val2 - target:
        return val2
    else:
        return val1
# scores = [100, 90, 90, 80, 75, 60]
# alice = [50, 65, 77, 90, 102]
scores = [997,981,957,933,930,927,926,920,916,896,887,874,863,863,858,847,815,809,803,794,789,785,783,778,764,755,751,
          740,737,730,691,677,652,650,587,585,583,568,546,541,540,538,531,527,506,493,457,435,430,427,422,422,414,404,
          400,394,387,384,374,371,369,369,368,365,363,337,336,328,325,316,314,306,282,277,230,227,212,199,179,173,171,
          168,136,125,124,95,92,88,85,70,68,61,60,59,44,43,28,23,13,12]
alice = [12,20,30,32,35,37,63,72,83,85,96,98,98,118,122,125,129,132,140,144,150,164,184,191,194,198,200,220,228,229,229,
         236,238,246,259,271,276,281,283,287,300,302,306,307,312,318,321,325,341,341,341,344,349,351,354,356,366,369,370,
         379,380,380,396,405,408,417,423,429,433,435,438,441,442,444,445,445,452,453,465,466,467,468,469,471,475,482,489,
         491,492,493,498,500,501,504,506,508,523,529,530,539,543,551,552,556,568,569,571,587,591,601,602,606,607,612,614,
         619,620,623,625,625,627,638,645,653,661,662,669,670,676,684,689,690,709,709,710,716,724,726,730,731,733,737,744,
         744,747,757,764,765,765,772,773,774,777,787,794,796,797,802,805,811,814,819,819,829,830,841,842,847,857,857,859,
         860,866,872,879,882,895,900,900,903,905,915,918,918,922,925,927,928,929,931,934,937,955,960,966,974,982,988,996,
         996]
climbingLeaderboard(scores, alice)
