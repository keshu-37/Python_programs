def r_words(sentence):
    words = sentence.split()
    reverse_list = words[: :-1]
    return ' '.join(reverse_list)

sentence = "I Love Coding"
a= r_words(sentence)
print(a)
