import re
def convert_variable(x):
    # convert java variable to c++
    # and vice versa
    # java = thisIsAVariable
    # c++ = this_is_a_variable
    # check if variable contains '_'
    if '_' in x:
        # c++ variable, convert to java
        list_of_words = x.split('_')
        for i in range(1, len(list_of_words)):
            list_of_words[i] = list_of_words[i].capitalize()
        x = " ".join(list_of_words)
        print(x.replace(" ", ""))
    else:
        #java to c++ variable
        first_word = ''
        for f in x:
            if not f.isupper():
                first_word += f
            else:
                break
        java_words = re.findall('[A-Z][a-z]*', x)
        java_words = [j.lower() for j in java_words]
        op = [None] * (len(java_words) + 1)
        op[0] = first_word
        for j in range(1, len(java_words) + 1):
            op[j] = java_words[j - 1]
        op = " ".join(op)
        print(op.replace(" ", "_"))

convert_variable('thisIsAVariable')