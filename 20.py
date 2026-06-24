class Solution(object):
    def isValid(self, s):
        stack = []
        mapping = {")": "(", "}": "{", "]": "["}
        for char in s:
            if char in "({[":
                stack.append(char)
            else:
                if not stack:
                    return False
                top_bracket = stack.pop()
                if mapping[char] != top_bracket:
                    return False
        return len(stack) == 0
