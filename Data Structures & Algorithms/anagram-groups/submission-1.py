class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        keeper = defaultdict(list)

        for s in strs:
            count = [0] * 26
            for i in range(len(s)):
                count[ord(s[i]) - ord('a')] += 1
        
            temp = tuple(count)

            keeper[temp].append(s)

        return list(keeper.values())

    