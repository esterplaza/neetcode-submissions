class Solution:
    def isValid(self, s: str) -> bool:
        types = {")":"(", "]":"[", "}":"{"}
        stack = []
        for char in s:
            if char in types.values():
                stack.append(char)
            else:
                if not stack:
                    return False
                else:
                    if types[char] == stack[-1]:
                        stack.pop()
                    else:
                        return False
        if not stack:
            return True
        else:
            return False



