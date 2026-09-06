class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        stack = {}
        for letter in s:
            if letter in t:
                if letter in stack:
                    stack[letter] += 1
                else:
                    stack[letter] = 1
        for letter in t:
            if letter in stack:
                stack[letter] -= 1
            else:
                return False
            if stack[letter] == 0:
                del stack[letter]
        return True
        


        