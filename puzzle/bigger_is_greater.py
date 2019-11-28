"""
next permutation in lexicographic ordering, if it exists
Find the largest index k such that a[k] < a[k + 1]. If no such index exists,
the permutation is the last permutation.
Find the largest index l greater than k such that a[k] < a[l].
Swap the value of a[k] with that of a[l].
Reverse the sequence from a[k + 1] up to and including the final element a[n].
"""
def biggerIsGreater(w):
    word = list(w)
    first_char_index = 0
    ceiling_index = 0
    first_char = None
    answer = None
    for j in range(len(word)-1):
        if ord(word[j]) < ord(word[j+1]):
            first_char = word[j]
            first_char_index = j
        else:
            continue

    if first_char != None:
        for i in range(first_char_index + 1, len(word)):
            if ord(word[i]) > ord(first_char):
                ceiling_index = i

        word[first_char_index], word[ceiling_index] = word[ceiling_index], word[first_char_index]

        word_f = word[:first_char_index+1] + sorted(word[first_char_index+1:])
        answer = "".join(word_f)

    if answer == w or first_char == None:
        answer = "no answer"

    return answer

word="fedcbabcd"
print(biggerIsGreater(word))