class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        unique = set(nums)
        greatest = 0
        for i in unique:
            if i-1 not in unique:
                length = 1
                while i+length in unique:
                    length+=1
                greatest = max(greatest, length)
        return greatest
            
