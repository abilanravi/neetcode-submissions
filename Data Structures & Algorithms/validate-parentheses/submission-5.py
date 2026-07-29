class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        brackPair = {")":"(", "]":"[", "}":"{"}

        for char in s:
            if char in brackPair:
                if stack and stack[-1] == brackPair[char]:
                    stack.pop()
                else:
                    return False
                
            else:
                stack.append(char)
            
        return True if not stack else False 
        