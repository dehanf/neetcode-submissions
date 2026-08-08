from collections import defaultdict
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        num_occ = defaultdict(int) #number occurences
        for num in nums:
            num_occ[num] += 1
        
        final = []
        for key,val in num_occ.items():
            if val >= k:
                final.append(key)
        return final
         