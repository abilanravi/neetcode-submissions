class Solution:
    def isPalindrome(self, s: str) -> bool:
        word = ""

        for char in s:
            if char.isalnum():
                word += char.lower()

        reversed = word[::-1]

        if reversed == word:
            return True

        return False
        