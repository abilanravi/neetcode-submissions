class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        bracketPair = {")":"(", "]":"[", "}":"{"}

        for char in s:
            if char in bracketPair:
                if stack and stack[-1] == bracketPair[char]:
                    stack.pop()
                else:
                    return False

            else:
                stack.append(char)
        
        return True if not stack else False
            
            
            
        
        