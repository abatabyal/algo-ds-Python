NO_OF_CHARS = 256

def longest_nrcs(word):
    n = len(word)
    curr_len = 1
    max_len = 1
    prev_index = 0
    i = 0

    visited = [-1] * NO_OF_CHARS

    visited[ord(word[0])] = 0

    for i in range(1, n):
        prev_index = visited[ord(word[i])]

        if prev_index == -1 or (i - curr_len > prev_index):
            curr_len += 1
        else:
            if curr_len > max_len:
                max_len = curr_len
            curr_len = i - prev_index

        visited[ord(word[i])] = i

    if curr_len > max_len:
        max_len = curr_len

    return max_len

string = "ABDEFGABEF"
print( "The input string is " + string)
length = longest_nrcs(string)
print("The length of the longest non-repeating character" +
       " substring is " + str(length))