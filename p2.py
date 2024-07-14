def reconstructSentence(s):
    words = s.split()
    sorted_words = sorted(words, key=lambda x: int(x[-1]))
    result = ' '.join(word[:-1] for word in sorted_words)
    return result
