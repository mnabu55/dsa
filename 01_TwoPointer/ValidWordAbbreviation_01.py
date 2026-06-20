'''
# Problem statement
Given a string wordand an abbreviation abbr, return TRUE if the abbreviation matches the given string. Otherwise, return FALSE.

A certain word "calendar"can be abbreviated as follows:

- "cal3ar"("cal endar"skipping three characters "end"from the word "calendar"still matches the provided abbreviation)
- "c6r"("c alendar"skipping six characters "alenda"from the word "calendar"still matches the provided abbreviation)

The word "internationalization"can also be abbreviated as "i18n"(the abbreviation comes from skipping 18 characters in "internationalization", leaving the first and last letters "i"and "n").

The following are notvalid abbreviations:

- "c06r"(has leading zeroes)
- "cale0ndar"(replaces an empty string)
- "c24r"("c alendar"the replaced substringsare adjacent)

# Constraints:

- 1≤1≤word.length≤20≤20
- word consists of only lowercase English letters.
- 1≤1≤abbr.length≤10≤10
- abbr consists of lowercase English letters and digits.
- All the integers in abbr will fit in a 3232–bit integer.
'''

def valid_word_abbreviation(word, abbr):
    n_word = len(word)
    n_abbr = len(abbr)
    word_index, abbr_index = 0, 0

    while abbr_index < n_abbr:
        if abbr[abbr_index].isalpha():
            if word_index >= n_word or word[word_index] != abbr[abbr_index]:
                return False
            word_index += 1
            abbr_index += 1
        elif abbr[abbr_index].isdecimal():
            if abbr[abbr_index] == '0':
                return False
            left, right = abbr_index, abbr_index
            while right < n_abbr and abbr[right].isdecimal():
                right += 1
            word_index += int(abbr[left:right])
            abbr_index = right
    
    return word_index == n_word and abbr_index == n_abbr


def main():
    # words = ['innovation', 'mindset', 'internationalization']
    # abbrs = ['in5ion', 'min3et', '13iz4n']
    # expecteds = [True, False, True]
    words = ['internationalization']
    abbrs = ['13iz4n']
    expecteds = [True]

    n = len(words)
    for i in range(n):
        word = words[i]
        abbr = abbrs[i]
        expected = expecteds[i]
        actual = valid_word_abbreviation(word, abbr)
        assert actual == expected, f"case [{i}], failed."


if __name__ =="__main__":
    main()
