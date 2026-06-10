class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        arr1 = list(s)
        arr2 = list(t)

        arr1 = sorted(arr1)
        arr2 = sorted(arr2)

        if len(arr1) != len(arr2):
            return False

        for i in range(len(arr1)):
            if arr1[i] != arr2[i]:
                return False

        return True