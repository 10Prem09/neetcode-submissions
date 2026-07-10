class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashMap = {}
        for i in range(len(nums)):
            if target - nums[i] in hashMap:
                returnList = sorted([i, hashMap[target-nums[i]]])
                return returnList
            else:
                hashMap[nums[i]] = i
        
