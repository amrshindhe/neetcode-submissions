class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        resultS = ''.join(sorted(s))
        resultT = ''.join(sorted(t))

        return resultS==resultT
