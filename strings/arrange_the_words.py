def arrange(sentence):
    split_sentence = sentence.split(' ')
    split_sentence[-1] = split_sentence[-1].replace('.','')
    split_sentence[0] = split_sentence[0].lower()
    for i in range(1, len(split_sentence)):
        temp = split_sentence[i]
        j = i - 1
        while j >= 0 and len(temp) < len(split_sentence[j]):
            split_sentence[j + 1] = split_sentence[j]
            j -= 1
        split_sentence[j + 1] = temp
    split_sentence[-1] = split_sentence[-1]+'.'
    split_sentence[0] = split_sentence[0].capitalize()
    print(split_sentence)
    op = " ".join(split_sentence)
    print(op)

sentence = "I love to code."
arrange(sentence)