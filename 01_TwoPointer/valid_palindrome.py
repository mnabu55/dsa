'''
# Statement
Write a function that takes a string as input and checks whether it can be a valid palindrome by removing at most one character from it.

# Constraints:

- 1≤ string.length ≤ 10 ** 5
- The string only consists of English letters.
'''

def is_palindrome(s):
    left = 0
    right = len(s) - 1

    while left < right:
        if s[left] != s[right]:
            return False
        left = left + 1 
        right = right - 1
    
    return True


def is_palindrome2(s):
    left = 0
    right = len(s) - 1

    while left < right:
        # s[left] is not alaphabet or number, increase left point
        while left < right and not s[left].isalnum():
            left += 1
        # s[right] is not alaphabet or number, decrease right point
        while left < right and not s[right].isalnum():
            right -= 1
        
        if s[left].lower() != s[right].lower():
            return False
        
        left = left + 1 
        right = right - 1
    
    return True



# Driver Code
def main():

    test_cases = ["RACEACAR", "A", "ABCDEFGFEDCBA",
                  "ABC", "ABCBA", "ABBA", "RACEACAR", "A man, a plan, a canal: Panama"]
    for i in range(len(test_cases)):
        print("Test Case #", i + 1)
        print("-" * 50)
        print("The input string is '", test_cases[i], "' and the length of the string is ", len(test_cases[i]), ".", sep='')
        print("Is it a palindrome?.....", is_palindrome2(test_cases[i]))
        print("-" * 50)


if __name__ == '__main__':
    main()
