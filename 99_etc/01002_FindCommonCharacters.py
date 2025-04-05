from typing import List
from collections import Counter


class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
        if not words:
            return []

        # 最初の文字列の文字の出現回数を基準にする
        common_counts = Counter(words[0])

        # 残りの文字列との共通文字を調べる
        for word in words[1:]:
            word_counts = Counter(word)
            common_counts = {
                char: min(common_counts.get(char, 0), word_counts.get(char, 0))
                for char in common_counts
            }

        # 共通文字をリストに変換する
        result = []
        for char, count in common_counts.items():
            result.extend([char] * count)

        return result
        

def main():
    words_list = [
        ["bella","label","roller"],
        ["cool","lock","cook"],
        ["cool"],
        []
    ]

    solution = Solution()
    for words in words_list:
        print(f"words: {words}")
        print(f"common characters: {solution.commonChars(words)}")


if __name__ == "__main__":
    main()
