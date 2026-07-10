class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        '''
        Here to find the sum of two numbers which is equal to the required sum. 
        To find a solution which is optimal. How can it be done is the question. 

        
        Hash Map ? -> But how and why ? 
        even if i eliminate num > target, that doesnt say anything, also since integer
        number can also be -ve so this wont work. 
        What will be stored in the hash map ?
        so we store element as key and index as value 
        '''

        hashMap = {}
        for i in range(len(nums)):
            if target - nums[i] in hashMap:
                returnList = sorted([i, hashMap[target-nums[i]]])
                return returnList
            else:
                hashMap[nums[i]] = i
            print(hashMap)

        
