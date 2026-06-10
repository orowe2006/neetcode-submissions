class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        l1 = []

        for i in range(len(s)):
            l1.append(ord(s[i]))

        for i in range(len(t)):
            try:
                l1.remove(ord(t[i]))
            except:
                return False

        return True