'''
Given a string s, return the minimum number of moves required to transform s into a palindrome. In each move, you can swap any two adjacent characters in s.

Note: The input string is guaranteed to be convertible into a palindrome.

Constraints:

-1 ≤ s.length ≤ 2000
-s consists of only lowercase English letters.
-s is guaranteed to be converted into a palindrome in a finite number of moves.
'''

def min_moves_to_make_palindrome(s):
    s = list(s)
    
    moves = 0

    i, j = 0, len(s) - 1
    while i < j:
        k = j
        while k > i:
            if s[i] == s[k]:
                for m in range(k, j):
                    s[m], s[m + 1] = s[m + 1], s[m]
                    moves += 1
                j -= 1
                break
            k -= 1
        if k == i:
            moves += len(s) // 2 - i
        i += 1

    return moves

# Driver code
def main():
    strings = ["ccxx", "arcacer", "w", "ooooooo", "eggeekgbbeg"]
    
    for index, string in enumerate(strings):
        print(f"{index + 1}.\ts: {string}")
        print(f"\tMoves: {min_moves_to_make_palindrome(string)}")
        print('-' * 100)

if __name__ == "__main__":
    main()
