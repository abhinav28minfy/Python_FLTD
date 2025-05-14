def word_frequency(text):
    d={}
    for word in text.split():
        if word in d:
            d[word]+=1
        else:
            d[word]=1
    return d

text = "the quick brown fox jumps over the lazy dog"
print(word_frequency(text))