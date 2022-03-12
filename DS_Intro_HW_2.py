def reverse(sentence,reverse_word):
    s=sentence.split()
    if type(reverse_word) is not str:
        return 'invalid input'
    else:
        for i in s:
            if i==reverse_word:
                x=reverse_word[::-1]
                break
            else:
                x='no match word found'
        return x
