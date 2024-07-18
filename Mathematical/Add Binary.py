class Solution:
    def addBinary(self, a: str, b: str) -> str:
        s=bin(int(a,2)+int(b,2))
        return str(s[2:])
