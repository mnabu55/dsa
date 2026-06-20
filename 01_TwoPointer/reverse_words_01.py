def reverse_words_wa(sentence):
    s = list(sentence[::-1])
    n = len(s)
    start, end = 0, 0
    while end < n:
        if s[end] == " " or end == n - 1:
            left, right = start, end - 1
            while left < right:
                s[left], s[right] = s[right], s[left]
                left += 1
                right -= 1
            end += 1
        elif s[end] != " ":
            end += 1
            continue

        # 空白をスキップする。次の単語の先頭に移動する
        while s[end] == " ":
            end += 1
        start = end

    # Replace this placeholder return statement with your code
    return "".join([c for c in s])


import re

def reverse_words(sentence):
    # 連続する空白を1つの空白に変換　←　この部分が実装できなかった。今後の課題
    sentence = re.sub(' +', ' ', sentence.strip())
    sentence = list(sentence)
    n = len(sentence)

    reverse(sentence, 0, n - 1)

    start = 0
    for end in range(n):
        if end == n - 1 or sentence[end] == ' ':
            end_idx = end if end == n - 1 else end - 1
            reverse(sentence, start, end_idx)
            start = end + 1

    return ''.join(sentence)


def reverse(s, start, end):
    while start < end:
        s[start], s[end] = s[end], s[start]
        start += 1
        end -= 1


s = ' Reverse this   string '
print(f"output: [{reverse_words(s)}]")

