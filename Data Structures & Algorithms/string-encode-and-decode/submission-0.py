from typing import List

class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded = ""
        for word in strs:
            encoded += "".join(str(len(word)) + "#" + word)
        return encoded

    def decode(self, s: str) -> List[str]:
        decoded = []
        i = 0
        
        while i < len(s):
            length_str = ""
            
            while s[i] != "#":
                length_str += s[i]
                i += 1
            
            length = int(length_str)
            i += 1

            words = s[i : i + length]
            decoded.append(words)
            i += length

        return decoded

            


