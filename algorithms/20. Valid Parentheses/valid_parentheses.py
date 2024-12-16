def isValid(s: str) -> bool:
    stack = []
    closing_parentheses = {")": "(", "}": "{", "]": "["}
    for char in s:
        if char in closing_parentheses:
            if stack and stack[-1] == closing_parentheses[char]:
                stack.pop()
            else:
                return False
        else:
            stack.append(char)
    return True if not stack else False
