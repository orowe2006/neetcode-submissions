import re

class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = re.sub(r'[^a-zA-Z0-9]','',s).replace(' ', '').lower()
        
        print(s)

        for i in range(int(len(s)/2)):
            if s[i] != s[len(s) - i - 1]:
                return False
        return True