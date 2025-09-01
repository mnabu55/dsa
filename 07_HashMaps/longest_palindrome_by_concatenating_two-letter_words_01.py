# # Statement
# Suppose you are given an array of strings, words, and each element in the array has a length of two. 
# You need to return the length of the longest palindrome that can be made by concatenating some elements from words. If no palindrome can be made, return 0.
#
# A palindrome is a sequence of characters that reads the same forward and backward.

def longest_palindrome(words):
    # 単語の出現回数をカウント
    count = Counter(words)
    total_length = 0
    center_used = False

    # 1. 反転ペアの処理
    for word in count.keys():
        reverse = word[::-1]
        if word != reverse and reverse in count:
            # ペアにできる回数
            pairs = min(count[word], count[reverse])

            # 1ペアで長さ4
            total_length += pairs * 4

            # 両方のカウントを消費
            count[word]   -= pairs
            count[reverse]-= pairs

    # 2. 自己ペアの処理 ("aa", "bb"など)
    for word in count.keys():
        if word[0] == word[1]:
            pairs = count[word] // 2   # 偶数ペア
            total_length += pairs * 4
            count[word] -= pairs * 2

            # もし1つ余っていれば中央に置ける
            if not center_used and count[word] > 0:
                total_length += 2
                center_used = True

    return total_length