class Solution:
    def isValid(self, s: str) -> bool:
        typen = {")":"(", "]":"[", "}":"{"}
        stack = []
        for char in s:
            if char in typen.values():
                stack.append(char)
            else:
                if not stack:
                    return False
                else:
                    if typen[char] == stack[-1]:
                        stack.pop()
                    else:
                        return False
        if not stack:
            return True
        else:
            return False



