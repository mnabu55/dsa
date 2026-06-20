import re

def reverse_words(sentence):
    sentence = re.sub(' +', ' ', sentence.strip())
    s = list(sentence)
    n = len(s)
    reverse(s, 0, n - 1)

    left = 0
    for right in range(n):
        if right == n - 1:
            reverse(s, left, right)
        elif s[right] == ' ':
            reverse(s, left, right - 1)
            left = right + 1

    return ''.join(s)

def reverse(s, start, end):
    while start < end:
        s[start], s[end] = s[end], s[start]
        start += 1
        end -= 1


sentence = "Hello   World   manabu"
print(reverse_words(sentence))
