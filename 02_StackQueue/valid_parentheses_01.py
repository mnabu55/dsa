def is_valid(s: str) -> bool:
    parentheses = {')': '(', '}': '{', ']': '['}
    stack = []

    for char in s:
        if char in parentheses:
            stack.append(char)
        elif char in parentheses.values():
            if not stack or char != parentheses[stack.pop()]:
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