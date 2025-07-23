class Solution:

    def encode(self, strs: List[str]) -> str:
        x = ""
        for i in strs:
            x += str(len(i)) + "~" + i
        return x
    def decode(self, s: str) -> List[str]:
        strs = []
        i = 0
        while i < len(s):
            x = i
            while s[x] != "~":
                x += 1
            length = int(s[i:x])
            i = x + 1
            x = i + length
            strs.append(s[i:x])
            i = x
        return strs
