class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded = ""
        for word in strs:
            encoded += "".join(str(len(word)) + "!" + word)
        return encoded

    def decode(self, s: str) -> List[str]:
        decoded = []
        i = 0

        while i < len(s):
            str_length = ""
            while s[i] != "!":
                str_length += s[i]
                i += 1
            
            length = int(str_length)
            i += 1

            words = s[i:i+length]
            decoded.append(words)
            i += length

        return decoded


