class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        # the array is sorted so can use divide and conquer. 
        i,j = 0,len(numbers)-1
        while i<j:
            intsum = numbers[i] + numbers[j]
            if intsum == target:
                return [i+1,j+1]
            elif intsum < target:
                i+=1
            else:
                j-=1