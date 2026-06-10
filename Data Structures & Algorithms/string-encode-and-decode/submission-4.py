class Solution:

    def encode(self, strs: List[str]) -> str:
        word = ""
        for s in strs:
            word += (s + "$12@")
        return word

    def decode(self, s: str) -> List[str]:
        l = s.split("$12@")
        l.pop()
        return l