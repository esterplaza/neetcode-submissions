class Solution:
    def isPalindrome(self, s: str) -> bool:
        index = 0
        last_index = -1
        new_s = s
        for letter in s:
            if not letter.isalnum():
                new_s = new_s.replace(letter, "")
                print(new_s)
        new_s = new_s.lower()
        new_s = new_s.replace(" ", "")
        length = len(new_s)
        if length <= 1:
            return True
        while new_s[index] == new_s[last_index]:
            index += 1
            last_index -= 1
            if index >= length/2 + 1:
                print(index)
                return True
        return False 


            
