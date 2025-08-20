"""
# approach

use stack.
if there is open paren, push stack.
if there is close paren, check if character of top stack element is equal
current character
"""
def is_valid(s: str) -> bool:
    parens = {
        "(": ")",
        "{": "}",
        "[": "]",
    }
    stack = []

    for char in s:
        if char in parens:
            stack.append(char)
        elif char in parens.values():
            if not stack or char != parens[stack.pop()]:
                return False
    
    return not stack


# Driver code
def main():
    inputs = ["(){}[]", "{}[]{}[{}])", "(){[{()}]}", "))){{}}}]]", "{[()}"]

    for i in range(len(inputs)):
        print(i + 1, ". Input string = ", inputs[i], sep="")
        print("   Valid parentheses = ", is_valid(inputs[i]), sep="")
        print("-" * 100)


if __name__ == "__main__":
    main()