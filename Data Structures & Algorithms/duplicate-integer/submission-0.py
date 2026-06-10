class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        
        known = []
        
        for n in nums:
            if n in known:
                return True
            
            known.append(n)

        return False
        