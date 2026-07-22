class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded_string = ""
        for i in strs:
            encoded_string = encoded_string + str(len(i)) + "#" + i
        return (encoded_string)

    def decode(self, s: str) -> List[str]:
        decoded_strings = []
        i = 0
        while i < len(s):
            j = i
            while s[j]!='#':
                j+=1
            length = int(s[i:j])
            decoded_strings.append(s[j+1 : j + 1 + length])
            i = j + 1 + length
            j = i
        return decoded_strings
