def pdf_viewer(h, arr):
    max_height = 0
    for w in arr:
        if h[ord(w) - 97] > max_height:
            max_height = h[ord(w) - 97]
    return max_height * len(arr)

h = [1,3,1,3,1,4,1,3,2,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,7]
word = "zaba"
print(pdf_viewer(h, word))