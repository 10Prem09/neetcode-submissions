class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # we need to find top k frequent
        # we do this by first fidning coutna dn storing it, then placing each count 
        # in bucket sort format
        # then interate from last until we get top k. 
        counts = {}
        frequencies = [[] for i in range(len(nums)+1)]
        for num in nums:
            counts[num] = counts.get(num,0) + 1
        for num,freq in counts.items():
            frequencies[freq].append(num)
        output = []
        for i in range(len(frequencies)- 1, 0, -1):
            for freq in frequencies[i]:
                output.append(freq)
                if len(output)==k:
                    return output

        